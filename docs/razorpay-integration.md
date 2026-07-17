# Razorpay Integration (WooCommerce)

End-to-end payment setup for the Jan Aushadhi store. India-first: **Razorpay**
for online payments (UPI / cards / netbanking / wallets) with **Cash on
Delivery (COD)** as a no-key fallback. Keys are **never committed** — enter them
in WP admin, and use `.env.example` only as a placeholder reference.

## Plugin

- **Razorpay for WooCommerce** — official free plugin (`razorpay/woo-razorpay`).
- Install: WP admin > Plugins > Add New > search **"Razorpay for WooCommerce"**
  > Install > Activate. Or upload the zip from
  <https://wordpress.org/plugins/woo-razorpay/>.

## Placeholder keys (`.env.example`)

`.env.example` documents the key **names** only — WordPress reads keys from the
plugin settings in the DB, not from env. Placeholders (test mode):

```
RAZORPAY_KEY_ID=rzp_test_xxxxxxxxxxxxxx
RAZORPAY_KEY_SECRET=xxxxxxxxxxxxxxxxxxxxxxxx
RAZORPAY_WEBHOOK_SECRET=xxxxxxxxxxxxxxxxxxxxxxxx
```

Replace `rzp_test_*` with **live** keys (`rzp_live_*`) only after test-mode
passes. Copy `.env.example` to `.env` locally; `.env` is gitignored.

## Setup (test mode first)

1. Sign in to the **Razorpay Dashboard** (<https://dashboard.razorpay.com/>).
2. **Settings > API Keys > Generate Test Key** — copy **Key ID** and
   **Key Secret** (secret shown once; store it in your password manager).
3. WooCommerce > Settings > **Payments** > **Razorpay** > **Manage**:
   - **Enable** the gateway.
   - Paste **Key ID** and **Key Secret**.
   - **Payment Action:** Authorize and Capture.
   - Title: "Pay online (UPI / Cards / Netbanking)".
4. **Webhook:** the plugin shows a **Webhook URL**
   (`https://<your-site>/?wc-api=razorpay`). In Razorpay Dashboard >
   **Settings > Webhooks > Add New Webhook**:
   - URL = that webhook URL.
   - Secret = a strong value; paste the **same** value into the plugin's
     **Webhook Secret** field (and `RAZORPAY_WEBHOOK_SECRET` in `.env`).
   - Active events: `payment.authorized`, `payment.captured`,
     `payment.failed`, `refund.created`, `order.paid`.
5. **Save.**

## End-to-end test

1. Add a product to cart > Checkout > select **Razorpay**.
2. Use Razorpay **test instruments**:
   - UPI: `success@razorpay`
   - Card: `4111 1111 1111 1111`, any future expiry, any CVV, OTP `1234`.
3. Complete payment. Order should move **Pending payment > Processing**.
4. Confirm the **webhook** fired (Dashboard > Webhooks > delivery log) and the
   order note records the Razorpay payment ID.
5. Test a **refund** from WooCommerce > Orders (issues via Razorpay API).

## Go live

1. Complete Razorpay **KYC / account activation** (business docs, bank
   account, settlement details).
2. Generate **Live** keys; swap them into the plugin (and `.env`), switch off
   test mode.
3. Re-point the webhook to the live URL (usually same URL, live secret).
4. Place one small **live** order end to end, verify settlement, then launch.

## Cash on Delivery (works WITHOUT any keys)

COD needs **no** Razorpay keys and must always be available:

1. WooCommerce > Settings > **Payments** > **Cash on delivery** > **Enable**.
2. Instructions: "Pay in cash to the delivery agent on receipt."
3. Optional: restrict COD to specific **shipping methods** or set a max order
   value (Settings > Payments > Cash on delivery > Manage).
4. Test: checkout selecting COD; order should land in **Processing** with no
   online payment step.

> COD keeps the store transacting even before Razorpay KYC is approved. Keep it
> enabled as a permanent fallback.

## Notes

- Currency must be **INR** (WooCommerce > Settings > General) — Razorpay India
  settles in INR only.
- Never place API keys in theme code, git, or client-side JS. The plugin stores
  them server-side; `.env.example` is documentation only.
- See `docs/woocommerce-settings.md` for the broader payments/checkout config.
