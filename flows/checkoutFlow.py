from pages.checkoutPage import CheckoutPage
from utilities.customLogger import LoggerFactory


class CheckoutFlow:
    logger = LoggerFactory.get_logger(__name__)

    def __init__(self, driver):
        self.driver = driver
        self.checkout_page = CheckoutPage(driver)

    def wait_for_checkout_page_to_load(self):
        self.logger.info("Waiting for Checkout page to load")
        self.checkout_page.handle_cloudflare_if_present()
        if not self.checkout_page.is_page_loaded():
            self.logger.error("Checkout page failed to load")
            raise Exception("Checkout page failed to load")
        self.logger.info("Checkout page loaded successfully")

    def enter_billing_address(self, billing_details):
        self.logger.info("Entering billing address details")
        self.wait_for_checkout_page_to_load()
        self.checkout_page.select_new_billing_address()
        if 'first_name' in billing_details:
            self.checkout_page.enter_billing_first_name(billing_details['first_name'])
        if 'last_name' in billing_details:
            self.checkout_page.enter_billing_last_name(billing_details['last_name'])
        if 'email' in billing_details:
            self.checkout_page.enter_billing_email(billing_details['email'])
        if 'phone' in billing_details:
            self.checkout_page.enter_billing_phone(billing_details['phone'])
        if 'company' in billing_details:
            self.checkout_page.enter_billing_company(billing_details['company'])
        if 'country' in billing_details:
            self.checkout_page.select_billing_country(billing_details['country'])
        if 'state' in billing_details:
            self.checkout_page.select_billing_state(billing_details['state'])
        if 'city' in billing_details:
            self.checkout_page.enter_billing_city(billing_details['city'])
        if 'address1' in billing_details:
            self.checkout_page.enter_billing_address1(billing_details['address1'])
        if 'address2' in billing_details:
            self.checkout_page.enter_billing_address2(billing_details['address2'])
        if 'postal_code' in billing_details:
            self.checkout_page.enter_billing_postal_code(billing_details['postal_code'])
        self.logger.info("Billing address details entered successfully")

    def use_existing_billing_address(self, address_id):
        self.logger.info(f"Using existing billing address: {address_id}")
        self.wait_for_checkout_page_to_load()
        success = self.checkout_page.select_billing_address_from_dropdown(address_id)
        if success:
            self.logger.info(f"Existing billing address selected: {address_id}")
        else:
            self.logger.error(f"Failed to select existing billing address: {address_id}")
        return success

    def proceed_from_billing_address(self):
        self.logger.info("Proceeding from billing address section")
        self.wait_for_checkout_page_to_load()
        self.checkout_page.continue_from_billing_address()
        self.logger.info("Proceeding from billing address")

    def enter_shipping_address_same_as_billing(self):
        self.logger.info("Using shipping address same as billing")
        self.wait_for_checkout_page_to_load()
        self.checkout_page.check_shipping_same_as_billing()
        self.logger.info("Shipping address set to same as billing")

    def enter_different_shipping_address(self, shipping_details):
        self.logger.info("Entering different shipping address")
        self.wait_for_checkout_page_to_load()
        self.checkout_page.uncheck_shipping_same_as_billing()
        if 'first_name' in shipping_details:
            self.checkout_page.enter_shipping_first_name(shipping_details['first_name'])
        if 'last_name' in shipping_details:
            self.checkout_page.enter_shipping_last_name(shipping_details['last_name'])
        if 'email' in shipping_details:
            self.checkout_page.enter_shipping_email(shipping_details['email'])
        if 'phone' in shipping_details:
            self.checkout_page.enter_shipping_phone(shipping_details['phone'])
        if 'company' in shipping_details:
            self.checkout_page.enter_shipping_company(shipping_details['company'])
        if 'country' in shipping_details:
            self.checkout_page.select_shipping_country(shipping_details['country'])
        if 'state' in shipping_details:
            self.checkout_page.select_shipping_state(shipping_details['state'])
        if 'city' in shipping_details:
            self.checkout_page.enter_shipping_city(shipping_details['city'])
        if 'address1' in shipping_details:
            self.checkout_page.enter_shipping_address1(shipping_details['address1'])
        if 'address2' in shipping_details:
            self.checkout_page.enter_shipping_address2(shipping_details['address2'])
        if 'postal_code' in shipping_details:
            self.checkout_page.enter_shipping_postal_code(shipping_details['postal_code'])
        self.logger.info("Shipping address details entered successfully")

    def proceed_from_shipping_address(self):
        self.logger.info("Proceeding from shipping address section")
        self.wait_for_checkout_page_to_load()
        self.checkout_page.continue_from_shipping_address()
        self.logger.info("Proceeding from shipping address")

    def select_shipping_method(self, method_value):
        self.logger.info(f"Selecting shipping method: {method_value}")
        self.wait_for_checkout_page_to_load()
        success = self.checkout_page.select_shipping_method(method_value)
        if success:
            self.logger.info(f"Shipping method selected: {method_value}")
        else:
            self.logger.error(f"Failed to select shipping method: {method_value}")
        return success

    def proceed_from_shipping_method(self):
        self.logger.info("Proceeding from shipping method section")
        self.wait_for_checkout_page_to_load()
        self.checkout_page.continue_from_shipping_method()
        self.logger.info("Proceeding from shipping method")

    def select_payment_method(self, method_value):
        self.logger.info(f"Selecting payment method: {method_value}")
        self.wait_for_checkout_page_to_load()
        success = self.checkout_page.select_payment_method(method_value)
        if success:
            self.logger.info(f"Payment method selected: {method_value}")
        else:
            self.logger.error(f"Failed to select payment method: {method_value}")
        return success

    def proceed_from_payment_method(self):
        self.logger.info("Proceeding from payment method section")
        self.wait_for_checkout_page_to_load()
        self.checkout_page.continue_from_payment_method()
        self.logger.info("Proceeding from payment method")

    def verify_order_review_visible(self):
        self.logger.info("Verifying order review is visible")
        self.wait_for_checkout_page_to_load()
        is_visible = self.checkout_page.is_order_review_visible()
        if is_visible:
            self.logger.info("Order review is visible")
        else:
            self.logger.warning("Order review is not visible")
        return is_visible

    def get_order_total_before_confirmation(self):
        self.logger.info("Getting order total before confirmation")
        self.wait_for_checkout_page_to_load()
        total = self.checkout_page.get_order_total()
        if total:
            self.logger.info(f"Order total: {total}")
        else:
            self.logger.warning("Could not retrieve order total")
        return total

    def place_order(self):
        self.logger.info("Placing order")
        self.wait_for_checkout_page_to_load()
        self.checkout_page.confirm_order()
        self.logger.info("Order confirmation submitted")

    def verify_checkout_error(self):
        self.logger.info("Verifying checkout error message")
        self.wait_for_checkout_page_to_load()
        has_error = self.checkout_page.is_error_message_displayed()
        if has_error:
            error_msg = self.checkout_page.get_error_message()
            self.logger.warning(f"Checkout error: {error_msg}")
        return has_error

    def get_checkout_error_message(self):
        self.logger.info("Getting checkout error message")
        self.wait_for_checkout_page_to_load()
        error_msg = self.checkout_page.get_error_message()
        if error_msg:
            self.logger.warning(f"Error: {error_msg}")
        return error_msg

    def complete_checkout_with_billing_and_shipping(self, billing_details, shipping_details, shipping_method, payment_method):
        self.logger.info("Completing full checkout workflow")
        self.enter_billing_address(billing_details)
        self.proceed_from_billing_address()
        self.enter_different_shipping_address(shipping_details)
        self.proceed_from_shipping_address()
        self.select_shipping_method(shipping_method)
        self.proceed_from_shipping_method()
        self.select_payment_method(payment_method)
        self.proceed_from_payment_method()
        self.verify_order_review_visible()
        self.logger.info("Full checkout workflow completed successfully")

    def complete_checkout_with_same_shipping_address(self, billing_details, shipping_method, payment_method):
        self.logger.info("Completing checkout with same billing and shipping address")
        self.enter_billing_address(billing_details)
        self.proceed_from_billing_address()
        self.enter_shipping_address_same_as_billing()
        self.proceed_from_shipping_address()
        self.select_shipping_method(shipping_method)
        self.proceed_from_shipping_method()
        self.select_payment_method(payment_method)
        self.proceed_from_payment_method()
        self.verify_order_review_visible()
        self.logger.info("Checkout with same billing and shipping address completed successfully")

    def get_checkout_cart_summary(self):
        self.logger.info("Getting checkout cart summary")
        self.wait_for_checkout_page_to_load()
        summary = self.checkout_page.get_cart_summary()
        if summary:
            self.logger.info("Cart summary retrieved successfully")
        else:
            self.logger.warning("Could not retrieve cart summary")
        return summary

    def go_back_from_checkout(self):
        self.logger.info("Going back from checkout")
        self.wait_for_checkout_page_to_load()
        self.checkout_page.click_back_button()
        self.logger.info("Checkout cancelled - went back")

    def complete_checkout_and_place_order(self, billing_details, shipping_details, shipping_method, payment_method):
        self.logger.info("Completing full checkout and placing order")
        self.complete_checkout_with_billing_and_shipping(billing_details, shipping_details, shipping_method, payment_method)
        self.place_order()
        self.logger.info("Order placed successfully")
    def validate_navigating_to_checkout_page_when_no_products_in_cart(self):
        """
        Validate navigating to checkout page when there are no products added to the Shopping Cart.
        
        Tests that checkout page handles empty cart appropriately with error message or warning.
        
        Returns:
            dict: Test result with empty cart validation
        """
        try:
            self.logger.info("TEST: Validate navigating to checkout page when there are no products in cart")
            
            # Verify checkout page loaded
            if not self.checkout_page.is_page_loaded():
                return self._build_empty_cart_result(False, "Checkout page load failed")
            
            # Get page title
            page_title = self.driver.title
            
            # Check for error message (empty cart warning)
            error_displayed = self.checkout_page.is_error_message_displayed()
            error_msg = self.checkout_page.get_error_message() if error_displayed else None
            
            # Get cart summary
            cart_summary = self.checkout_page.get_cart_summary()
            
            # Test passes if page loaded AND error displayed OR cart empty
            test_passed = error_displayed or (cart_summary is None or len(cart_summary) == 0)
            
            if test_passed:
                self.logger.info("✓ TEST PASSED: Empty cart properly handled on checkout page")
            else:
                self.logger.error("✗ TEST FAILED: Empty cart not properly handled")
            
            return {
                'test_case_title': "Validate navigating to checkout page when there are no products added to the Shopping Cart",
                'page_title': page_title,
                'page_loaded': True,
                'error_displayed': error_displayed,
                'error_message': error_msg,
                'cart_empty': cart_summary is None or len(cart_summary) == 0,
                'test_passed': test_passed,
                'test_failure_reason': None if test_passed else "Empty cart not properly handled on checkout page"
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_empty_cart_result(False, str(e))

    def _build_empty_cart_result(self, test_passed, failure_reason):
        """Build empty cart validation test result dictionary."""
        return {
            'test_case_title': "Validate navigating to checkout page when there are no products added to the Shopping Cart",
            'page_title': None,
            'page_loaded': False,
            'error_displayed': False,
            'error_message': None,
            'cart_empty': False,
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }

    def verify_checkout_page_opens_with_items_present_in_shopping_cart(self):
        """
        Verify Checkout page opens with items present in Shopping Cart.
        
        Tests that checkout page loads successfully with cart items available.
        
        Returns:
            dict: Test result with cart items presence validation
        """
        try:
            self.logger.info("TEST: Verify Checkout page opens with items present in Shopping Cart")
            
            # Verify checkout page loaded
            if not self.checkout_page.is_page_loaded():
                return self._build_items_present_result(False, "Checkout page load failed")
            
            # Get page title
            page_title = self.driver.title
            
            # Get cart summary
            cart_summary = self.checkout_page.get_cart_summary()
            
            # Verify cart has items
            cart_has_items = cart_summary is not None and len(cart_summary) > 0
            
            # Check no error message (cart should not be empty)
            no_error = not self.checkout_page.is_error_message_displayed()
            
            test_passed = cart_has_items and no_error
            
            if test_passed:
                self.logger.info("✓ TEST PASSED: Checkout page opened with items in cart")
            else:
                self.logger.error("✗ TEST FAILED: Checkout page missing cart items or showing error")
            
            return {
                'test_case_title': "Verify Checkout page opens with items present in Shopping Cart",
                'page_title': page_title,
                'page_loaded': True,
                'cart_has_items': cart_has_items,
                'cart_items_count': len(cart_summary) if cart_summary else 0,
                'error_displayed': not no_error,
                'test_passed': test_passed,
                'test_failure_reason': None if test_passed else "Checkout page missing items or error displayed"
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_items_present_result(False, str(e))

    def _build_items_present_result(self, test_passed, failure_reason):
        """Build items present test result dictionary."""
        return {
            'test_case_title': "Verify Checkout page opens with items present in Shopping Cart",
            'page_title': None,
            'page_loaded': False,
            'cart_has_items': False,
            'cart_items_count': 0,
            'error_displayed': False,
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }
    def verify_checkout_rejects_missing_mandatory_billing_fields(self):
        """
        Verify Checkout rejects missing mandatory billing fields.
        
        Tests that checkout shows error when mandatory billing fields are empty.
        
        Returns:
            dict: Test result with mandatory field validation
        """
        try:
            self.logger.info("TEST: Verify Checkout rejects missing mandatory billing fields")
            
            # Verify checkout page loaded
            if not self.checkout_page.is_page_loaded():
                return self._build_mandatory_fields_result(False, "Checkout page load failed")
            
            # Attempt to proceed from billing address without filling fields
            # The page should reject and show error
            self.checkout_page.continue_from_billing_address()
            self.logger.debug("Attempted to continue without filling mandatory fields")
            
            # Check if error message is displayed
            error_displayed = self.checkout_page.is_error_message_displayed()
            error_msg = self.checkout_page.get_error_message() if error_displayed else None
            
            test_passed = error_displayed
            
            if test_passed:
                self.logger.info("✓ TEST PASSED: Checkout rejected missing mandatory fields")
            else:
                self.logger.error("✗ TEST FAILED: Checkout did not reject missing mandatory fields")
            
            return {
                'test_case_title': "Verify Checkout rejects missing mandatory billing fields",
                'page_loaded': True,
                'error_displayed': error_displayed,
                'error_message': error_msg,
                'mandatory_fields_validated': error_displayed,
                'test_passed': test_passed,
                'test_failure_reason': None if test_passed else "Missing mandatory fields not rejected"
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_mandatory_fields_result(False, str(e))

    def _build_mandatory_fields_result(self, test_passed, failure_reason):
        """Build mandatory fields validation test result dictionary."""
        return {
            'test_case_title': "Verify Checkout rejects missing mandatory billing fields",
            'page_loaded': False,
            'error_displayed': False,
            'error_message': None,
            'mandatory_fields_validated': False,
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }

    def verify_checkout_redirects_correctly_after_order_completion(self):
        """
        Verify Checkout redirects correctly after order completion.
        
        Tests that after order placement, page redirects to confirmation/success page.
        
        Returns:
            dict: Test result with redirect validation
        """
        try:
            self.logger.info("TEST: Verify Checkout redirects correctly after order completion")
            
            # Verify checkout page loaded
            if not self.checkout_page.is_page_loaded():
                return self._build_redirect_result(False, "Checkout page load failed")
            
            # Get initial URL before placing order
            initial_url = self.driver.current_url
            
            # Place the order
            self.place_order()
            self.logger.debug("Order placed")
            
            # Get final URL after redirect
            final_url = self.driver.current_url
            
            # Check if URL changed (redirect occurred)
            url_changed = initial_url != final_url
            
            # Check if confirmation page or success indicator is visible
            confirmation_visible = self.checkout_page.is_order_review_visible()
            
            # Test passes if URL changed or confirmation is visible
            test_passed = url_changed or confirmation_visible
            
            if test_passed:
                self.logger.info("✓ TEST PASSED: Checkout redirected correctly after order completion")
            else:
                self.logger.error("✗ TEST FAILED: Checkout did not redirect after order completion")
            
            return {
                'test_case_title': "Verify Checkout redirects correctly after order completion",
                'page_loaded': True,
                'initial_url': initial_url,
                'final_url': final_url,
                'url_changed': url_changed,
                'confirmation_visible': confirmation_visible,
                'test_passed': test_passed,
                'test_failure_reason': None if test_passed else "Page did not redirect after order completion"
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_redirect_result(False, str(e))

    def _build_redirect_result(self, test_passed, failure_reason):
        """Build redirect validation test result dictionary."""
        return {
            'test_case_title': "Verify Checkout redirects correctly after order completion",
            'page_loaded': False,
            'initial_url': None,
            'final_url': None,
            'url_changed': False,
            'confirmation_visible': False,
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }
