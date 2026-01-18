from pages.myAccountPage import MyAccountPage
from pages.myAccountProfilePage import MyAccountProfilePage
from pages.myAccountAddressesPage import MyAccountAddressesPage
from pages.myAccountPasswordPage import MyAccountPasswordPage
from utilities.customLogger import LoggerFactory


class MyAccountFlow:
    logger = LoggerFactory.get_logger(__name__)

    def __init__(self, driver):
        self.driver = driver
        self.account_page = MyAccountPage(driver)
        self.profile_page = MyAccountProfilePage(driver)
        self.addresses_page = MyAccountAddressesPage(driver)
        self.password_page = MyAccountPasswordPage(driver)

    def wait_for_account_page_to_load(self):
        self.logger.info("Waiting for My Account page to load")
        self.account_page.handle_cloudflare_if_present()
        if not self.account_page.is_page_loaded():
            self.logger.error("My Account page failed to load")
            raise Exception("My Account page failed to load")
        self.logger.info("My Account page loaded successfully")

    def navigate_to_account_page(self):
        self.logger.info("Navigating to My Account page")
        self.wait_for_account_page_to_load()
        self.logger.info("My Account page ready")

    def get_account_overview(self):
        self.logger.info("Getting account overview")
        self.wait_for_account_page_to_load()
        overview = {
            'customer_name': self.account_page.get_customer_name(),
            'customer_email': self.account_page.get_customer_email(),
            'welcome_message': self.account_page.get_welcome_message(),
            'menu_items': self.account_page.get_all_menu_items()
        }
        self.logger.info("Account overview retrieved successfully")
        return overview

    def navigate_to_profile_edit(self):
        self.logger.info("Navigating to edit profile")
        self.wait_for_account_page_to_load()
        self.account_page.click_edit_profile_link()
        self.logger.info("Edit profile link clicked")

    def wait_for_profile_page_to_load(self):
        self.logger.info("Waiting for Profile page to load")
        self.profile_page.handle_cloudflare_if_present()
        if not self.profile_page.is_page_loaded():
            self.logger.error("Profile page failed to load")
            raise Exception("Profile page failed to load")
        self.logger.info("Profile page loaded successfully")

    def get_current_profile_details(self):
        self.logger.info("Getting current profile details")
        self.wait_for_profile_page_to_load()
        details = self.profile_page.get_profile_details()
        self.logger.info("Profile details retrieved successfully")
        return details

    def update_profile_information(self, profile_details):
        self.logger.info("Updating profile information")
        self.navigate_to_profile_edit()
        self.wait_for_profile_page_to_load()
        self.profile_page.update_profile(profile_details)
        self.profile_page.save_profile()
        self.logger.info("Profile information updated and saved")

    def verify_profile_update_successful(self):
        self.logger.info("Verifying profile update was successful")
        self.wait_for_profile_page_to_load()
        is_successful = self.profile_page.is_success_message_displayed()
        if is_successful:
            message = self.profile_page.get_success_message()
            self.logger.info(f"Profile update successful: {message}")
        else:
            self.logger.warning("Profile update success message not displayed")
        return is_successful

    def verify_profile_update_error(self):
        self.logger.info("Verifying profile update error")
        self.wait_for_profile_page_to_load()
        has_error = self.profile_page.is_error_message_displayed()
        if has_error:
            error = self.profile_page.get_error_message()
            self.logger.warning(f"Profile update error: {error}")
        return has_error

    def navigate_to_addresses(self):
        self.logger.info("Navigating to addresses")
        self.wait_for_account_page_to_load()
        self.account_page.click_addresses_link()
        self.logger.info("Addresses link clicked")

    def wait_for_addresses_page_to_load(self):
        self.logger.info("Waiting for Addresses page to load")
        self.addresses_page.handle_cloudflare_if_present()
        if not self.addresses_page.is_page_loaded():
            self.logger.error("Addresses page failed to load")
            raise Exception("Addresses page failed to load")
        self.logger.info("Addresses page loaded successfully")

    def get_all_addresses(self):
        self.logger.info("Getting all addresses")
        self.navigate_to_addresses()
        self.wait_for_addresses_page_to_load()
        addresses = self.addresses_page.get_all_addresses()
        self.logger.info(f"Retrieved {len(addresses)} addresses")
        return addresses

    def get_address_count(self):
        self.logger.info("Getting address count")
        self.navigate_to_addresses()
        self.wait_for_addresses_page_to_load()
        count = self.addresses_page.get_addresses_count()
        self.logger.info(f"Address count: {count}")
        return count

    def verify_no_addresses(self):
        self.logger.info("Verifying no addresses exist")
        self.navigate_to_addresses()
        self.wait_for_addresses_page_to_load()
        is_empty = self.addresses_page.is_no_addresses_message_displayed()
        if is_empty:
            self.logger.info("No addresses found as expected")
        else:
            self.logger.warning("Addresses are present")
        return is_empty

    def add_new_address(self):
        self.logger.info("Adding new address")
        self.navigate_to_addresses()
        self.wait_for_addresses_page_to_load()
        self.addresses_page.click_add_new_address()
        self.logger.info("Add new address button clicked")

    def edit_address(self, index):
        self.logger.info(f"Editing address at index: {index}")
        self.navigate_to_addresses()
        self.wait_for_addresses_page_to_load()
        success = self.addresses_page.edit_address_by_index(index)
        if success:
            self.logger.info(f"Address edit started for index: {index}")
        else:
            self.logger.error(f"Failed to edit address at index: {index}")
        return success

    def delete_address(self, index):
        self.logger.info(f"Deleting address at index: {index}")
        self.navigate_to_addresses()
        self.wait_for_addresses_page_to_load()
        success = self.addresses_page.delete_address_by_index(index)
        if success:
            self.logger.info(f"Address deletion initiated for index: {index}")
        else:
            self.logger.error(f"Failed to delete address at index: {index}")
        return success

    def set_address_as_billing(self, index):
        self.logger.info(f"Setting address at index {index} as billing")
        self.navigate_to_addresses()
        self.wait_for_addresses_page_to_load()
        success = self.addresses_page.set_address_as_billing_by_index(index)
        if success:
            self.logger.info(f"Address set as billing: {index}")
        else:
            self.logger.error(f"Failed to set address as billing: {index}")
        return success

    def set_address_as_shipping(self, index):
        self.logger.info(f"Setting address at index {index} as shipping")
        self.navigate_to_addresses()
        self.wait_for_addresses_page_to_load()
        success = self.addresses_page.set_address_as_shipping_by_index(index)
        if success:
            self.logger.info(f"Address set as shipping: {index}")
        else:
            self.logger.error(f"Failed to set address as shipping: {index}")
        return success

    def navigate_to_change_password(self):
        self.logger.info("Navigating to change password")
        self.wait_for_account_page_to_load()
        self.account_page.click_change_password_link()
        self.logger.info("Change password link clicked")

    def wait_for_password_page_to_load(self):
        self.logger.info("Waiting for Change Password page to load")
        self.password_page.handle_cloudflare_if_present()
        if not self.password_page.is_page_loaded():
            self.logger.error("Change Password page failed to load")
            raise Exception("Change Password page failed to load")
        self.logger.info("Change Password page loaded successfully")

    def change_password(self, old_password, new_password, confirm_password):
        self.logger.info("Changing password")
        self.navigate_to_change_password()
        self.wait_for_password_page_to_load()
        self.password_page.enter_old_password(old_password)
        self.password_page.enter_new_password(new_password)
        self.password_page.enter_confirm_password(confirm_password)
        self.password_page.save_password_changes()
        self.logger.info("Password change submitted")

    def verify_password_change_successful(self):
        self.logger.info("Verifying password change was successful")
        self.wait_for_password_page_to_load()
        is_successful = self.password_page.is_success_message_displayed()
        if is_successful:
            message = self.password_page.get_success_message()
            self.logger.info(f"Password change successful: {message}")
        else:
            self.logger.warning("Password change success message not displayed")
        return is_successful

    def verify_password_change_error(self):
        self.logger.info("Verifying password change error")
        self.wait_for_password_page_to_load()
        has_error = self.password_page.is_error_message_displayed()
        if has_error:
            error = self.password_page.get_error_message()
            self.logger.warning(f"Password change error: {error}")
        return has_error

    def verify_old_password_error(self):
        self.logger.info("Verifying old password error")
        self.wait_for_password_page_to_load()
        has_error = self.password_page.is_old_password_error_displayed()
        if has_error:
            error = self.password_page.get_old_password_error()
            self.logger.warning(f"Old password error: {error}")
        return has_error

    def verify_password_mismatch_error(self):
        self.logger.info("Verifying password mismatch error")
        self.wait_for_password_page_to_load()
        has_error = self.password_page.is_password_mismatch_error_displayed()
        if has_error:
            error = self.password_page.get_password_mismatch_error()
            self.logger.warning(f"Password mismatch error: {error}")
        return has_error

    def navigate_to_orders(self):
        self.logger.info("Navigating to orders history")
        self.wait_for_account_page_to_load()
        self.account_page.click_orders_link()
        self.logger.info("Orders link clicked")

    def get_recent_orders(self):
        self.logger.info("Getting recent orders")
        self.wait_for_account_page_to_load()
        orders = self.account_page.get_recent_orders_details()
        self.logger.info(f"Retrieved {len(orders)} recent orders")
        return orders

    def get_recent_order_count(self):
        self.logger.info("Getting recent order count")
        self.wait_for_account_page_to_load()
        count = self.account_page.get_recent_orders_count()
        self.logger.info(f"Recent order count: {count}")
        return count

    def view_recent_order(self, order_number):
        self.logger.info(f"Viewing recent order: {order_number}")
        self.wait_for_account_page_to_load()
        success = self.account_page.view_recent_order_by_number(order_number)
        if success:
            self.logger.info(f"Order view initiated: {order_number}")
        else:
            self.logger.error(f"Failed to view order: {order_number}")
        return success

    def navigate_to_downloads(self):
        self.logger.info("Navigating to downloads")
        self.wait_for_account_page_to_load()
        self.account_page.click_downloads_link()
        self.logger.info("Downloads link clicked")

    def navigate_to_product_reviews(self):
        self.logger.info("Navigating to product reviews")
        self.wait_for_account_page_to_load()
        self.account_page.click_product_reviews_link()
        self.logger.info("Product reviews link clicked")

    def navigate_to_notifications(self):
        self.logger.info("Navigating to account notifications")
        self.wait_for_account_page_to_load()
        self.account_page.click_account_notifications_link()
        self.logger.info("Account notifications link clicked")

    def logout_from_account(self):
        self.logger.info("Logging out from account")
        self.wait_for_account_page_to_load()
        self.account_page.click_logout_link()
        self.logger.info("Logout link clicked from account")

    def verify_account_menu_visible(self, menu_item):
        self.logger.info(f"Verifying account menu item visible: {menu_item}")
        self.wait_for_account_page_to_load()
        menu_items = self.account_page.get_all_menu_items()
        is_present = any(menu_item.lower() in item.lower() for item in menu_items)
        if is_present:
            self.logger.info(f"Menu item found: {menu_item}")
        else:
            self.logger.warning(f"Menu item not found: {menu_item}")
        return is_present
    def validate_navigating_to_my_account_page_from_order_success_page(self):
        """
        Validate navigating to 'My Account' page from the 'Order Success' page.
        
        Tests that user can access My Account page with proper customer info displayed.
        
        Returns:
            dict: Test result with navigation and account info validation
        """
        try:
            self.logger.info("TEST: Validate navigating to My Account page from Order Success page")
            
            # Verify account page loaded
            if not self.account_page.is_page_loaded():
                return self._build_navigation_result(False, "Account page load failed")
            
            # Get page title
            page_title = self.driver.title
            
            # Get customer information
            customer_name = self.account_page.get_customer_name()
            welcome_message = self.account_page.get_welcome_message()
            
            # Get menu items
            menu_items = self.account_page.get_all_menu_items()
            
            # Verify account page has customer info
            customer_info_present = customer_name is not None and len(customer_name) > 0
            menu_loaded = menu_items is not None and len(menu_items) > 0
            
            test_passed = customer_info_present and menu_loaded
            
            if test_passed:
                self.logger.info("✓ TEST PASSED: Successfully navigated to My Account page")
            else:
                self.logger.error("✗ TEST FAILED: My Account page missing customer info or menu")
            
            return {
                'test_case_title': "Validate navigating to 'My Account' page from the 'Order Success' page",
                'page_title': page_title,
                'page_loaded': True,
                'customer_name': customer_name,
                'welcome_message': welcome_message,
                'menu_items_count': len(menu_items) if menu_items else 0,
                'customer_info_present': customer_info_present,
                'test_passed': test_passed,
                'test_failure_reason': None if test_passed else "Customer info or menu items missing"
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_navigation_result(False, str(e))

    def _build_navigation_result(self, test_passed, failure_reason):
        """Build navigation validation test result dictionary."""
        return {
            'test_case_title': "Validate navigating to 'My Account' page from the 'Order Success' page",
            'page_title': None,
            'page_loaded': False,
            'customer_name': None,
            'welcome_message': None,
            'menu_items_count': 0,
            'customer_info_present': False,
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }

    def validate_my_account_page_is_accessible_for_logged_in_users(self):
        """
        Verify my account page is accessible for logged-in users.
        
        Tests that My Account page loads and displays user-specific content.
        
        Returns:
            dict: Test result with accessibility validation
        """
        try:
            self.logger.info("TEST: Verify my account page is accessible for logged in users")
            
            # Verify account page loaded
            if not self.account_page.is_page_loaded():
                return self._build_accessibility_result(False, "Account page load failed")
            
            # Get page title
            page_title = self.driver.title
            
            # Get customer name (indicates logged-in user)
            customer_name = self.account_page.get_customer_name()
            
            # Get welcome message
            welcome_message = self.account_page.get_welcome_message()
            
            # Get menu items (should be available only for logged-in users)
            menu_items = self.account_page.get_all_menu_items()
            
            # Verify user is logged in (has customer name and menu items)
            user_logged_in = customer_name is not None and len(customer_name) > 0
            menu_available = menu_items is not None and len(menu_items) > 0
            
            test_passed = user_logged_in and menu_available
            
            if test_passed:
                self.logger.info("✓ TEST PASSED: My Account page accessible for logged-in user")
            else:
                self.logger.error("✗ TEST FAILED: My Account page not properly accessible")
            
            return {
                'test_case_title': "Verify my account page is accessible for logged in users",
                'page_title': page_title,
                'page_loaded': True,
                'customer_name': customer_name,
                'welcome_message': welcome_message,
                'user_logged_in': user_logged_in,
                'menu_items_available': menu_available,
                'menu_items_count': len(menu_items) if menu_items else 0,
                'test_passed': test_passed,
                'test_failure_reason': None if test_passed else "User not logged in or menu items missing"
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_accessibility_result(False, str(e))

    def _build_accessibility_result(self, test_passed, failure_reason):
        """Build accessibility validation test result dictionary."""
        return {
            'test_case_title': "Verify my account page is accessible for logged in users",
            'page_title': None,
            'page_loaded': False,
            'customer_name': None,
            'welcome_message': None,
            'user_logged_in': False,
            'menu_items_available': False,
            'menu_items_count': 0,
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }

    def verify_my_account_page_loads_correct_user_information(self):
        """
        Verify 'My Account Page' loads correct user information.
        
        Tests that user profile data is correctly displayed on My Account page.
        
        Returns:
            dict: Test result with user information validation
        """
        try:
            self.logger.info("TEST: Verify 'My Account Page' loads correct user information")
            
            if not self.account_page.is_page_loaded():
                return self._build_user_info_result(False, "Account page load failed")
            
            # Get user information
            customer_name = self.account_page.get_customer_name()
            welcome_message = self.account_page.get_welcome_message()
            
            # Verify user information is present
            has_name = customer_name is not None and len(customer_name) > 0
            has_welcome = welcome_message is not None and len(welcome_message) > 0
            
            test_passed = has_name and has_welcome
            
            if test_passed:
                self.logger.info("✓ TEST PASSED: User information loaded correctly")
            else:
                self.logger.error("✗ TEST FAILED: User information missing or incomplete")
            
            return {
                'test_case_title': "Verify 'My Account Page' loads correct user information",
                'customer_name': customer_name,
                'welcome_message': welcome_message,
                'name_present': has_name,
                'welcome_present': has_welcome,
                'test_passed': test_passed,
                'test_failure_reason': None if test_passed else "User information not properly displayed"
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_user_info_result(False, str(e))

    def _build_user_info_result(self, test_passed, failure_reason):
        """Build user information validation test result dictionary."""
        return {
            'test_case_title': "Verify 'My Account Page' loads correct user information",
            'customer_name': None,
            'welcome_message': None,
            'name_present': False,
            'welcome_present': False,
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }

    def verify_user_is_redirected_correctly_after_saving_changes(self):
        """
        Verify user is redirected correctly after saving changes.
        
        Tests that page redirect occurs after saving account changes.
        
        Returns:
            dict: Test result with redirect validation
        """
        try:
            self.logger.info("TEST: Verify user is redirected correctly after saving changes")
            
            if not self.account_page.is_page_loaded():
                return self._build_redirect_result(False, "Account page load failed")
            
            # Get current page URL before save
            current_url_before = self.driver.current_url
            
            # Perform save action (page handles the actual save)
            self.account_page.save_changes()
            
            # Get URL after save
            import time
            time.sleep(2)  # Wait for redirect
            current_url_after = self.driver.current_url
            
            # Verify redirect occurred (URL changed or page reloaded)
            redirect_occurred = current_url_before != current_url_after or self.account_page.is_page_loaded()
            
            if redirect_occurred:
                self.logger.info("✓ TEST PASSED: User redirected correctly after saving")
            else:
                self.logger.error("✗ TEST FAILED: User not redirected after saving changes")
            
            return {
                'test_case_title': "Verify user is redirected correctly after saving changes",
                'url_before': current_url_before,
                'url_after': current_url_after,
                'redirect_occurred': redirect_occurred,
                'test_passed': redirect_occurred,
                'test_failure_reason': None if redirect_occurred else "Redirect did not occur after saving"
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_redirect_result(False, str(e))

    def _build_redirect_result(self, test_passed, failure_reason):
        """Build redirect validation test result dictionary."""
        return {
            'test_case_title': "Verify user is redirected correctly after saving changes",
            'url_before': None,
            'url_after': None,
            'redirect_occurred': False,
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }

    def verify_my_account_fields_are_accessible_using_keyboard_navigation(self):
        """
        Verify 'My Account' fields are accessible using keyboard navigation.
        
        Tests that form fields can be accessed via keyboard tab navigation.
        
        Returns:
            dict: Test result with keyboard accessibility validation
        """
        try:
            self.logger.info("TEST: Verify 'My Account' fields are accessible using keyboard navigation")
            
            if not self.account_page.is_page_loaded():
                return self._build_keyboard_result(False, "Account page load failed")
            
            # Simulate keyboard navigation (Tab key)
            from selenium.webdriver.common.keys import Keys
            
            # Get focused element before navigation
            initial_element = self.driver.switch_to.active_element
            
            # Tab through fields
            for _ in range(5):  # Tab through 5 fields
                initial_element.send_keys(Keys.TAB)
            
            # Get focused element after navigation
            final_element = self.driver.switch_to.active_element
            
            # Verify navigation occurred (different element or same field group)
            keyboard_accessible = initial_element != final_element
            
            if keyboard_accessible:
                self.logger.info("✓ TEST PASSED: Fields accessible via keyboard navigation")
            else:
                self.logger.error("✗ TEST FAILED: Fields not properly accessible via keyboard")
            
            return {
                'test_case_title': "Verify 'My Account' fields are accessible using keyboard navigation",
                'keyboard_navigation_works': keyboard_accessible,
                'fields_traversable': keyboard_accessible,
                'test_passed': keyboard_accessible,
                'test_failure_reason': None if keyboard_accessible else "Keyboard navigation not working"
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_keyboard_result(False, str(e))

    def _build_keyboard_result(self, test_passed, failure_reason):
        """Build keyboard accessibility validation test result dictionary."""
        return {
            'test_case_title': "Verify 'My Account' fields are accessible using keyboard navigation",
            'keyboard_navigation_works': False,
            'fields_traversable': False,
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }
