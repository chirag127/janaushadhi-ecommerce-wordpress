# Jan Aushadhi Generic Medicines - WordPress / WooCommerce Store

A production-ready **WordPress + WooCommerce + Elementor** ecommerce site for
selling generic medicines under the Pradhan Mantri Bhartiya Janaushadhi
Pariyojana (PMBJP) programme. This repository is a **configuration, theme, and
documentation deliverable** plus a **generated product-import CSV** - WordPress
sites are stood up by installing WordPress and plugins and applying the config
documented here, not by compiling application code.

- **Catalog:** 2,439 generic medicines across **62 categories** under a single
  `Medicines` parent category.
- **Currency:** Indian Rupee (INR, Rs).
- **Payments:** Razorpay (India) + Cash on Delivery fallback.
- **Region:** India.

---

## Repository structure

```
janaushadhi-ecommerce-wordpress/
├── README.md                     <- this file (structure + full setup runbook)
├── docs/
│   ├── plugin-list.md            <- required + recommended plugins
│   ├── theme-config.md           <- base theme, child theme, palette, typography, dark mode
│   ├── woocommerce-settings.md   <- store settings (INR, tax, shipping, Razorpay, checkout, accounts)
│   ├── homepage-layout.md        <- Elementor homepage spec + About/Contact/FAQ notes
│   ├── seo.md                    <- Rank Math config, sitemap, schema
│   └── performance.md            <- Cloudflare CDN, caching, image optimization
├── theme/                        <- installable Astra child theme
│   ├── style.css                 <- header + design tokens + WooCommerce/pharmacy styles + dark mode
│   ├── functions.php             <- enqueue, WooCommerce support, tweaks, dark-mode toggle
│   ├── woocommerce/
│   │   └── product-searchform.php  <- WooCommerce template override (branded search)
│   └── README.md                 <- theme install notes
└── import/
    ├── build_products_csv.py     <- generates products.csv from the source meds.csv
    ├── products.csv              <- 2,439 WooCommerce-importable products
    └── README.md                 <- import steps + category mapping
```

---

## Site page structure

- **Home** - Elementor-built landing page (see `docs/homepage-layout.md`).
- **Shop** - WooCommerce shop archive (all products).
- **Product categories** - 62 category archives under `Medicines`.
- **Single product** - price, pack size, add-to-cart, wishlist, native reviews/ratings.
- **Cart / Checkout** - WooCommerce (Razorpay + COD).
- **My Account** - login/register, orders, order tracking, addresses, downloads.
- **About Us / Contact / FAQ** - Elementor pages (outlines in `docs/homepage-layout.md`).
- **Wishlist** - via wishlist plugin.
- **Legal** - Privacy Policy, Terms & Conditions, Refund/Return policy.

---

## Setup runbook (install order)

> Do this on a host with **PHP 8.1+**, **MySQL/MariaDB**, HTTPS, and (ideally)
> a LiteSpeed server or managed WordPress host. See `docs/performance.md`.

### 1. Install WordPress
1. Create a database + DB user on your host.
2. Install WordPress (one-click on most hosts, or upload core + run the installer).
3. Complete the famous 5-minute install; set the admin user, site title
   "Jan Aushadhi", and a strong password.
4. **Settings > General:** set Site URL/Home URL (HTTPS), timezone (Kolkata),
   date format.
5. **Settings > Permalinks:** choose **Post name** (SEO-friendly).

### 2. Install the base theme + child theme
1. **Appearance > Themes > Add New** > install & activate **Astra**.
2. Install the child theme from `theme/` (zip it as `janaushadhi-child.zip` with
   `style.css` at the zip root, or copy to `wp-content/themes/janaushadhi-child/`).
3. **Appearance > Themes** > activate **Jan Aushadhi Child**.
   (Full notes: `theme/README.md` and `docs/theme-config.md`.)

### 3. Install plugins
Install in this order (details + free/paid in `docs/plugin-list.md`):
1. **WooCommerce** (run its setup wizard: country India, currency INR).
2. **Elementor** (+ Elementor Pro if licensed).
3. **Rank Math SEO** (run setup wizard - `docs/seo.md`).
4. **Razorpay for WooCommerce** (payment gateway).
5. **TI WooCommerce Wishlist** (wishlist).
6. **WooCommerce PDF Invoices & Packing Slips** (invoices).
7. Caching: **LiteSpeed Cache** (LiteSpeed hosts) or **W3 Total Cache**.
8. **ShortPixel** or **Smush** (image optimization).
9. **Cloudflare** (CDN - `docs/performance.md`).
10. Recommended: **Wordfence** (security), **UpdraftPlus** (backups),
    **Contact Form 7 / WPForms** (contact page), a consent/cookie plugin.

### 4. Configure WooCommerce
Follow `docs/woocommerce-settings.md`: currency INR, India store address,
shipping zones, GST tax classes, checkout/account pages, order statuses,
and emails.

### 5. Import the product catalog
1. Ensure `import/products.csv` exists (regenerate with
   `python import/build_products_csv.py` if needed - Python 3.14).
2. **Products > All Products > Import** > upload `import/products.csv` >
   verify column mapping > **Run the importer**.
3. Confirm the `Medicines` parent + 62 subcategories and 2,439 products.
   Full steps + category mapping: `import/README.md`.

### 6. Build the homepage + content pages
Use Elementor to build Home, About, Contact, FAQ per `docs/homepage-layout.md`.
Set the homepage under **Settings > Reading > A static page**.

### 7. Configure Razorpay (payments)
1. Create/verify a Razorpay merchant account (KYC) at razorpay.com.
2. In the Razorpay Dashboard, generate **Key ID** and **Key Secret**
   (Test mode first, then Live).
3. **WooCommerce > Settings > Payments > Razorpay** > enable > paste
   **Key ID** and **Key Secret** > save.
4. Set the **webhook URL** shown by the plugin in the Razorpay Dashboard
   (Settings > Webhooks) and enable payment events.
5. Test a Test-mode order end to end, then switch to **Live** keys.
6. Enable **Cash on Delivery** as a fallback in the same Payments screen.

> **Never commit API keys/secrets to git.** All keys are entered in WP admin only.

### 8. SEO + performance + go-live
- Apply `docs/seo.md` (Rank Math, sitemap to Google Search Console, schema).
- Apply `docs/performance.md` (Cloudflare, caching, image optimization).
- Run a test order, verify emails/invoice, check mobile, then launch.

---

## Regenerating the product CSV

```bash
cd C:/g/janaushadhi-ecommerce-wordpress/import
python build_products_csv.py
```

Reads `C:\g\janaushadhi-ecommerce-astro\meds.csv` and writes `products.csv`
(2,439 products, 62 normalized categories). See `import/README.md`.

---

## Notes
- WooCommerce uses its own WordPress MySQL database (standard WP). It does **not**
  connect to any shared Postgres/InsForge backend; catalog parity is achieved via
  the generated `import/products.csv`.
- Product images are not in the source data; add a placeholder and/or image URLs
  later (see `import/README.md`).
- Verify current **GST** rates for medicines with a tax professional before launch.
