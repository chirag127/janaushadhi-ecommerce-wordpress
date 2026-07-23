#!/usr/bin/env python3
"""Split products.csv into ~500-row chunks for throttled free hosting (InfinityFree).

WooCommerce > Products > Import times out on InfinityFree with 2,439 rows. Each
chunk keeps the header row so it imports standalone. Import the chunks in order;
WooCommerce dedupes by SKU so re-running is safe.

Usage:  python scripts/split-products-csv.py [rows_per_chunk]   (default 500)
Output: import/chunks/products-01.csv, products-02.csv, ...
"""
import csv
import os
import sys

ROWS = int(sys.argv[1]) if len(sys.argv) > 1 else 500
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(HERE, "import", "products.csv")
OUT = os.path.join(HERE, "import", "chunks")

os.makedirs(OUT, exist_ok=True)

with open(SRC, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

chunks = [rows[i : i + ROWS] for i in range(0, len(rows), ROWS)]
for idx, chunk in enumerate(chunks, 1):
    path = os.path.join(OUT, f"products-{idx:02d}.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(chunk)
    print(f"  wrote {os.path.relpath(path, HERE)} ({len(chunk)} products)")

print(f"\nDone: {len(rows)} products -> {len(chunks)} files of <= {ROWS} rows.")
print("Import each in order via WooCommerce > Products > Import (SKU dedupes reruns).")
