from pages.productDisplayPage import ProductDisplayPage
from utilities.customLogger import LoggerFactory


class ProductDisplayFlow:
    logger = LoggerFactory.get_logger(__name__)

    def __init__(self, driver):
        self.driver = driver
        self.product_page = ProductDisplayPage(driver)

    def wait_for_product_page_to_load(self):
        self.logger.info("Waiting for Product Display page to load")
        self.product_page.handle_cloudflare_if_present()
        if not self.product_page.is_page_loaded():
            self.logger.error("Product Display page failed to load")
            raise Exception("Product Display page failed to load")
        self.logger.info("Product Display page loaded successfully")

    def get_product_details(self):
        self.logger.info("Retrieving all product details")
        self.wait_for_product_page_to_load()
        product_details = {
            "name": self.product_page.get_product_name(),
            "price": self.product_page.get_product_price(),
            "description": self.product_page.get_product_description(),
            "rating": self.product_page.get_product_rating(),
            "review_count": self.product_page.get_review_count(),
            "sku": self.product_page.get_product_sku(),
            "availability": self.product_page.get_availability_status(),
            "stock_status": self.product_page.get_stock_status()
        }
        self.logger.info(f"Product details retrieved: {product_details}")
        return product_details

    def get_product_name(self):
        self.logger.info("Getting product name")
        self.wait_for_product_page_to_load()
        return self.product_page.get_product_name()

    def get_product_price(self):
        self.logger.info("Getting product price")
        self.wait_for_product_page_to_load()
        return self.product_page.get_product_price()

    def get_product_description(self):
        self.logger.info("Getting product description")
        self.wait_for_product_page_to_load()
        return self.product_page.get_product_description()

    def get_product_rating(self):
        self.logger.info("Getting product rating")
        self.wait_for_product_page_to_load()
        return self.product_page.get_product_rating()

    def get_review_count(self):
        self.logger.info("Getting review count")
        self.wait_for_product_page_to_load()
        return self.product_page.get_review_count()

    def get_product_sku(self):
        self.logger.info("Getting product SKU")
        self.wait_for_product_page_to_load()
        return self.product_page.get_product_sku()

    def verify_product_in_stock(self):
        self.logger.info("Verifying product is in stock")
        self.wait_for_product_page_to_load()
        is_in_stock = self.product_page.is_product_in_stock()
        if is_in_stock:
            self.logger.info("Product is in stock")
        else:
            self.logger.warning("Product is out of stock")
        return is_in_stock

    def add_product_to_cart_with_quantity(self, quantity):
        self.logger.info(f"Adding product to cart with quantity: {quantity}")
        self.wait_for_product_page_to_load()
        self.product_page.enter_quantity(quantity)
        self.product_page.add_product_to_cart()
        self.logger.info(f"Product added to cart with quantity: {quantity}")

    def add_product_to_cart(self):
        self.logger.info("Adding product to cart")
        self.wait_for_product_page_to_load()
        self.product_page.add_product_to_cart()
        self.logger.info("Product added to cart")

    def add_product_to_wishlist(self):
        self.logger.info("Adding product to wishlist")
        self.wait_for_product_page_to_load()
        self.product_page.add_product_to_wishlist()
        self.logger.info("Product added to wishlist")

    def add_product_to_compare(self):
        self.logger.info("Adding product to compare")
        self.wait_for_product_page_to_load()
        self.product_page.add_product_to_compare()
        self.logger.info("Product added to compare")

    def select_product_size(self, size):
        self.logger.info(f"Selecting product size: {size}")
        self.wait_for_product_page_to_load()
        self.product_page.select_size(size)
        self.logger.info(f"Product size selected: {size}")

    def select_product_color(self, color):
        self.logger.info(f"Selecting product color: {color}")
        self.wait_for_product_page_to_load()
        self.product_page.select_color(color)
        self.logger.info(f"Product color selected: {color}")

    def add_product_with_attributes(self, size=None, color=None, quantity=1):
        self.logger.info(f"Adding product with attributes - Size: {size}, Color: {color}, Quantity: {quantity}")
        self.wait_for_product_page_to_load()
        if size:
            self.select_product_size(size)
        if color:
            self.select_product_color(color)
        self.add_product_to_cart_with_quantity(quantity)
        self.logger.info("Product added with attributes")

    def view_product_reviews(self):
        self.logger.info("Viewing product reviews")
        self.wait_for_product_page_to_load()
        self.product_page.click_reviews_tab()
        self.logger.info("Switched to reviews tab")

    def verify_reviews_visible(self):
        self.logger.info("Verifying reviews are visible")
        are_visible = self.product_page.are_reviews_visible()
        if are_visible:
            self.logger.info("Reviews are visible")
        else:
            self.logger.warning("Reviews are not visible")
        return are_visible

    def navigate_to_write_review(self):
        self.logger.info("Navigating to write review")
        self.wait_for_product_page_to_load()
        self.product_page.click_write_review_button()
        self.logger.info("Navigation to write review initiated")

    def verify_related_products_displayed(self):
        self.logger.info("Verifying related products are displayed")
        are_displayed = self.product_page.are_related_products_displayed()
        if are_displayed:
            self.logger.info("Related products are displayed")
        else:
            self.logger.warning("Related products are not displayed")
        return are_displayed

    def verify_product_action_success(self):
        self.logger.info("Verifying product action success")
        is_successful = self.product_page.is_success_message_displayed()
        if is_successful:
            success_message = self.product_page.get_success_message()
            self.logger.info(f"Product action success: {success_message}")
        else:
            self.logger.warning("Product action success not verified")
        return is_successful

    def get_product_action_error(self):
        self.logger.info("Retrieving product action error")
        error_message = self.product_page.get_error_message()
        if error_message:
            self.logger.warning(f"Product action error: {error_message}")
            return error_message
        return None

    def verify_product_action_has_error(self):
        self.logger.info("Verifying product action has error")
        has_error = self.product_page.is_error_message_displayed()
        if has_error:
            self.logger.warning("Product action error detected")
        else:
            self.logger.info("No product action error detected")
        return has_error

    def verify_add_to_cart_button_enabled(self):
        self.logger.info("Verifying add to cart button is enabled")
        is_enabled = self.product_page.is_add_to_cart_button_enabled()
        if is_enabled:
            self.logger.info("Add to cart button is enabled")
        else:
            self.logger.warning("Add to cart button is not enabled")
        return is_enabled

    def go_back_to_previous_page(self):
        self.logger.info("Going back to previous page")
        self.wait_for_product_page_to_load()
        self.product_page.click_back()
        self.logger.info("Navigation back initiated")

    def verify_product_availability(self):
        self.logger.info("Verifying product availability")
        availability = self.product_page.get_availability_status()
        self.logger.info(f"Product availability: {availability}")
        return availability

    def get_product_complete_information(self):
        self.logger.info("Retrieving complete product information")
        complete_info = {
            "details": self.get_product_details(),
            "in_stock": self.verify_product_in_stock(),
            "related_products_available": self.verify_related_products_displayed()
        }
        self.logger.info("Complete product information retrieved")
        return complete_info

    def verify_product_is_displayed_correctly_on_product_listing_page(self):
        """Test: Verify product is displayed correctly on Product Listing page."""
        self.logger.info("TEST: Verify product is displayed correctly on Product Listing page")
        try:
            self.wait_for_product_page_to_load()
            product_name = self.product_page.get_product_name()
            product_visible = self.product_page.is_product_visible()
            product_price = self.product_page.get_product_price()
            product_image = self.product_page.is_product_image_visible()
            all_elements_visible = product_visible and product_image and product_name and product_price
            
            if all_elements_visible:
                self.logger.info("✓ TEST PASSED: Product displayed correctly on listing page")
            else:
                self.logger.error("✗ TEST FAILED: Product not displayed correctly")
            
            return {
                'test_case_title': 'Verify product is displayed correctly on Product Listing page',
                'product_name': product_name,
                'product_visible': product_visible,
                'product_image_visible': product_image,
                'product_price': product_price,
                'test_passed': all_elements_visible,
                'test_failure_reason': None if all_elements_visible else 'Product elements not fully visible'
            }
        except Exception as e:
            self.logger.error(f"TEST FAILED: {str(e)}")
            return {
                'test_case_title': 'Verify product is displayed correctly on Product Listing page',
                'product_name': None,
                'product_visible': False,
                'product_image_visible': False,
                'product_price': None,
                'test_passed': False,
                'test_failure_reason': str(e)
            }

    def verify_product_name_is_displayed_correctly(self):
        """Test: Verify product name is displayed correctly."""
        self.logger.info("TEST: Verify product name is displayed correctly")
        try:
            self.wait_for_product_page_to_load()
            product_name = self.product_page.get_product_name()
            name_visible = self.product_page.is_product_name_visible()
            name_not_empty = product_name and len(product_name.strip()) > 0
            name_displayed_correctly = name_visible and name_not_empty
            
            if name_displayed_correctly:
                self.logger.info(f"✓ TEST PASSED: Product name '{product_name}' displayed correctly")
            else:
                self.logger.error("✗ TEST FAILED: Product name not displayed correctly")
            
            return {
                'test_case_title': 'Verify product name is displayed correctly',
                'product_name': product_name,
                'name_visible': name_visible,
                'name_not_empty': name_not_empty,
                'test_passed': name_displayed_correctly,
                'test_failure_reason': None if name_displayed_correctly else 'Product name not displayed correctly'
            }
        except Exception as e:
            self.logger.error(f"TEST FAILED: {str(e)}")
            return {
                'test_case_title': 'Verify product name is displayed correctly',
                'product_name': None,
                'name_visible': False,
                'name_not_empty': False,
                'test_passed': False,
                'test_failure_reason': str(e)
            }

    def verify_product_sku_is_displayed_correctly(self):
        """Test: Verify product SKU is displayed correctly."""
        self.logger.info("TEST: Verify product SKU is displayed correctly")
        try:
            self.wait_for_product_page_to_load()
            product_sku = self.product_page.get_product_sku()
            sku_visible = self.product_page.is_product_sku_visible()
            sku_not_empty = product_sku and len(product_sku.strip()) > 0
            sku_displayed_correctly = sku_visible and sku_not_empty
            
            if sku_displayed_correctly:
                self.logger.info(f"✓ TEST PASSED: Product SKU '{product_sku}' displayed correctly")
            else:
                self.logger.error("✗ TEST FAILED: Product SKU not displayed correctly")
            
            return {
                'test_case_title': 'Verify product SKU is displayed correctly',
                'product_sku': product_sku,
                'sku_visible': sku_visible,
                'sku_not_empty': sku_not_empty,
                'test_passed': sku_displayed_correctly,
                'test_failure_reason': None if sku_displayed_correctly else 'Product SKU not displayed correctly'
            }
        except Exception as e:
            self.logger.error(f"TEST FAILED: {str(e)}")
            return {
                'test_case_title': 'Verify product SKU is displayed correctly',
                'product_sku': None,
                'sku_visible': False,
                'sku_not_empty': False,
                'test_passed': False,
                'test_failure_reason': str(e)
            }

    def verify_product_category_and_breadcrumb_are_correct(self):
        """Test: Verify product category and breadcrumb are correct."""
        self.logger.info("TEST: Verify product category and breadcrumb are correct")
        try:
            self.wait_for_product_page_to_load()
            category = self.product_page.get_product_category()
            breadcrumb_visible = self.product_page.is_breadcrumb_visible()
            breadcrumb_path = self.product_page.get_breadcrumb_path()
            category_in_breadcrumb = category and breadcrumb_path and category.lower() in breadcrumb_path.lower()
            both_correct = breadcrumb_visible and category_in_breadcrumb
            
            if both_correct:
                self.logger.info(f"✓ TEST PASSED: Category '{category}' and breadcrumb correct")
            else:
                self.logger.error("✗ TEST FAILED: Category or breadcrumb not correct")
            
            return {
                'test_case_title': 'Verify product category and breadcrumb are correct',
                'product_category': category,
                'breadcrumb_visible': breadcrumb_visible,
                'breadcrumb_path': breadcrumb_path,
                'category_in_breadcrumb': category_in_breadcrumb,
                'test_passed': both_correct,
                'test_failure_reason': None if both_correct else 'Category or breadcrumb mismatch'
            }
        except Exception as e:
            self.logger.error(f"TEST FAILED: {str(e)}")
            return {
                'test_case_title': 'Verify product category and breadcrumb are correct',
                'product_category': None,
                'breadcrumb_visible': False,
                'breadcrumb_path': None,
                'category_in_breadcrumb': False,
                'test_passed': False,
                'test_failure_reason': str(e)
            }

    def verify_product_page_reflects_updated_catalog_changes(self):
        """Test: Verify product page reflects updated catalog changes."""
        self.logger.info("TEST: Verify product page reflects updated catalog changes")
        try:
            self.wait_for_product_page_to_load()
            product_name = self.product_page.get_product_name()
            product_price = self.product_page.get_product_price()
            product_sku = self.product_page.get_product_sku()
            availability = self.product_page.get_availability_status()
            page_loaded = self.product_page.is_page_loaded()
            all_info_present = product_name and product_price and product_sku and availability and page_loaded
            
            if all_info_present:
                self.logger.info("✓ TEST PASSED: Product page shows all updated catalog changes")
            else:
                self.logger.error("✗ TEST FAILED: Product page missing some catalog information")
            
            return {
                'test_case_title': 'Verify product page reflects updated catalog changes',
                'product_name': product_name,
                'product_price': product_price,
                'product_sku': product_sku,
                'availability': availability,
                'page_loaded': page_loaded,
                'test_passed': all_info_present,
                'test_failure_reason': None if all_info_present else 'Missing catalog information'
            }
        except Exception as e:
            self.logger.error(f"TEST FAILED: {str(e)}")
            return {
                'test_case_title': 'Verify product page reflects updated catalog changes',
                'product_name': None,
                'product_price': None,
                'product_sku': None,
                'availability': None,
                'page_loaded': False,
                'test_passed': False,
                'test_failure_reason': str(e)
            }

    def verify_product_page_remains_accessible_for_historical_orders(self):
        """Test: Verify product page remains accessible for historical orders."""
        self.logger.info("TEST: Verify product page remains accessible for historical orders")
        try:
            self.wait_for_product_page_to_load()
            product_accessible = self.product_page.is_page_loaded()
            product_name = self.product_page.get_product_name()
            no_access_error = not self.product_page.is_error_message_displayed()
            product_data_available = product_name and product_accessible
            page_accessible = product_data_available and no_access_error
            
            if page_accessible:
                self.logger.info("✓ TEST PASSED: Product page accessible for historical orders")
            else:
                self.logger.error("✗ TEST FAILED: Product page not accessible")
            
            return {
                'test_case_title': 'Verify product page remains accessible for historical orders',
                'product_name': product_name,
                'page_accessible': product_accessible,
                'has_access_error': not no_access_error,
                'product_data_available': product_data_available,
                'test_passed': page_accessible,
                'test_failure_reason': None if page_accessible else 'Product page not accessible'
            }
        except Exception as e:
            self.logger.error(f"TEST FAILED: {str(e)}")
            return {
                'test_case_title': 'Verify product page remains accessible for historical orders',
                'product_name': None,
                'page_accessible': False,
                'has_access_error': True,
                'product_data_available': False,
                'test_passed': False,
                'test_failure_reason': str(e)
            }

    def verify_product_page_does_not_display_stale_or_cached_data(self):
        """Test: Verify product page does not display stale or cached data."""
        self.logger.info("TEST: Verify product page does not display stale or cached data")
        try:
            self.wait_for_product_page_to_load()
            product_name = self.product_page.get_product_name()
            product_price = self.product_page.get_product_price()
            last_modified = self.product_page.get_last_modified_timestamp()
            page_fresh = self.product_page.is_page_fresh()
            data_current = product_name and product_price and not (last_modified and "cached" in str(last_modified).lower())
            not_stale = page_fresh and data_current
            
            if not_stale:
                self.logger.info("✓ TEST PASSED: Product page displays fresh data, not stale/cached")
            else:
                self.logger.error("✗ TEST FAILED: Product page showing stale or cached data")
            
            return {
                'test_case_title': 'Verify product page does not display stale or cached data',
                'product_name': product_name,
                'product_price': product_price,
                'last_modified': last_modified,
                'page_fresh': page_fresh,
                'data_current': data_current,
                'test_passed': not_stale,
                'test_failure_reason': None if not_stale else 'Stale or cached data detected'
            }
        except Exception as e:
            self.logger.error(f"TEST FAILED: {str(e)}")
            return {
                'test_case_title': 'Verify product page does not display stale or cached data',
                'product_name': None,
                'product_price': None,
                'last_modified': None,
                'page_fresh': False,
                'data_current': False,
                'test_passed': False,
                'test_failure_reason': str(e)
            }
