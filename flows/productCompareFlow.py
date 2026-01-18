from pages.productComparePage import ProductComparePage
from utilities.customLogger import LoggerFactory


class ProductCompareFlow:
    logger = LoggerFactory.get_logger(__name__)

    def __init__(self, driver):
        self.driver = driver
        self.compare_page = ProductComparePage(driver)

    def wait_for_compare_page_to_load(self):
        self.logger.info("Waiting for Product Compare page to load")
        self.compare_page.handle_cloudflare_if_present()
        if not self.compare_page.is_page_loaded():
            self.logger.error("Product Compare page failed to load")
            raise Exception("Product Compare page failed to load")
        self.logger.info("Product Compare page loaded successfully")

    def add_product_to_comparison(self, product_index):
        self.logger.info(f"Adding product at index {product_index} to comparison")
        self.compare_page.add_product_to_comparison(product_index)
        self.logger.info(f"Product {product_index} add operation completed")

    def add_multiple_products_to_comparison(self, product_indices):
        self.logger.info(f"Adding multiple products to comparison: {product_indices}")
        for index in product_indices:
            self.add_product_to_comparison(index)
        self.logger.info(f"Added {len(product_indices)} products to comparison")

    def remove_product_from_comparison(self, product_index):
        self.logger.info(f"Removing product at index {product_index} from comparison")
        self.compare_page.remove_product_from_comparison(product_index)
        self.logger.info(f"Product {product_index} remove operation completed")

    def clear_all_products_from_comparison(self):
        self.logger.info("Clearing all products from comparison")
        self.compare_page.clear_all_comparisons()
        self.logger.info("All products cleared from comparison")

    def navigate_to_comparison_page(self):
        self.logger.info("Navigating to product comparison page")
        self.wait_for_compare_page_to_load()
        self.compare_page.navigate_to_compare_page()
        self.logger.info("Navigation to comparison page initiated")

    def get_product_count_in_comparison(self):
        self.logger.info("Getting count of products in comparison")
        count = self.compare_page.get_number_of_products_in_comparison()
        self.logger.info(f"Products in comparison: {count}")
        return count

    def verify_products_in_comparison(self, expected_count):
        self.logger.info(f"Verifying {expected_count} products in comparison")
        actual_count = self.get_product_count_in_comparison()
        is_verified = actual_count == expected_count
        if is_verified:
            self.logger.info(f"Product count verification successful: {actual_count} == {expected_count}")
        else:
            self.logger.warning(f"Product count mismatch: {actual_count} != {expected_count}")
        return is_verified

    def get_all_products_in_comparison(self):
        self.logger.info("Retrieving all products in comparison")
        products = self.compare_page.get_all_product_names_in_comparison()
        self.logger.info(f"Retrieved {len(products)} products from comparison")
        return products

    def get_all_prices_in_comparison(self):
        self.logger.info("Retrieving all product prices in comparison")
        prices = self.compare_page.get_all_product_prices_in_comparison()
        self.logger.info(f"Retrieved {len(prices)} product prices from comparison")
        return prices

    def get_all_specifications_in_comparison(self):
        self.logger.info("Retrieving all product specifications in comparison")
        specs = self.compare_page.get_all_specifications_in_comparison()
        self.logger.info(f"Retrieved {len(specs)} product specifications from comparison")
        return specs

    def verify_no_products_message(self):
        self.logger.info("Verifying no products to compare message is displayed")
        is_displayed = self.compare_page.is_no_products_message_displayed()
        if is_displayed:
            self.logger.info("No products message verified successfully")
        else:
            self.logger.warning("No products message not displayed")
        return is_displayed

    def verify_comparison_table_displayed(self):
        self.logger.info("Verifying comparison table is displayed")
        is_displayed = self.compare_page.is_comparison_table_visible()
        if is_displayed:
            self.logger.info("Comparison table verified successfully")
        else:
            self.logger.warning("Comparison table not displayed")
        return is_displayed

    def get_comparison_error_message(self):
        self.logger.info("Retrieving comparison error message")
        error_message = self.compare_page.get_error_message()
        if error_message:
            self.logger.warning(f"Comparison error: {error_message}")
            return error_message
        return None

    def verify_comparison_has_error(self):
        self.logger.info("Verifying comparison has error")
        has_error = self.compare_page.is_any_error_displayed()
        if has_error:
            self.logger.warning("Comparison error detected")
        else:
            self.logger.info("No comparison error detected")
        return has_error

    def get_comparison_success_message(self):
        self.logger.info("Retrieving comparison success message")
        success_message = self.compare_page.get_success_message()
        if success_message:
            self.logger.info(f"Comparison success: {success_message}")
            return success_message
        return None

    def verify_comparison_success(self):
        self.logger.info("Verifying comparison success message is displayed")
        is_displayed = self.compare_page.is_success_message_displayed()
        if is_displayed:
            self.logger.info("Comparison success message verified")
        else:
            self.logger.warning("Comparison success message not displayed")
        return is_displayed

    def add_and_compare_products(self, product_indices):
        self.logger.info(f"Adding products {product_indices} and navigating to comparison")
        self.add_multiple_products_to_comparison(product_indices)
        self.navigate_to_comparison_page()
        self.logger.info("Products added and comparison page navigated")

    def compare_product_specifications(self, product_indices):
        self.logger.info(f"Comparing specifications for products {product_indices}")
        self.add_and_compare_products(product_indices)
        specifications = self.get_all_specifications_in_comparison()
        self.logger.info(f"Retrieved specifications for comparison")
        return specifications

    def compare_product_prices(self, product_indices):
        self.logger.info(f"Comparing prices for products {product_indices}")
        self.add_and_compare_products(product_indices)
        prices = self.get_all_prices_in_comparison()
        self.logger.info(f"Retrieved prices for comparison")
        return prices

    def validate_adding_product_for_comparison_from_search_results_list_view(self):
        """Test: Validate adding the product for comparison from List View of Search Results page."""
        self.logger.info("TEST: Validate adding product for comparison from Search Results list view")
        try:
            self.wait_for_compare_page_to_load()
            self.compare_page.add_product_to_comparison(0)
            success = self.compare_page.is_compare_success_message_visible()
            count = self.get_product_count_in_comparison()
            product_added = count >= 1 and success
            
            if product_added:
                self.logger.info("✓ TEST PASSED: Product added to comparison from search results")
            else:
                self.logger.error("✗ TEST FAILED: Product not added to comparison")
            
            return {
                'test_case_title': 'Validate adding product for comparison from List View of Search Results page',
                'product_count': count,
                'success_message_visible': success,
                'test_passed': product_added,
                'test_failure_reason': None if product_added else 'Failed to add product to comparison'
            }
        except Exception as e:
            self.logger.error(f"TEST FAILED: {str(e)}")
            return {
                'test_case_title': 'Validate adding product for comparison from List View of Search Results page',
                'product_count': 0,
                'success_message_visible': False,
                'test_passed': False,
                'test_failure_reason': str(e)
            }
    def validate_product_compare_page_when_no_products_are_added_for_comparison(self):
        """Test: Validate 'Product Compare' page when no products are added for comparison."""
        self.logger.info("TEST: Validate Product Compare page when no products are added")
        try:
            self.wait_for_compare_page_to_load()
            self.clear_all_products_from_comparison()
            no_products_msg = self.verify_no_products_message()
            table_visible = self.verify_comparison_table_displayed()
            empty_state = no_products_msg and not table_visible
            
            if empty_state:
                self.logger.info("✓ TEST PASSED: Empty state displayed correctly")
            else:
                self.logger.error("✗ TEST FAILED: Empty state not displayed correctly")
            
            return {
                'test_case_title': 'Validate Product Compare page when no products are added for comparison',
                'no_products_message_displayed': no_products_msg,
                'comparison_table_visible': table_visible,
                'test_passed': empty_state,
                'test_failure_reason': None if empty_state else 'Empty state validation failed'
            }
        except Exception as e:
            self.logger.error(f"TEST FAILED: {str(e)}")
            return {
                'test_case_title': 'Validate Product Compare page when no products are added for comparison',
                'no_products_message_displayed': False,
                'comparison_table_visible': False,
                'test_passed': False,
                'test_failure_reason': str(e)
            }

    def verify_same_product_is_not_duplicated_in_compare_list(self):
        """Test: Verify same product is not duplicated in Compare list."""
        self.logger.info("TEST: Verify same product is not duplicated in Compare list")
        try:
            self.wait_for_compare_page_to_load()
            self.compare_page.add_product_to_comparison(0)
            count_after_first = self.get_product_count_in_comparison()
            self.compare_page.add_product_to_comparison(0)
            count_after_second = self.get_product_count_in_comparison()
            not_duplicated = count_after_first == count_after_second
            
            if not_duplicated:
                self.logger.info("✓ TEST PASSED: Same product not duplicated in compare list")
            else:
                self.logger.error("✗ TEST FAILED: Product was duplicated")
            
            return {
                'test_case_title': 'Verify same product is not duplicated in Compare list',
                'count_after_first_add': count_after_first,
                'count_after_second_add': count_after_second,
                'test_passed': not_duplicated,
                'test_failure_reason': None if not_duplicated else 'Product was duplicated'
            }
        except Exception as e:
            self.logger.error(f"TEST FAILED: {str(e)}")
            return {
                'test_case_title': 'Verify same product is not duplicated in Compare list',
                'count_after_first_add': 0,
                'count_after_second_add': 0,
                'test_passed': False,
                'test_failure_reason': str(e)
            }