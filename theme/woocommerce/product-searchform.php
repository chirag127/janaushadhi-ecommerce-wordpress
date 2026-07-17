<?php
/**
 * The product search form (WooCommerce template override).
 *
 * Override of woocommerce/templates/product-searchform.php.
 * Adds pharmacy-branded classes so the .ja-search-form styles apply.
 * Placing this file at theme/woocommerce/product-searchform.php makes
 * WooCommerce use it instead of its default.
 *
 * @package janaushadhi-child
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?>
<form role="search" method="get" class="woocommerce-product-search ja-search-form" action="<?php echo esc_url( home_url( '/' ) ); ?>">
	<label class="screen-reader-text" for="woocommerce-product-search-field-<?php echo esc_attr( $index ); ?>"><?php esc_html_e( 'Search for medicines:', 'janaushadhi-child' ); ?></label>
	<input
		type="search"
		id="woocommerce-product-search-field-<?php echo esc_attr( $index ); ?>"
		class="search-field"
		placeholder="<?php echo esc_attr__( 'Search medicines by name...', 'janaushadhi-child' ); ?>"
		value="<?php echo get_search_query(); ?>"
		name="s"
	/>
	<button type="submit" class="ja-btn" value="<?php echo esc_attr_x( 'Search', 'submit button', 'janaushadhi-child' ); ?>">
		<?php echo esc_html_x( 'Search', 'submit button', 'janaushadhi-child' ); ?>
	</button>
	<input type="hidden" name="post_type" value="product" />
</form>
