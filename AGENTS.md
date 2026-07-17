# AGENTS.md — Jan Aushadhi WordPress / WooCommerce store

Config + theme + docs + product-import deliverable for the Jan Aushadhi
generic-medicines storefront. **Not a code app** — a WordPress site is stood up
by installing WP + plugins and applying the config documented here. No build
step, no WP/wp-cli in this repo's toolchain.

## What this repo is

- **Catalog:** 2,439 generic medicines, 62 categories under one `Medicines`
  parent. Currency **INR**, region **India**. Prices = MRP.
- **Payments:** Razorpay (India) + Cash on Delivery. COD works with no keys.
- **Stack:** WordPress + WooCommerce + Elementor, **Astra** parent theme +
  this child theme.
- **License:** MIT (repo). The child theme's `style.css` header declares GPL —
  required for WordPress.org theme compliance; unrelated to repo license.

## Layout

```
.
├── LICENSE                         MIT
├── README.md                       structure + full setup runbook
├── .env.example                    placeholder Razorpay keys (names only)
├── docs/
│   ├── plugin-list.md              required + recommended plugins
│   ├── theme-config.md             base theme, palette, typography, dark mode
│   ├── homepage-layout.md          Elementor section-by-section build spec
│   ├── woocommerce-settings.md     store config runbook (general/tax/ship/pay)
│   ├── razorpay-integration.md     end-to-end Razorpay + COD setup
│   ├── seo.md                      Rank Math + schema config
│   └── performance.md              caching / CDN / image optimization
├── theme/                          Astra child theme (installable as-is)
│   ├── style.css                   theme header + design tokens + WC styles
│   ├── functions.php               enqueue, WC support, header/footer, dark mode
│   └── woocommerce/product-searchform.php   WC template override
└── import/
    ├── build_products_csv.py       meds.csv -> products.csv generator
    ├── products.csv                2,439 rows, WooCommerce import format
    └── README.md                   import steps + column/category mapping
```

## Toolchain / how to validate

- **No WP, no wp-cli.** Validate config + CSV only; review theme PHP by
  inspection.
- **Python IS available** for CSV validation. Regenerate CSV:
  `python import/build_products_csv.py` (reads sibling astro repo's `meds.csv`).
- **Validate CSV:** parse with Python `csv` module — expect 16 columns,
  2,439 data rows, unique SKUs, all prices numeric.

## Rules for agents

- **Secrets:** never commit keys. `.env.example` holds placeholders only
  (`rzp_test_xxx`); real keys go in WP admin plugin settings. `.env` is
  gitignored.
- **COD must work without keys** — keep Cash on Delivery documented + enabled.
- **No auth wall on storefront browsing** — the catalog is public.
- **Community/free plugins only** — see `docs/plugin-list.md` (free tiers cover
  every documented feature).
- **Theme edits:** child theme only, never edit Astra. Keep `functions.php`
  dependency-free (no composer packages) so it installs as-is.
- **Terse conventional commits**; push to `main` when done.

## Standing up the store (human, manual)

1. Install WordPress; install + activate **Astra**, then this child theme
   (`docs/theme-config.md`).
2. Install plugins (`docs/plugin-list.md`), run the WooCommerce wizard
   (India / INR).
3. Apply `docs/woocommerce-settings.md` (tax/shipping/payments/checkout).
4. Import `import/products.csv` (`import/README.md`).
5. Configure Razorpay + COD (`docs/razorpay-integration.md`).
6. Build homepage/About/Contact/FAQ in Elementor (`docs/homepage-layout.md`).
7. SEO + performance (`docs/seo.md`, `docs/performance.md`), test order, launch.
