# Product Import (WooCommerce)

This folder produces a WooCommerce-importable catalog derived from the
Jan Aushadhi source list.

## Files
- `build_products_csv.py` - reads the source `meds.csv` and emits `products.csv`.
- `products.csv` - **2,439** products ready for the WooCommerce Product CSV Importer.

## Source
`C:\g\janaushadhi-ecommerce-astro\meds.csv`
Columns: `Sr No, Drug Code, Generic Name, Unit Size, MRP, Group Name`
(2,439 data rows; every `Drug Code` is unique.)

## Output columns (WooCommerce standard)
| CSV column | Source / value |
|---|---|
| `Type` | `simple` |
| `SKU` | Drug Code |
| `Name` | Generic Name |
| `Published` | `1` |
| `Is featured?` | `0` |
| `Visibility in catalog` | `visible` |
| `Short description` | `Generic medicine. Pack size: <Unit Size>.` |
| `Description` | Full PMBJP description incl. pack size, category, drug code |
| `In stock?` | `1` |
| `Stock` | blank (in-stock flag only, qty not managed) |
| `Backorders allowed?` | `0` |
| `Sold individually?` | `0` |
| `Regular price` | MRP (2-decimal, INR) |
| `Categories` | `Medicines > <Normalized Group Name>` |
| `Tax status` | `taxable` |
| `Tax class` | blank (standard) |

## Category mapping / normalization
The source `Group Name` contained case-variant and near-duplicate
categories. `build_products_csv.py` folds them into a single canonical set:

- `Anti-fungal` + `Anti-Fungal` -> **Anti-Fungal**
- `STOMATOLOGICALS` + `Stomatologicals` -> **Stomatologicals**
- `Hepato-protective` + `Hepato-Protective` (+ trailing-space variant) -> **Hepato-Protective**
- `Anti-retroviral` + `Anti-Retroviral` -> **Anti-Retroviral**
- `Anti-viral` + `Anti-Viral` -> **Anti-Viral**
- `Opthalmic/Otic` -> **Ophthalmic/Otic** (spelling fix)
- plus tidy casing for the rest (e.g. `Weight management` -> `Weight Management`).

Result: **62 canonical categories** (down from 68 raw variants), all imported
as children of a single top-level **Medicines** category. WooCommerce creates
the parent and children automatically from the `Parent > Child` syntax.

## Regenerate the CSV
```bash
cd C:/g/janaushadhi-ecommerce-wordpress/import
python build_products_csv.py
# optional custom paths:
python build_products_csv.py --src /path/meds.csv --out /path/products.csv
```

## Import into WooCommerce (exact steps)
1. WordPress admin > **Products > All Products > Import** (top of page).
2. Click **Choose File**, select `import/products.csv`, click **Continue**.
3. On "Column mapping": the importer auto-maps standard headers. Verify
   `SKU`, `Name`, `Regular price`, `Categories`, `Short description`,
   `Description`, `In stock?`, `Published` are mapped correctly.
4. Leave **"Update existing products"** unchecked for a first import
   (check it on re-imports so matching SKUs update instead of duplicating).
5. Click **Run the importer**. For 2,439 rows this takes a few minutes.
6. When done, go to **Products > Categories** to confirm the `Medicines`
   parent and its 62 subcategories exist, then check **Products** for the
   full catalog.

### Tips
- Increase PHP `max_execution_time` / `memory_limit` if the import stalls
  (or split the CSV). Most hosts handle 2.4k rows fine.
- Product images are not in the source data. Add a global placeholder in
  **WooCommerce > Settings > Products**, and/or add an `Images` column with
  image URLs to the CSV later (the importer downloads them).
- Prices are entered as MRP. Configure tax display in
  **WooCommerce > Settings > Tax** (see `docs/woocommerce-settings.md`).
