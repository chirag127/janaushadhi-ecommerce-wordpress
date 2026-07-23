# Deploy the Jan Aushadhi store on InfinityFree (free, no card)

Plain step-by-step. InfinityFree gives free web hosting with **MySQL** (what
WooCommerce needs). No credit card. Ad-supported + throttled — fine for a
demo/portfolio store, not high traffic.

## 1. Sign up
- Go to **infinityfree.com** -> **Sign Up** (email + password, no card).

## 2. Create the site
- **Create Account** (InfinityFree calls a website an "account").
- Pick a free subdomain, e.g. `janaushdhi.rf.gd` or `janaushdhi.great-site.net`.
- Wait ~5 min for it to activate.

## 3. Open the Control Panel
- Click **Control Panel** for your new site.

## 4. Install WordPress (one click)
- In the panel: **Softaculous Apps Installer** -> **WordPress** -> **Install**.
- Set an admin **username + password** -> WRITE THEM DOWN (your WP login).
- It auto-creates the MySQL database. You never touch the DB directly.

## 5. Log in to WordPress
- Visit `your-site.rf.gd/wp-admin` -> log in with the admin from step 4.

## 6. Install plugins
WP Admin -> **Plugins -> Add New** -> install + activate:
- **WooCommerce** (store engine)
- **Elementor** (page builder)
- **Razorpay for WooCommerce** (payments)
- (optional) **Rank Math** (SEO)
See `docs/plugin-list.md` for the full list.

## 7. Apply the theme
- Zip the `theme/` folder in this repo -> WP Admin -> **Appearance -> Themes ->
  Add New -> Upload Theme** -> activate. (Install the Astra parent theme from the
  theme directory first.)

## 8. Import the 2,439 products (CHUNKED - important on free hosting)
InfinityFree times out on a 2,439-row import. So import in 5 small files:
- Run once locally: `python scripts/split-products-csv.py` -> creates
  `import/chunks/products-01.csv` ... `products-05.csv` (500 rows each).
- WP Admin -> **Products -> Import** -> upload `products-01.csv` -> run.
- Repeat for `-02` ... `-05`, in order. (WooCommerce dedupes by SKU, so re-running
  a chunk is safe.)

## 9. Configure WooCommerce + Razorpay
- WooCommerce -> Settings: currency **INR (Rs)**, region **India**
  (see `docs/woocommerce-settings.md`).
- Razorpay plugin: paste your **TEST** Key ID + Secret, enable **Test mode**.
- Place a test order to confirm.

## 10. Homepage in Elementor
- Build per `docs/homepage-layout.md`; set it as the static homepage.

## Later: custom domain
You own `oriz.in`. To use `janaushadhi.oriz.in`: in InfinityFree add the custom
domain, then add a CNAME in Cloudflare DNS pointing `janaushadhi` -> the
InfinityFree target. (SSL is free via their panel.)

## Known InfinityFree limits (expect these)
- No SSH / WP-CLI -> everything via the web UI.
- Daily hit limits -> throttles under real traffic (fine for demo).
- Big imports time out -> that's why step 8 is chunked.
- For real paying customers, a ~$3-5/mo shared host is more reliable (not free).
