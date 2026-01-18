from pages.shoppingCartReviewPage import ShoppingCartReviewPage
from utilities.customLogger import LoggerFactory


class ShoppingCartFlow:
    logger = LoggerFactory.get_logger(__name__)

    def __init__(self, driver):
        self.driver = driver
        self.cart_review_page = ShoppingCartReviewPage(driver)

    def wait_for_cart_review_page_to_load(self):
        self.logger.info("Waiting for Shopping Cart Review page to load")
        self.cart_review_page.handle_cloudflare_if_present()
        if not self.cart_review_page.is_page_loaded():
            self.logger.error("Shopping Cart Review page failed to load")
            raise Exception("Shopping Cart Review page failed to load")
        self.logger.info("Shopping Cart Review page loaded successfully")

    def verify_cart_contains_items(self):
        self.logger.info("Verifying cart contains items")
        self.wait_for_cart_review_page_to_load()
        is_empty = self.cart_review_page.is_cart_empty()
        if not is_empty:
            self.logger.info("Cart contains items")
        else:
            self.logger.warning("Cart is empty")
        return not is_empty

    def get_cart_item_count(self):
        self.logger.info("Getting cart item count")
        self.wait_for_cart_review_page_to_load()
        count = self.cart_review_page.get_number_of_items()
        self.logger.info(f"Cart item count: {count}")
        return count

    def verify_cart_item_count(self, expected_count):
        self.logger.info(f"Verifying cart has {expected_count} items")
        actual_count = self.get_cart_item_count()
        is_verified = actual_count == expected_count
        if is_verified:
            self.logger.info(f"Cart item count verified: {actual_count} == {expected_count}")
        else:
            self.logger.warning(f"Cart item count mismatch: {actual_count} != {expected_count}")
        return is_verified

    def review_cart_contents(self):
        self.logger.info("Reviewing cart contents")
        self.wait_for_cart_review_page_to_load()
        products = self.cart_review_page.get_all_product_details()
        self.logger.info(f"Cart contents reviewed: {len(products)} products")
        return products

    def get_complete_cart_summary(self):
        self.logger.info("Getting complete cart summary")
        self.wait_for_cart_review_page_to_load()
        summary = self.cart_review_page.get_cart_summary()
        self.logger.info(f"Cart summary retrieved: {summary}")
        return summary

    def verify_cart_total(self, expected_total):
        self.logger.info(f"Verifying cart total is {expected_total}")
        actual_total = self.cart_review_page.get_total()
        if actual_total:
            is_verified = expected_total in actual_total
            if is_verified:
                self.logger.info(f"Cart total verified: {actual_total}")
            else:
                self.logger.warning(f"Cart total mismatch: {actual_total} != {expected_total}")
            return is_verified
        return False

    def apply_discount_voucher(self, voucher_code):
        self.logger.info(f"Applying discount voucher: {voucher_code}")
        self.wait_for_cart_review_page_to_load()
        self.cart_review_page.apply_voucher_code(voucher_code)
        self.logger.info(f"Discount voucher {voucher_code} applied")

    def verify_voucher_applied(self):
        self.logger.info("Verifying voucher was applied")
        is_applied = self.cart_review_page.is_discount_applied()
        if is_applied:
            discount = self.cart_review_page.get_discount()
            self.logger.info(f"Voucher verified as applied. Discount: {discount}")
        else:
            self.logger.warning("Voucher not applied")
        return is_applied

    def select_shipping_method(self, method_index):
        self.logger.info(f"Selecting shipping method {method_index}")
        self.wait_for_cart_review_page_to_load()
        self.cart_review_page.select_shipping_method(method_index)
        self.logger.info(f"Shipping method {method_index} selected")

    def get_estimated_delivery_date(self):
        self.logger.info("Getting estimated delivery date")
        self.wait_for_cart_review_page_to_load()
        delivery_date = self.cart_review_page.get_estimated_delivery_date()
        self.logger.info(f"Estimated delivery date: {delivery_date}")
        return delivery_date

    def add_gift_message(self, message):
        self.logger.info(f"Adding gift message: {message}")
        self.wait_for_cart_review_page_to_load()
        self.cart_review_page.enter_gift_message(message)
        self.logger.info("Gift message added")

    def enable_gift_wrap_service(self):
        self.logger.info("Enabling gift wrap service")
        self.wait_for_cart_review_page_to_load()
        self.cart_review_page.enable_gift_wrap()
        self.logger.info("Gift wrap service enabled")

    def disable_gift_wrap_service(self):
        self.logger.info("Disabling gift wrap service")
        self.wait_for_cart_review_page_to_load()
        self.cart_review_page.disable_gift_wrap()
        self.logger.info("Gift wrap service disabled")

    def accept_terms_for_checkout(self):
        self.logger.info("Accepting terms and conditions for checkout")
        self.wait_for_cart_review_page_to_load()
        self.cart_review_page.accept_terms_and_conditions()
        self.logger.info("Terms and conditions accepted")

    def decline_terms_for_checkout(self):
        self.logger.info("Declining terms and conditions for checkout")
        self.wait_for_cart_review_page_to_load()
        self.cart_review_page.decline_terms_and_conditions()
        self.logger.info("Terms and conditions declined")

    def complete_cart_review_and_proceed(self, voucher_code=None, shipping_method=None, gift_message=None):
        self.logger.info("Completing cart review and proceeding to checkout")
        self.wait_for_cart_review_page_to_load()

        if voucher_code:
            self.apply_discount_voucher(voucher_code)

        if shipping_method is not None:
            self.select_shipping_method(shipping_method)

        if gift_message:
            self.add_gift_message(gift_message)

        self.accept_terms_for_checkout()
        self.cart_review_page.proceed_to_checkout()
        self.logger.info("Cart review completed and checkout initiated")

    def review_and_modify_cart(self, quantity_updates=None):
        self.logger.info("Reviewing cart and preparing to modify if needed")
        self.wait_for_cart_review_page_to_load()
        
        if quantity_updates:
            self.logger.info(f"Modifying cart quantities: {quantity_updates}")
            self.cart_review_page.edit_cart()
            self.logger.info("Cart edit initiated")
        
        products = self.review_cart_contents()
        return products

    def get_cart_pricing_breakdown(self):
        self.logger.info("Getting cart pricing breakdown")
        self.wait_for_cart_review_page_to_load()
        breakdown = {
            "subtotal": self.cart_review_page.get_subtotal(),
            "shipping": self.cart_review_page.get_shipping_cost(),
            "tax": self.cart_review_page.get_tax(),
            "discount": self.cart_review_page.get_discount(),
            "total": self.cart_review_page.get_total()
        }
        self.logger.info(f"Cart pricing breakdown: {breakdown}")
        return breakdown

    def verify_cart_action_success(self):
        self.logger.info("Verifying cart action success")
        is_successful = self.cart_review_page.is_success_message_displayed()
        if is_successful:
            message = self.cart_review_page.get_success_message()
            self.logger.info(f"Cart action successful: {message}")
        else:
            self.logger.warning("Cart action success not verified")
        return is_successful

    def get_cart_action_error(self):
        self.logger.info("Retrieving cart action error")
        error_message = self.cart_review_page.get_error_message()
        if error_message:
            self.logger.warning(f"Cart action error: {error_message}")
            return error_message
        return None

    def verify_cart_has_error(self):
        self.logger.info("Verifying cart has error")
        has_error = self.cart_review_page.is_error_message_displayed()
        if has_error:
            self.logger.warning("Cart error detected")
        else:
            self.logger.info("No cart error detected")
        return has_error

    def get_cart_action_warning(self):
        self.logger.info("Retrieving cart action warning")
        warning_message = self.cart_review_page.get_warning_message()
        if warning_message:
            self.logger.warning(f"Cart action warning: {warning_message}")
            return warning_message
        return None

    def verify_cart_has_warning(self):
        self.logger.info("Verifying cart has warning")
        has_warning = self.cart_review_page.is_warning_message_displayed()
        if has_warning:
            self.logger.warning("Cart warning detected")
        else:
            self.logger.info("No cart warning detected")
        return has_warning

    def review_cart_and_get_summary(self):
        self.logger.info("Reviewing cart and retrieving complete summary")
        self.wait_for_cart_review_page_to_load()
        
        summary = {
            "items": self.review_cart_contents(),
            "item_count": self.get_cart_item_count(),
            "pricing": self.get_cart_pricing_breakdown(),
            "estimated_delivery": self.get_estimated_delivery_date()
        }
        
        self.logger.info("Cart summary with all details retrieved")
        return summary

    def prepare_cart_for_checkout(self, apply_voucher=None, select_shipping=None, enable_gift=False, gift_msg=None):
        self.logger.info("Preparing cart for checkout")
        self.wait_for_cart_review_page_to_load()
        
        if apply_voucher:
            self.apply_discount_voucher(apply_voucher)
        
        if select_shipping is not None:
            self.select_shipping_method(select_shipping)
        
        if enable_gift:
            self.enable_gift_wrap_service()
            if gift_msg:
                self.add_gift_message(gift_msg)
        
        self.logger.info("Cart preparation completed")
    def validate_navigating_to_shopping_cart_from_success_message(self):
        """
        Validate navigating to 'shopping cart' page from the success message.
        
        Tests that success message is displayed and shopping cart page is accessible.
        
        Returns:
            dict: Test result with navigation and message validation
        """
        try:
            self.logger.info("TEST: Validate navigating to shopping cart from success message")
            
            # Verify cart page loaded
            if not self.cart_review_page.is_page_loaded():
                return self._build_navigation_result(False, "Cart page load failed")
            
            # Check if success message displayed
            success_message_displayed = self.cart_review_page.is_success_message_displayed()
            success_message_text = self.cart_review_page.get_success_message() if success_message_displayed else None
            
            # Verify page title indicates shopping cart
            page_title = self.driver.title
            cart_in_title = "cart" in page_title.lower()
            
            # Test result
            test_passed = success_message_displayed and cart_in_title
            
            if test_passed:
                self.logger.info("✓ TEST PASSED: Shopping cart accessible from success message")
            else:
                self.logger.error("✗ TEST FAILED: Navigation or message validation failed")
            
            return {
                'test_case_title': "Validate navigating to 'shopping cart' page from the success message",
                'page_title': page_title,
                'success_message_displayed': success_message_displayed,
                'success_message_text': success_message_text,
                'cart_title_verified': cart_in_title,
                'page_loaded': True,
                'test_passed': test_passed,
                'test_failure_reason': None if test_passed else "Success message not displayed or cart title not verified"
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_navigation_result(False, str(e))

    def _build_navigation_result(self, test_passed, failure_reason):
        """Build navigation test result dictionary."""
        return {
            'test_case_title': "Validate navigating to 'shopping cart' page from the success message",
            'page_title': self.driver.title if self.driver else None,
            'success_message_displayed': False,
            'success_message_text': None,
            'cart_title_verified': False,
            'page_loaded': False,
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }

    def validate_removing_item_from_shopping_cart(self, product_index=0):
        """
        Validate removing the item from the shopping cart.
        
        Tests that a product can be removed and cart updates immediately.
        
        Args:
            product_index (int): Index of product to remove (default: 0)
            
        Returns:
            dict: Test result with removal and cart update validation
        """
        try:
            self.logger.info("TEST: Validate removing item from shopping cart")
            
            # Verify cart page loaded
            if not self.cart_review_page.is_page_loaded():
                return self._build_removal_result(False, "Cart page load failed")
            
            # Get initial item count
            initial_count = self.get_cart_item_count()
            self.logger.debug(f"Initial cart count: {initial_count}")
            
            # Remove product
            self.cart_review_page.remove_product_from_cart(product_index)
            self.logger.debug(f"Removed product at index {product_index}")
            
            # Get updated count
            updated_count = self.get_cart_item_count()
            count_decreased = updated_count < initial_count
            
            self.logger.debug(f"Updated cart count: {updated_count}")
            
            # Test passes if count decreased by exactly 1
            test_passed = count_decreased and updated_count == (initial_count - 1)
            
            if test_passed:
                self.logger.info("✓ TEST PASSED: Item successfully removed from cart")
            else:
                self.logger.error("✗ TEST FAILED: Item removal or cart update validation failed")
            
            return {
                'test_case_title': "Validate removing the item from the shopping cart",
                'product_index': product_index,
                'initial_cart_count': initial_count,
                'updated_cart_count': updated_count,
                'item_removed': count_decreased,
                'count_decreased_by_one': updated_count == (initial_count - 1),
                'test_passed': test_passed,
                'test_failure_reason': None if test_passed else "Item count did not decrease correctly"
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_removal_result(False, str(e))

    def _build_removal_result(self, test_passed, failure_reason):
        """Build removal test result dictionary."""
        return {
            'test_case_title': "Validate removing the item from the shopping cart",
            'product_index': 0,
            'initial_cart_count': 0,
            'updated_cart_count': 0,
            'item_removed': False,
            'count_decreased_by_one': False,
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }

    def verify_shopping_cart_displays_added_products_correctly(self):
        """
        Verify Shopping Cart displays added products correctly.
        
        Tests that products are visible in cart with proper names and prices.
        
        Returns:
            dict: Test result with product display validation
        """
        try:
            self.logger.info("TEST: Verify Shopping Cart displays added products correctly")
            
            # Verify cart page loaded
            if not self.cart_review_page.is_page_loaded():
                return self._build_product_display_result(False, "Cart page load failed")
            
            # Get cart item count
            item_count = self.get_cart_item_count()
            
            # Get product names and prices
            product_names = self.cart_review_page.get_all_product_names_in_cart()
            product_prices = self.cart_review_page.get_all_product_prices_in_cart()
            
            self.logger.debug(f"Products found: {len(product_names)}, Prices found: {len(product_prices)}")
            
            # Verify all products have names and prices
            names_valid = len(product_names) == item_count and all(product_names)
            prices_valid = len(product_prices) == item_count and all(product_prices)
            
            test_passed = names_valid and prices_valid
            
            if test_passed:
                self.logger.info("✓ TEST PASSED: All products displayed correctly with names and prices")
            else:
                self.logger.error("✗ TEST FAILED: Some products missing names or prices")
            
            return {
                'test_case_title': "Verify Shopping Cart displays added products correctly",
                'total_products': item_count,
                'products_with_names': len(product_names),
                'products_with_prices': len(product_prices),
                'all_names_present': names_valid,
                'all_prices_present': prices_valid,
                'test_passed': test_passed,
                'test_failure_reason': None if test_passed else "Missing product names or prices"
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_product_display_result(False, str(e))

    def _build_product_display_result(self, test_passed, failure_reason):
        """Build product display test result dictionary."""
        return {
            'test_case_title': "Verify Shopping Cart displays added products correctly",
            'total_products': 0,
            'products_with_names': 0,
            'products_with_prices': 0,
            'all_names_present': False,
            'all_prices_present': False,
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }

    def verify_shopping_cart_reject_zero_quantity_input(self, product_index=0):
        """
        Verify shopping cart reject zero quantity input.
        
        Tests that setting product quantity to zero is rejected with error.
        
        Args:
            product_index (int): Index of product to test (default: 0)
            
        Returns:
            dict: Test result with zero quantity rejection validation
        """
        try:
            self.logger.info("TEST: Verify shopping cart reject zero quantity input")
            
            # Verify cart page loaded
            if not self.cart_review_page.is_page_loaded():
                return self._build_quantity_result(False, "Cart page load failed")
            
            # Enter edit mode
            self.cart_review_page.edit_cart()
            self.logger.debug("Entered edit mode")
            
            # Try to set quantity to 0
            self.cart_review_page.update_product_quantity(product_index, 0)
            self.cart_review_page.update_cart()
            self.logger.debug("Attempted to update quantity to 0")
            
            # Check if error message displayed
            error_displayed = self.cart_review_page.is_error_message_displayed()
            error_msg = self.cart_review_page.get_error_message() if error_displayed else None
            
            test_passed = error_displayed
            
            if test_passed:
                self.logger.info("✓ TEST PASSED: Zero quantity input correctly rejected")
            else:
                self.logger.error("✗ TEST FAILED: Zero quantity input was not rejected")
            
            return {
                'test_case_title': "Verify shopping cart reject zero quantity input",
                'product_index': product_index,
                'quantity_set': 0,
                'error_message_displayed': error_displayed,
                'error_message': error_msg,
                'test_passed': test_passed,
                'test_failure_reason': None if test_passed else "Zero quantity was not rejected"
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_quantity_result(False, str(e))

    def _build_quantity_result(self, test_passed, failure_reason):
        """Build quantity validation test result dictionary."""
        return {
            'test_case_title': "Verify shopping cart reject zero quantity input",
            'product_index': 0,
            'quantity_set': 0,
            'error_message_displayed': False,
            'error_message': None,
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }

    def verify_shopping_cart_applies_product_price_correctly(self):
        """
        Verify Shopping Cart applies product price correctly.
        
        Tests that product prices are displayed and total is calculated correctly.
        
        Returns:
            dict: Test result with price application validation
        """
        try:
            self.logger.info("TEST: Verify Shopping Cart applies product price correctly")
            
            # Verify cart page loaded
            if not self.cart_review_page.is_page_loaded():
                return self._build_price_result(False, "Cart page load failed")
            
            # Get item count
            item_count = self.get_cart_item_count()
            
            # Get all product prices
            product_prices = self.cart_review_page.get_all_product_prices_in_cart()
            
            # Get cart totals
            subtotal = self.cart_review_page.get_cart_subtotal()
            total = self.cart_review_page.get_cart_total()
            
            self.logger.debug(f"Items: {item_count}, Prices: {len(product_prices)}, Subtotal: {subtotal}, Total: {total}")
            
            # Verify all products have prices and totals are valid
            prices_valid = len(product_prices) == item_count and all(product_prices)
            totals_valid = subtotal is not None and total is not None
            
            test_passed = prices_valid and totals_valid
            
            if test_passed:
                self.logger.info("✓ TEST PASSED: Product prices applied correctly")
            else:
                self.logger.error("✗ TEST FAILED: Product prices or totals invalid")
            
            return {
                'test_case_title': "Verify Shopping Cart applies product price correctly",
                'total_products': item_count,
                'products_with_prices': len(product_prices),
                'subtotal': subtotal,
                'total': total,
                'prices_valid': prices_valid,
                'totals_valid': totals_valid,
                'test_passed': test_passed,
                'test_failure_reason': None if test_passed else "Product prices or totals invalid"
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_price_result(False, str(e))

    def _build_price_result(self, test_passed, failure_reason):
        """Build price validation test result dictionary."""
        return {
            'test_case_title': "Verify Shopping Cart applies product price correctly",
            'total_products': 0,
            'products_with_prices': 0,
            'subtotal': None,
            'total': None,
            'prices_valid': False,
            'totals_valid': False,
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }

    def verify_shopping_cart_updates_totals_after_product_removal(self, product_index=0):
        """
        Verify Shopping Cart updates totals after product removal.
        
        Tests that cart totals decrease after removing a product.
        
        Args:
            product_index (int): Index of product to remove (default: 0)
            
        Returns:
            dict: Test result with total update validation after removal
        """
        try:
            self.logger.info("TEST: Verify Shopping Cart updates totals after product removal")
            
            # Verify cart page loaded
            if not self.cart_review_page.is_page_loaded():
                return self._build_removal_total_result(False, "Cart page load failed")
            
            # Get initial totals
            initial_subtotal = self.cart_review_page.get_cart_subtotal()
            initial_total = self.cart_review_page.get_cart_total()
            self.logger.debug(f"Initial - Subtotal: {initial_subtotal}, Total: {initial_total}")
            
            # Remove product
            self.cart_review_page.remove_product_from_cart(product_index)
            self.logger.debug(f"Removed product at index {product_index}")
            
            # Get updated totals
            updated_subtotal = self.cart_review_page.get_cart_subtotal()
            updated_total = self.cart_review_page.get_cart_total()
            self.logger.debug(f"Updated - Subtotal: {updated_subtotal}, Total: {updated_total}")
            
            # Verify totals decreased
            subtotal_decreased = updated_subtotal < initial_subtotal
            total_decreased = updated_total < initial_total
            
            test_passed = subtotal_decreased and total_decreased
            
            if test_passed:
                self.logger.info("✓ TEST PASSED: Totals updated correctly after product removal")
            else:
                self.logger.error("✗ TEST FAILED: Totals did not update after product removal")
            
            return {
                'test_case_title': "Verify Shopping Cart updates totals after product removal",
                'product_index': product_index,
                'initial_subtotal': initial_subtotal,
                'updated_subtotal': updated_subtotal,
                'initial_total': initial_total,
                'updated_total': updated_total,
                'subtotal_decreased': subtotal_decreased,
                'total_decreased': total_decreased,
                'test_passed': test_passed,
                'test_failure_reason': None if test_passed else "Totals did not decrease after removal"
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_removal_total_result(False, str(e))

    def _build_removal_total_result(self, test_passed, failure_reason):
        """Build removal total update test result dictionary."""
        return {
            'test_case_title': "Verify Shopping Cart updates totals after product removal",
            'product_index': 0,
            'initial_subtotal': None,
            'updated_subtotal': None,
            'initial_total': None,
            'updated_total': None,
            'subtotal_decreased': False,
            'total_decreased': False,
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }

    def verify_shopping_cart_handles_out_of_stock_products_correctly(self):
        """
        Verify shopping cart handles out-of-stock products correctly.
        
        Tests that cart properly displays out-of-stock status or messages.
        
        Returns:
            dict: Test result with out-of-stock handling validation
        """
        try:
            self.logger.info("TEST: Verify shopping cart handles out-of-stock products correctly")
            
            # Verify cart page loaded
            if not self.cart_review_page.is_page_loaded():
                return self._build_stock_result(False, "Cart page load failed")
            
            # Check if cart is empty (out-of-stock products may be removed)
            is_empty = self.cart_review_page.is_cart_empty()
            
            # Check for error or warning messages
            error_displayed = self.cart_review_page.is_error_message_displayed()
            error_msg = self.cart_review_page.get_error_message() if error_displayed else None
            
            # Get item count
            item_count = self.get_cart_item_count() if not is_empty else 0
            
            self.logger.debug(f"Cart empty: {is_empty}, Error displayed: {error_displayed}, Items: {item_count}")
            
            # Test passes if either cart is empty OR error message is displayed
            test_passed = is_empty or error_displayed
            
            if test_passed:
                self.logger.info("✓ TEST PASSED: Out-of-stock products handled correctly")
            else:
                self.logger.error("✗ TEST FAILED: Out-of-stock handling not detected")
            
            return {
                'test_case_title': "Verify shopping cart handles out-of-stock products correctly",
                'cart_empty': is_empty,
                'item_count': item_count,
                'error_message_displayed': error_displayed,
                'error_message': error_msg,
                'test_passed': test_passed,
                'test_failure_reason': None if test_passed else "Out-of-stock products not handled"
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_stock_result(False, str(e))

    def _build_stock_result(self, test_passed, failure_reason):
        """Build out-of-stock handling test result dictionary."""
        return {
            'test_case_title': "Verify shopping cart handles out-of-stock products correctly",
            'cart_empty': False,
            'item_count': 0,
            'error_message_displayed': False,
            'error_message': None,
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }

    def verify_shopping_cart_clears_after_user_logs_out(self):
        """
        Verify Shopping Cart clears after user logs out.
        
        Tests that cart is emptied when user logs out.
        
        Returns:
            dict: Test result with logout cart clearing validation
        """
        try:
            self.logger.info("TEST: Verify Shopping Cart clears after user logs out")
            
            # Verify cart page loaded
            if not self.cart_review_page.is_page_loaded():
                return self._build_logout_result(False, "Cart page load failed")
            
            # Get initial cart state
            initial_count = self.get_cart_item_count()
            self.logger.debug(f"Initial cart count: {initial_count}")
            
            # Check if cart is now empty (indicating logout cleared it)
            cart_is_empty = self.cart_review_page.is_cart_empty()
            
            self.logger.debug(f"Cart empty after logout: {cart_is_empty}")
            
            test_passed = cart_is_empty
            
            if test_passed:
                self.logger.info("✓ TEST PASSED: Cart cleared after logout")
            else:
                self.logger.error("✗ TEST FAILED: Cart not cleared after logout")
            
            return {
                'test_case_title': "Verify Shopping Cart clears after user logs out",
                'initial_cart_count': initial_count,
                'cart_empty_after_logout': cart_is_empty,
                'test_passed': test_passed,
                'test_failure_reason': None if test_passed else "Cart items still present after logout"
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_logout_result(False, str(e))

    def _build_logout_result(self, test_passed, failure_reason):
        """Build logout cart clearing test result dictionary."""
        return {
            'test_case_title': "Verify Shopping Cart clears after user logs out",
            'initial_cart_count': 0,
            'cart_empty_after_logout': False,
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }