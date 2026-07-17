# WooCommerce Settings

Store configuration runbook for the Jan Aushadhi generic-medicines store.
Currency **INR (Rs)**, region **India**, payments **Razorpay + COD**.
All admin paths are **WooCommerce > Settings > ...**. Never commit API keys.

## General (WooCommerce > Settings > General)
- **Store address:** the Jan Aushadhi Kendra address; Country/State = India.
- **Selling location(s):** "Sell to specific countries" -> **India** (or all, if
  shipping wider later).
- **Shipping location(s):** ship to your selling countries.
- **Default customer location:** Shop base / geolocate.
- **Enable taxes:** checked (see Tax section).
- **Enable coupons:** checked (see Coupons).
- **Currency:** Indian Rupee (Rs) - `INR`.
- **Currency position:** Left (`Rs 10.32`).
- **Thousand separator:** `,`  **Decimal separator:** `.`  **Decimals:** `2`
  (Indian formatting; for grouping like 1,00,000 use a locale/format plugin if
  required).

## Products (WooCommerce > Settings > Products)
- **Shop page:** set to the "Shop" page.
- **Measurements:** weight `g`/`kg`, dimensions `cm` (medicine packs).
- **Reviews:** enable **product reviews** and **star ratings**; check
  **"Reviews can only be left by verified owners"** and show the "verified
  owner" label. (This uses WooCommerce **native** reviews - no plugin.)
- **Placeholder image:** upload a neutral pill/medicine placeholder (source data
  has no images).
- **Add-to-cart behavior:** redirect to cart optional; enable AJAX add-to-cart
  on archives.

## Categories (Products > Categories)
- The import creates a single parent **Medicines** with **62 subcategories**
  (normalized `Group Name`, e.g. Cardiovascular System (CVS), Anti-Diabetic,
  Antibiotics, CNS, Respiratory ...).
- Categories are created automatically by the importer from the
  `Medicines > <Category>` syntax in `import/products.csv`.
- After import, optionally add category images/descriptions and set display
  order. See `import/README.md` for the full mapping.

## Inventory (WooCommerce > Settings > Products > Inventory)
- Imported products are **In stock = 1** with **stock quantity not managed**
  (simple in-stock flag). Leave "Manage stock" off globally unless you want
  per-SKU quantities.
- Optional: enable low-stock/out-of-stock notification emails if you later
  manage quantities.

## Shipping (WooCommerce > Settings > Shipping)
- Create a shipping **zone "India"** covering the country.
- Methods in the India zone:
  - **Flat rate** (e.g. Rs 40) for standard orders.
  - **Free shipping** with a minimum order (e.g. free over **Rs 500**).
  - **Local pickup** at the Jan Aushadhi Kendra (Rs 0).
- Optional: a "Rest of World" zone if you expand later.
- Set package handling/weight defaults if using weight-based rates.

## Tax (WooCommerce > Settings > Tax)
> **Verify current GST rates with a tax professional before launch.** Many PMBJP
> generic medicines are nil/exempt or attract **5% GST**; some items differ.
- **Prices entered with tax:** recommend **exclusive of tax** (enter MRP as net,
  show tax at checkout) - or inclusive if your MRP already includes GST; be
  consistent with how the catalog MRP is defined.
- **Display prices in shop / at cart:** choose incl. or excl. tax consistently.
- **Tax classes:**
  - **Standard** - default.
  - Add a **"Medicines 5% GST"** reduced class and assign medicine products to it.
  - Add a **"Zero rate / Exempt"** class for nil-rated items.
- **Tax rates:** add India rate rows per class (Country IN, rate %, name "GST").
- **Rounding:** round at subtotal level.

## Payments (WooCommerce > Settings > Payments)
> Full end-to-end steps (test keys, webhook, refunds, go-live) live in
> `docs/razorpay-integration.md`. Placeholder keys: `.env.example`.
### Razorpay (primary, India)
1. Install **Razorpay for WooCommerce**.
2. In the **Razorpay Dashboard**, generate **Key ID** and **Key Secret**
   (start in **Test mode**).
3. WooCommerce > Settings > Payments > **Razorpay** > **Enable** > paste
   `<YOUR_RAZORPAY_KEY_ID>` and `<YOUR_RAZORPAY_KEY_SECRET>` > Save.
4. Set the **Webhook URL** the plugin displays into the Razorpay Dashboard
   (Settings > Webhooks) and enable payment/refund events; add the webhook
   secret if prompted.
5. Place a **Test-mode** order end to end (use Razorpay test cards/UPI).
6. Switch to **Live** keys and repeat one small live test, then go live.
> Keys are entered in WP admin only and **never committed to git**.

### Cash on Delivery (fallback)
- Enable **Cash on delivery**; optionally restrict to specific shipping methods
  or a max order value.

## Checkout
- Allow **guest checkout**; also allow account creation during checkout.
- Set a **Terms & Conditions** page and require acceptance.
- Keep required address fields minimal but valid for India (PIN code, state).
- Enable order notes.

## Accounts & Privacy (WooCommerce > Settings > Accounts & Privacy)
- Enable **customer registration** on the My Account page and (optionally) at
  checkout.
- Set **My Account** page; users get Orders, Addresses, Account details,
  Downloads.
- Configure account erasure/retention and link the **Privacy Policy** page.

## Order statuses & tracking
- Standard statuses: **Pending payment > Processing > Completed**, plus
  **On hold**, **Cancelled**, **Refunded**, **Failed**.
- **Order tracking for customers:** native - customers view status and history
  under **My Account > Orders** (each order has a "view" page). Order-status
  emails notify them on each change. Add a shipment-tracking plugin later if you
  need carrier tracking numbers.

## Emails (WooCommerce > Settings > Emails)
- Enable/customize: New order (admin), Processing order, Completed order,
  Customer invoice, Refunded, New account.
- Set sender name "Jan Aushadhi" and a valid from-address; consider an SMTP
  plugin for deliverability.
- **PDF invoice:** the **WooCommerce PDF Invoices & Packing Slips** plugin
  auto-attaches the invoice to the Completed/Processing email.

## Coupons (Marketing > Coupons)
- Enabled in General. Create percentage / fixed-cart / fixed-product coupons
  with usage limits, expiry, and category restrictions (e.g. a launch discount,
  or category-specific offers).
