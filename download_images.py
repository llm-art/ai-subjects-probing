#!/usr/bin/env python3
"""Download full-resolution images from IIIF links.

Input: a CSV (default: data/images.csv) with columns:
    id        - short slug used as the output filename
    iiif_url  - any of:
                  * IIIF Image API info.json URL
                  * IIIF Image API base/service URL (info.json appended)
                  * IIIF Presentation manifest URL (v2 or v3; first canvas used,
                    or all canvases with --all-canvases)
                  * a direct image URL (downloaded as-is)
    any other columns are carried through to the output log.

Output: images saved to data/images/<id>.<ext> plus data/download_log.json
recording the resolved full-res URL, dimensions, and IIIF metadata for each item.

Full resolution strategy: ask the Image API for /full/max/0/default.jpg
(v3) or /full/full/0/default.jpg (v2). If the server enforces maxWidth/
maxHeight/maxArea below the native size, fall back to tiled assembly so we
still get true full resolution.
"""

import argparse
import csv
import io
import json
import math
import sys
import time
from pathlib import Path

import requests
from PIL import Image
from tqdm import tqdm

Image.MAX_IMAGE_PIXELS = None  # museum scans can exceed PIL's default bomb limit

HEADERS = {"User-Agent": "ai-subjects-probing/0.1 (research; IIIF full-res downloader)"}
TIMEOUT = 60
RETRIES = 3


def get(url, **kw):
    last = None
    for attempt in range(RETRIES):
        try:
            r = requests.get(url, headers=HEADERS, timeout=TIMEOUT, **kw)
            r.raise_for_status()
            return r
        except requests.RequestException as e:
            last = e
            time.sleep(2 ** attempt)
    raise RuntimeError(f"GET failed after {RETRIES} attempts: {url} ({last})")


def is_manifest(doc):
    t = doc.get("@type") or doc.get("type") or ""
    return "Manifest" in (t if isinstance(t, str) else " ".join(t))


def image_services_from_manifest(doc):
    """Yield (canvas_label, image-service base URL or direct image URL)."""
    # v2
    for seq in doc.get("sequences", []):
        for canvas in seq.get("canvases", []):
            label = canvas.get("label", "")
            for img in canvas.get("images", []):
                res = img.get("resource", {})
                svc = res.get("service", {})
                svc_id = svc.get("@id") or svc.get("id")
                yield label, svc_id or res.get("@id")
    # v3
    for canvas in doc.get("items", []):
        label = canvas.get("label", "")
        if isinstance(label, dict):
            label = "; ".join(v[0] for v in label.values() if v)
        for page in canvas.get("items", []):
            for anno in page.get("items", []):
                body = anno.get("body", {})
                if isinstance(body, list):
                    body = body[0] if body else {}
                services = body.get("service", [])
                if isinstance(services, dict):
                    services = [services]
                svc_id = None
                for svc in services:
                    svc_id = svc.get("@id") or svc.get("id")
                    if svc_id:
                        break
                yield label, svc_id or body.get("id")


def normalize_service_url(url):
    return url[: -len("/info.json")] if url.endswith("/info.json") else url.rstrip("/")


def fetch_info(service_url):
    info = get(service_url + "/info.json").json()
    # Use the canonical @id / id from the response as the service base so that
    # image requests go to the correct versioned path (e.g. /iiif/2/NNN not /iiif/NNN).
    canonical = info.get("@id") or info.get("id")
    if canonical:
        info["_service_url"] = canonical.rstrip("/")
    return info


def max_constraints(info):
    """Return (max_w, max_h) the server will serve in one request, or None if unconstrained."""
    w, h = info["width"], info["height"]
    mw = info.get("maxWidth")
    mh = info.get("maxHeight")
    ma = info.get("maxArea")
    # v2 puts these inside profile list entries
    for p in info.get("profile", []) if isinstance(info.get("profile"), list) else []:
        if isinstance(p, dict):
            mw = mw or p.get("maxWidth")
            mh = mh or p.get("maxHeight")
            ma = ma or p.get("maxArea")
    if mw is None and mh is None and ma is None:
        return None
    cw, ch = mw or w, mh or h
    if ma and cw * ch > ma:
        scale = math.sqrt(ma / (cw * ch))
        cw, ch = int(cw * scale), int(ch * scale)
    return (min(cw, w), min(ch, h))


def full_size_segment(info):
    ctx = info.get("@context", "")
    ctx = ctx if isinstance(ctx, str) else " ".join(map(str, ctx))
    return "full/max" if "image/3" in ctx else "full/full"


def download_single(service_url, info, dest):
    url = f"{service_url}/{full_size_segment(info)}/0/default.jpg"
    r = get(url, stream=True)
    with open(dest, "wb") as f:
        for chunk in r.iter_content(1 << 16):
            f.write(chunk)
    return url


def download_tiled(service_url, info, dest):
    """Assemble the image from full-resolution region tiles when the server
    caps single-request size below the native dimensions."""
    w, h = info["width"], info["height"]
    cons = max_constraints(info)
    tile = min(cons[0], cons[1], 2048) if cons else 2048
    canvas = Image.new("RGB", (w, h))
    cols, rows = math.ceil(w / tile), math.ceil(h / tile)
    for ty in range(rows):
        for tx in range(cols):
            x, y = tx * tile, ty * tile
            rw, rh = min(tile, w - x), min(tile, h - y)
            url = f"{service_url}/{x},{y},{rw},{rh}/{rw},/0/default.jpg"
            part = Image.open(io.BytesIO(get(url).content))
            canvas.paste(part, (x, y))
    canvas.save(dest, "JPEG", quality=95)
    return f"{service_url} (tiled {cols}x{rows})"


def download_from_service(service_url, dest_stem, force_tiled=False):
    service_url = normalize_service_url(service_url)
    info = fetch_info(service_url)
    # Prefer the canonical service URL from the info.json @id over the request URL
    service_url = info.get("_service_url", service_url)
    w, h = info["width"], info["height"]
    dest = dest_stem.with_suffix(".jpg")
    cons = max_constraints(info)
    needs_tiling = force_tiled or (cons is not None and (cons[0] < w or cons[1] < h))
    if needs_tiling:
        resolved = download_tiled(service_url, info, dest)
    else:
        resolved = download_single(service_url, info, dest)
        # verify we actually got native resolution; some servers silently downscale
        with Image.open(dest) as im:
            gw, gh = im.size
        if gw < w or gh < h:
            resolved = download_tiled(service_url, info, dest)
    with Image.open(dest) as im:
        gw, gh = im.size
    return {
        "file": str(dest),
        "resolved_url": resolved,
        "native_size": [w, h],
        "downloaded_size": [gw, gh],
        "full_resolution": gw >= w and gh >= h,
    }


def download_direct(url, dest_stem):
    ext = Path(url.split("?")[0]).suffix or ".jpg"
    dest = dest_stem.with_suffix(ext)
    r = get(url, stream=True)
    with open(dest, "wb") as f:
        for chunk in r.iter_content(1 << 16):
            f.write(chunk)
    with Image.open(dest) as im:
        gw, gh = im.size
    return {
        "file": str(dest),
        "resolved_url": url,
        "native_size": None,
        "downloaded_size": [gw, gh],
        "full_resolution": None,
    }


def process_row(row, out_dir, all_canvases=False):
    url = row["iiif_url"].strip()
    stem = out_dir / row["id"].strip()
    results = []

    # Try to interpret the URL: manifest? image service? direct image?
    if url.endswith("/info.json"):
        results.append(download_from_service(url, stem))
        return results

    try:
        doc = get(url).json()
    except (RuntimeError, ValueError):
        doc = None

    if doc and is_manifest(doc):
        services = list(image_services_from_manifest(doc))
        if not services:
            raise RuntimeError(f"manifest has no image services: {url}")
        if not all_canvases:
            services = services[:1]
        for i, (label, svc) in enumerate(services):
            s = stem if len(services) == 1 else out_dir / f"{row['id']}_{i:03d}"
            res = download_from_service(svc, s) if "/full/" not in svc else download_direct(svc, s)
            res["canvas_label"] = label
            results.append(res)
    elif doc and ("width" in doc and "height" in doc):  # it was an info.json without the suffix
        results.append(download_from_service(url, stem))
    else:
        # not JSON: either an Image API base URL or a direct image
        try:
            results.append(download_from_service(url, stem))
        except Exception:
            results.append(download_direct(url, stem))
    return results


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", default="data/images.csv", help="input CSV (id,iiif_url,...)")
    ap.add_argument("--out", default="data/images", help="output directory")
    ap.add_argument("--log", default="data/download_log.json", help="JSON log of downloads")
    ap.add_argument("--all-canvases", action="store_true", help="download every canvas of a manifest, not just the first")
    ap.add_argument("--skip-existing", action="store_true", help="skip ids that already have a file in the output dir")
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    delim = "\t" if args.input.endswith(".tsv") else ","
    with open(args.input, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f, delimiter=delim) if r.get("iiif_url", "").strip()]

    log_path = Path(args.log)
    log = json.loads(log_path.read_text()) if log_path.exists() else {}
    failures = []

    for row in tqdm(rows, unit="img"):
        rid = row["id"].strip()
        if args.skip_existing and list(out_dir.glob(rid + ".*")):
            continue
        try:
            results = process_row(row, out_dir, args.all_canvases)
            log[rid] = {"source": row, "downloads": results}
        except Exception as e:
            failures.append((rid, str(e)))
            log[rid] = {"source": row, "error": str(e)}
        log_path.write_text(json.dumps(log, indent=2, ensure_ascii=False))

    ok = sum(1 for v in log.values() if "downloads" in v)
    print(f"\n{ok}/{len(rows)} downloaded. Log: {log_path}")
    if failures:
        print("Failures:", file=sys.stderr)
        for rid, err in failures:
            print(f"  {rid}: {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
