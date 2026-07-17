#!/usr/bin/env python3
"""
build_products_csv.py

Reads the Jan Aushadhi source catalog (meds.csv) and emits a
WooCommerce Product CSV Importer-compatible file (products.csv).

Source columns : Sr No, Drug Code, Generic Name, Unit Size, MRP, Group Name
Output columns : WooCommerce standard import headers.

Category normalization: the source Group Name field contains case-variant
and near-duplicate categories (e.g. "Anti-fungal" vs "Anti-Fungal",
"STOMATOLOGICALS" vs "Stomatologicals"). These are folded into a single
canonical set so the WooCommerce store has clean, deduplicated categories.

Usage:
    python build_products_csv.py
    python build_products_csv.py --src /path/to/meds.csv --out /path/to/products.csv

Python 3.14+
"""
from __future__ import annotations

import argparse
import csv
import os
import sys
from collections import Counter

# ---------------------------------------------------------------------------
# Paths (defaults resolve relative to this script so it runs from anywhere)
# ---------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SRC = os.path.abspath(
    os.path.join(HERE, "..", "..", "janaushadhi-ecommerce-astro", "meds.csv")
)
DEFAULT_OUT = os.path.join(HERE, "products.csv")

# ---------------------------------------------------------------------------
# Category normalization map.
#
# Keys are the *raw* Group Name values (compared case-insensitively after
# stripping). Values are the canonical category name used in WooCommerce.
# Anything not in the map keeps its original (stripped) value.
# ---------------------------------------------------------------------------
CANONICAL_CATEGORIES = {
    "anti-fungal": "Anti-Fungal",
    "stomatologicals": "Stomatologicals",
    "hepato-protective": "Hepato-Protective",
    "anti-retroviral": "Anti-Retroviral",
    "anti-viral": "Anti-Viral",
    # explicit passthroughs kept for clarity / stable casing
    "surgical & medical consumables": "Surgical & Medical Consumables",
    "cardiovascular system (cvs)": "Cardiovascular System (CVS)",
    "central nervous system (cns)": "Central Nervous System (CNS)",
    "antibiotics": "Antibiotics",
    "anti-diabetic": "Anti-Diabetic",
    "gastrointestinal (git)": "Gastrointestinal (GIT)",
    "respiratory": "Respiratory",
    "analgesic/antipyretic/anti-inflammatory": "Analgesic/Antipyretic/Anti-Inflammatory",
    "supplement/vitamin/mineral": "Supplement/Vitamin/Mineral",
    "oncology": "Oncology",
    "dermatology/topical/external": "Dermatology/Topical/External",
    "opthalmic/otic": "Ophthalmic/Otic",
    "urology": "Urology",
    "nutraceuticals": "Nutraceuticals",
    "gynaecology": "Gynaecology",
    "ortho": "Ortho",
    "anti-histaminic": "Anti-Histaminic",
    "derma care": "Derma Care",
    "steroids & hormones": "Steroids & Hormones",
    "antiseptic/disinfectants": "Antiseptic/Disinfectants",
    "diuretic": "Diuretic",
    "electrolytes": "Electrolytes",
    "anti-malarial": "Anti-Malarial",
    "immunosuppressant": "Immunosuppressant",
    "anti-thyroid": "Anti-Thyroid",
    "enzyme preparation": "Enzyme Preparation",
    "anthelmintic": "Anthelmintic",
    "anti-emetic": "Anti-Emetic",
    "anticoagulant": "Anticoagulant",
    "anaesthetics": "Anaesthetics",
    "coagulants": "Coagulants",
    "iron-chelating agents": "Iron-Chelating Agents",
    "nephrology": "Nephrology",
    "ayurvedic": "Ayurvedic",
    "burn relief": "Burn Relief",
    "vaccines": "Vaccines",
    "anti-alcoholism": "Anti-Alcoholism",
    "smoking cessation": "Smoking Cessation",
    "treatment of gout": "Treatment of Gout",
    "irrigation fluid": "Irrigation Fluid",
    "erythropoiesis": "Erythropoiesis",
    "weight management": "Weight Management",
    "covid-19": "Covid-19",
    "treatment of severe aplastic anemia": "Treatment of Severe Aplastic Anemia",
    "anti-rabies": "Anti-Rabies",
    "altitude sickness": "Altitude Sickness",
    "anti-t.b": "Anti-T.B",
    "mosquito repellent": "Mosquito Repellent",
    "polycystic ovary/ovarian syndrome": "Polycystic Ovary Syndrome",
    "hemorrhoids & anal fissures": "Hemorrhoids & Anal Fissures",
    "footcare cream": "Footcare Cream",
    "antidote": "Antidote",
    "mouth ulcer gel": "Mouth Ulcer Gel",
    "throat spray for freshness": "Throat Spray for Freshness",
    "anti-diuretic": "Anti-Diuretic",
    "immunostimulator": "Immunostimulator",
    "anti-migraine": "Anti-Migraine",
    "hepato-protective ": "Hepato-Protective",
}

# Parent category all products roll up under, for a clean store tree.
PARENT_CATEGORY = "Medicines"

# WooCommerce Product CSV Importer standard headers.
WC_HEADERS = [
    "Type",
    "SKU",
    "Name",
    "Published",
    "Is featured?",
    "Visibility in catalog",
    "Short description",
    "Description",
    "In stock?",
    "Stock",
    "Backorders allowed?",
    "Sold individually?",
    "Regular price",
    "Categories",
    "Tax status",
    "Tax class",
]


def canonical_category(raw: str) -> str:
    """Fold a raw Group Name into its canonical WooCommerce category."""
    key = raw.strip().lower()
    return CANONICAL_CATEGORIES.get(key, raw.strip())


def clean_price(raw: str) -> str:
    """Normalize an MRP value to a plain decimal string; '' if unparseable."""
    if raw is None:
        return ""
    v = raw.strip().replace(",", "")
    if not v:
        return ""
    try:
        return f"{float(v):.2f}"
    except ValueError:
        return ""


def build(src: str, out: str) -> tuple[int, Counter]:
    """Read src meds.csv, write WooCommerce products.csv, return (rows, cat_counts)."""
    if not os.path.exists(src):
        sys.exit(f"ERROR: source not found: {src}")

    cat_counts: Counter = Counter()
    seen_skus: set[str] = set()
    rows_written = 0

    with open(src, encoding="utf-8-sig", newline="") as fh_in, open(
        out, "w", encoding="utf-8", newline=""
    ) as fh_out:
        reader = csv.DictReader(fh_in)
        writer = csv.DictWriter(fh_out, fieldnames=WC_HEADERS)
        writer.writeheader()

        for row in reader:
            name = (row.get("Generic Name") or "").strip()
            drug_code = (row.get("Drug Code") or "").strip()
            unit_size = (row.get("Unit Size") or "").strip()
            price = clean_price(row.get("MRP", ""))
            group = (row.get("Group Name") or "").strip()

            if not name or not drug_code:
                continue  # skip malformed rows

            # De-duplicate SKUs (Drug Code) — WooCommerce requires unique SKUs.
            sku = drug_code
            if sku in seen_skus:
                continue
            seen_skus.add(sku)

            cat = canonical_category(group) if group else "Uncategorized"
            cat_counts[cat] += 1

            # WooCommerce hierarchical category syntax: "Parent > Child"
            category_path = f"{PARENT_CATEGORY} > {cat}"

            short_desc = (
                f"Generic medicine. Pack size: {unit_size}."
                if unit_size
                else "Generic medicine."
            )
            long_desc = (
                f"{name} supplied under the Pradhan Mantri Bhartiya Janaushadhi "
                f"Pariyojana (PMBJP) generic-medicines programme. "
                f"Pack size: {unit_size}. Category: {cat}. "
                f"Drug Code: {drug_code}."
            )

            writer.writerow(
                {
                    "Type": "simple",
                    "SKU": sku,
                    "Name": name,
                    "Published": 1,
                    "Is featured?": 0,
                    "Visibility in catalog": "visible",
                    "Short description": short_desc,
                    "Description": long_desc,
                    "In stock?": 1,
                    "Stock": "",  # blank = don't manage stock qty, just in-stock flag
                    "Backorders allowed?": 0,
                    "Sold individually?": 0,
                    "Regular price": price,
                    "Categories": category_path,
                    "Tax status": "taxable",
                    "Tax class": "",  # standard rate
                }
            )
            rows_written += 1

    return rows_written, cat_counts


def main() -> None:
    ap = argparse.ArgumentParser(description="Build WooCommerce products.csv from meds.csv")
    ap.add_argument("--src", default=DEFAULT_SRC, help="path to source meds.csv")
    ap.add_argument("--out", default=DEFAULT_OUT, help="path to output products.csv")
    args = ap.parse_args()

    rows, cats = build(args.src, args.out)

    print(f"Source : {args.src}")
    print(f"Output : {args.out}")
    print(f"Products written : {rows}")
    print(f"Canonical categories : {len(cats)}")
    print("-" * 60)
    for name, count in cats.most_common():
        print(f"{count:5d}  {name}")


if __name__ == "__main__":
    main()
