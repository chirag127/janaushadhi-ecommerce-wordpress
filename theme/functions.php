<?php
/**
 * Jan Aushadhi Child theme functions.
 *
 * Child of Astra. Enqueues styles, declares WooCommerce support,
 * and applies pharmacy-store tweaks. Keep this file dependency-free
 * (no external composer packages) so it is installable as-is.
 *
 * @package janaushadhi-child
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit; // No direct access.
}

/**
 * Enqueue parent + child styles (and Google Fonts used by the palette).
 */
function janaushadhi_enqueue_styles() {
	// Parent (Astra) stylesheet.
	wp_enqueue_style(
		'astra-parent-style',
		get_template_directory_uri() . '/style.css',
		array(),
		wp_get_theme( 'astra' )->get( 'Version' )
	);

	// Google Fonts: Poppins (headings) + Inter (body). Loaded with display=swap.
	wp_enqueue_style(
		'janaushadhi-fonts',
		'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@500;600;700&display=swap',
		array(),
		null
	);

	// Child theme stylesheet (design tokens + WooCommerce/pharmacy styles).
	wp_enqueue_style(
		'janaushadhi-child-style',
		get_stylesheet_uri(),
		array( 'astra-parent-style', 'janaushadhi-fonts' ),
		wp_get_theme()->get( 'Version' )
	);
}
add_action( 'wp_enqueue_scripts', 'janaushadhi_enqueue_styles', 15 );

/**
 * Theme supports.
 */
function janaushadhi_after_setup_theme() {
	// WooCommerce.
	add_theme_support( 'woocommerce' );
	// Product gallery UX.
	add_theme_support( 'wc-product-gallery-zoom' );
	add_theme_support( 'wc-product-gallery-lightbox' );
	add_theme_support( 'wc-product-gallery-slider' );

	// Editor niceties.
	add_theme_support( 'align-wide' );
	add_theme_support( 'responsive-embeds' );
}
add_action( 'after_setup_theme', 'janaushadhi_after_setup_theme' );

/**
 * Currency symbol safety net: ensure INR shows as the rupee sign.
 * (WooCommerce already does this once currency = INR; this is defensive.)
 */
function janaushadhi_inr_symbol( $currency_symbol, $currency ) {
	if ( 'INR' === $currency ) {
		$currency_symbol = '&#8377;'; // Rupee sign.
	}
	return $currency_symbol;
}
add_filter( 'woocommerce_currency_symbol', 'janaushadhi_inr_symbol', 10, 2 );

/**
 * Products per page on catalog (tuned for a large 2,400+ product catalog).
 */
function janaushadhi_products_per_page() {
	return 24;
}
add_filter( 'loop_shop_per_page', 'janaushadhi_products_per_page', 20 );

/**
 * Add a short "generic medicine" trust note under the Add-to-Cart on
 * single product pages. Purely presentational.
 */
function janaushadhi_single_product_trust_note() {
	echo '<p class="ja-trust-badge">&#10003; Genuine generic medicine &middot; Govt. of India PMBJP</p>';
}
add_action( 'woocommerce_single_product_summary', 'janaushadhi_single_product_trust_note', 25 );

/**
 * Enable WooCommerce product reviews / ratings globally (defensive default).
 */
function janaushadhi_enable_reviews() {
	if ( 'no' === get_option( 'woocommerce_enable_reviews' ) ) {
		update_option( 'woocommerce_enable_reviews', 'yes' );
	}
}
add_action( 'admin_init', 'janaushadhi_enable_reviews' );

/**
 * Register a simple footer helpline notice hook target for Elementor / widgets.
 * Shortcode: [ja_helpline]
 */
function janaushadhi_helpline_shortcode() {
	return '<span class="ja-helpline">Helpline: 1800-XXX-XXXX (9am-9pm)</span>';
}
add_shortcode( 'ja_helpline', 'janaushadhi_helpline_shortcode' );

/**
 * Header customization: announcement bar above the site header.
 * Pushes free-delivery offer + helpline. Dependency-free (Astra hook).
 */
function janaushadhi_announcement_bar() {
	echo '<div class="ja-announcement-bar"><div class="ja-container">'
		. '<span>&#128666; Free delivery on orders over &#8377;500</span>'
		. '<span>' . do_shortcode( '[ja_helpline]' ) . '</span>'
		. '</div></div>';
}
add_action( 'astra_header_before', 'janaushadhi_announcement_bar' );

/**
 * Header customization: mark Astra's main header sticky so search + cart
 * stay reachable on scroll. Adds the .ja-sticky-header class via filter.
 */
function janaushadhi_sticky_header_class( $classes ) {
	$classes[] = 'ja-sticky-header';
	return $classes;
}
add_filter( 'astra_site_header_class', 'janaushadhi_sticky_header_class' );

/**
 * Footer customization: trust / compliance strip above Astra's footer.
 * Shows PMBJP mission line, helpline, and payment/COD reassurance.
 */
function janaushadhi_footer_trust_strip() {
	echo '<div class="ja-footer-trust ja-section--alt"><div class="ja-container">'
		. '<p class="ja-trust-badge">&#10003; Genuine generic medicines &middot; Govt. of India PMBJP</p>'
		. '<p>Secure payments via Razorpay (UPI / cards / netbanking) &middot; Cash on Delivery available.</p>'
		. '<p>' . do_shortcode( '[ja_helpline]' ) . '</p>'
		. '</div></div>';
}
add_action( 'astra_footer_before', 'janaushadhi_footer_trust_strip' );

/**
 * Footer customization: replace Astra's default copyright with a
 * Jan Aushadhi credit line (kept text-only, no emoji in chrome).
 */
function janaushadhi_footer_copyright( $output ) {
	$year = gmdate( 'Y' );
	return '<span class="ja-copyright">&copy; ' . esc_html( $year )
		. ' Jan Aushadhi Generic Medicines. Under the Pradhan Mantri Bhartiya Janaushadhi Pariyojana.</span>';
}
add_filter( 'astra_footer_copyright', 'janaushadhi_footer_copyright' );

/**
 * Lightweight, dependency-free dark-mode toggle.
 * Adds a small button to the footer that flips data-theme on <html>
 * and remembers the choice in localStorage. CSS variables in style.css
 * handle the actual theming. Remove if using a dedicated plugin.
 */
function janaushadhi_dark_mode_toggle() {
	?>
	<script>
	(function () {
		try {
			var stored = localStorage.getItem('ja-theme');
			if (stored) { document.documentElement.setAttribute('data-theme', stored); }
		} catch (e) {}
		document.addEventListener('DOMContentLoaded', function () {
			var btn = document.createElement('button');
			btn.className = 'ja-theme-toggle';
			btn.type = 'button';
			btn.setAttribute('aria-label', 'Toggle dark mode');
			btn.textContent = 'Toggle theme';
			btn.style.position = 'fixed';
			btn.style.right = '16px';
			btn.style.bottom = '16px';
			btn.style.zIndex = '1000';
			btn.addEventListener('click', function () {
				var cur = document.documentElement.getAttribute('data-theme');
				var next = (cur === 'dark') ? 'light' : 'dark';
				document.documentElement.setAttribute('data-theme', next);
				try { localStorage.setItem('ja-theme', next); } catch (e) {}
			});
			document.body.appendChild(btn);
		});
	})();
	</script>
	<?php
}
add_action( 'wp_footer', 'janaushadhi_dark_mode_toggle' );
