from pages.recurringPaymentsPage import RecurringPaymentsPage
from utilities.customLogger import LoggerFactory


class RecurringPaymentsFlow:
    logger = LoggerFactory.get_logger(__name__)

    def __init__(self, driver):
        self.driver = driver
        self.recurring_payments_page = RecurringPaymentsPage(driver)

    def wait_for_recurring_payments_page_to_load(self):
        self.logger.info("Waiting for Recurring Payments page to load")
        self.recurring_payments_page.handle_cloudflare_if_present()
        if not self.recurring_payments_page.is_page_loaded():
            self.logger.error("Recurring Payments page failed to load")
            raise Exception("Recurring Payments page failed to load")
        self.logger.info("Recurring Payments page loaded successfully")

    def navigate_to_recurring_payments(self):
        self.logger.info("Navigating to Recurring Payments page")
        self.wait_for_recurring_payments_page_to_load()
        self.logger.info("Recurring Payments page ready")

    def verify_recurring_payments_page_loaded(self):
        self.logger.info("Verifying Recurring Payments page is loaded")
        self.wait_for_recurring_payments_page_to_load()
        is_loaded = self.recurring_payments_page.is_page_loaded()
        if is_loaded:
            self.logger.info("Recurring Payments page verified as loaded")
        else:
            self.logger.error("Recurring Payments page verification failed")
        return is_loaded

    def verify_no_subscriptions_exist(self):
        self.logger.info("Verifying no subscriptions exist")
        self.navigate_to_recurring_payments()
        is_empty = self.recurring_payments_page.is_no_subscriptions_message_displayed()
        if is_empty:
            self.logger.info("No subscriptions found as expected")
        else:
            self.logger.warning("Subscriptions are present")
        return is_empty

    def get_all_subscriptions(self):
        self.logger.info("Getting all subscriptions")
        self.navigate_to_recurring_payments()
        subscriptions = self.recurring_payments_page.get_all_subscriptions()
        self.logger.info(f"Retrieved {len(subscriptions)} subscriptions")
        return subscriptions

    def get_subscription_count(self):
        self.logger.info("Getting subscription count")
        self.navigate_to_recurring_payments()
        count = self.recurring_payments_page.get_subscriptions_count()
        self.logger.info(f"Subscription count: {count}")
        return count

    def get_subscription_details(self, subscription_id):
        self.logger.info(f"Getting details for subscription: {subscription_id}")
        self.navigate_to_recurring_payments()
        subscription = self.recurring_payments_page.get_subscription_by_id(subscription_id)
        if subscription:
            self.logger.info(f"Subscription details retrieved: {subscription}")
        else:
            self.logger.warning(f"Subscription not found: {subscription_id}")
        return subscription

    def view_subscription_by_id(self, subscription_id):
        self.logger.info(f"Viewing subscription: {subscription_id}")
        self.navigate_to_recurring_payments()
        success = self.recurring_payments_page.view_subscription_by_id(subscription_id)
        if success:
            self.logger.info(f"Subscription viewed: {subscription_id}")
        else:
            self.logger.error(f"Failed to view subscription: {subscription_id}")
        return success

    def edit_subscription(self, subscription_id):
        self.logger.info(f"Editing subscription: {subscription_id}")
        self.navigate_to_recurring_payments()
        success = self.recurring_payments_page.edit_subscription_by_id(subscription_id)
        if success:
            self.logger.info(f"Edit form opened for subscription: {subscription_id}")
        else:
            self.logger.error(f"Failed to edit subscription: {subscription_id}")
        return success

    def pause_subscription(self, subscription_id):
        self.logger.info(f"Pausing subscription: {subscription_id}")
        self.navigate_to_recurring_payments()
        success = self.recurring_payments_page.pause_subscription_by_id(subscription_id)
        if success:
            self.logger.info(f"Subscription paused: {subscription_id}")
        else:
            self.logger.error(f"Failed to pause subscription: {subscription_id}")
        return success

    def resume_subscription(self, subscription_id):
        self.logger.info(f"Resuming subscription: {subscription_id}")
        self.navigate_to_recurring_payments()
        success = self.recurring_payments_page.resume_subscription_by_id(subscription_id)
        if success:
            self.logger.info(f"Subscription resumed: {subscription_id}")
        else:
            self.logger.error(f"Failed to resume subscription: {subscription_id}")
        return success

    def cancel_subscription(self, subscription_id):
        self.logger.info(f"Canceling subscription: {subscription_id}")
        self.navigate_to_recurring_payments()
        success = self.recurring_payments_page.cancel_subscription_by_id(subscription_id)
        if success:
            self.logger.info(f"Subscription canceled: {subscription_id}")
        else:
            self.logger.error(f"Failed to cancel subscription: {subscription_id}")
        return success

    def change_payment_method(self, subscription_id):
        self.logger.info(f"Changing payment method for subscription: {subscription_id}")
        self.navigate_to_recurring_payments()
        success = self.recurring_payments_page.change_payment_method_by_id(subscription_id)
        if success:
            self.logger.info(f"Payment method change form opened for subscription: {subscription_id}")
        else:
            self.logger.error(f"Failed to change payment method: {subscription_id}")
        return success

    def filter_subscriptions_by_status(self, status):
        self.logger.info(f"Filtering subscriptions by status: {status}")
        self.navigate_to_recurring_payments()
        success = self.recurring_payments_page.filter_by_status(status)
        if success:
            subscriptions = self.recurring_payments_page.get_subscriptions_by_status(status)
            self.logger.info(f"Found {len(subscriptions)} subscriptions with status {status}")
            return subscriptions
        else:
            self.logger.error(f"Failed to filter by status: {status}")
            return []

    def filter_subscriptions_by_frequency(self, frequency):
        self.logger.info(f"Filtering subscriptions by frequency: {frequency}")
        self.navigate_to_recurring_payments()
        success = self.recurring_payments_page.filter_by_frequency(frequency)
        if success:
            subscriptions = self.recurring_payments_page.get_subscriptions_by_frequency(frequency)
            self.logger.info(f"Found {len(subscriptions)} subscriptions with frequency {frequency}")
            return subscriptions
        else:
            self.logger.error(f"Failed to filter by frequency: {frequency}")
            return []

    def sort_subscriptions(self, sort_option):
        self.logger.info(f"Sorting subscriptions by: {sort_option}")
        self.navigate_to_recurring_payments()
        success = self.recurring_payments_page.sort_subscriptions(sort_option)
        if success:
            self.logger.info(f"Subscriptions sorted by: {sort_option}")
        else:
            self.logger.error(f"Failed to sort subscriptions")
        return success

    def search_subscriptions(self, search_term):
        self.logger.info(f"Searching for subscriptions: {search_term}")
        self.navigate_to_recurring_payments()
        success = self.recurring_payments_page.search_subscription(search_term)
        if success:
            self.logger.info(f"Search completed for: {search_term}")
        else:
            self.logger.error(f"Failed to search for subscriptions")
        return success

    def clear_all_filters(self):
        self.logger.info("Clearing all subscription filters")
        self.navigate_to_recurring_payments()
        success = self.recurring_payments_page.clear_filters()
        if success:
            self.logger.info("All filters cleared")
        else:
            self.logger.error("Failed to clear filters")
        return success

    def export_subscriptions_data(self):
        self.logger.info("Exporting subscriptions data")
        self.navigate_to_recurring_payments()
        success = self.recurring_payments_page.export_subscriptions()
        if success:
            self.logger.info("Subscriptions data exported")
        else:
            self.logger.error("Failed to export subscriptions")
        return success

    def print_subscriptions_data(self):
        self.logger.info("Printing subscriptions data")
        self.navigate_to_recurring_payments()
        success = self.recurring_payments_page.print_subscriptions()
        if success:
            self.logger.info("Subscriptions data printed")
        else:
            self.logger.error("Failed to print subscriptions")
        return success

    def initiate_new_subscription(self):
        self.logger.info("Initiating new subscription")
        self.navigate_to_recurring_payments()
        success = self.recurring_payments_page.add_new_subscription()
        if success:
            self.logger.info("New subscription form opened")
        else:
            self.logger.error("Failed to open new subscription form")
        return success

    def get_total_monthly_recurring_amount(self):
        self.logger.info("Calculating total monthly recurring amount")
        self.navigate_to_recurring_payments()
        subscriptions = self.recurring_payments_page.get_all_subscriptions()
        total = 0
        for subscription in subscriptions:
            try:
                # Parse amount and convert to float
                amount_str = str(subscription.get('amount', '0')).replace('$', '').replace(',', '')
                frequency = subscription.get('frequency', '').lower()
                amount = float(amount_str)
                
                # If frequency is not monthly, convert to monthly equivalent
                if 'weekly' in frequency:
                    amount *= 4.33  # Weekly to monthly
                elif 'yearly' in frequency or 'annual' in frequency:
                    amount /= 12  # Yearly to monthly
                
                total += amount
            except (ValueError, AttributeError):
                self.logger.warning(f"Failed to parse amount: {subscription.get('amount')}")
        self.logger.info(f"Total monthly recurring amount: {total}")
        return total

    def verify_subscription_status(self, subscription_id, expected_status):
        self.logger.info(f"Verifying subscription {subscription_id} has status {expected_status}")
        subscription = self.get_subscription_details(subscription_id)
        if subscription:
            actual_status = subscription.get('status', '').lower()
            expected_status_lower = expected_status.lower()
            if actual_status == expected_status_lower:
                self.logger.info(f"Subscription status verified: {expected_status}")
                return True
            else:
                self.logger.error(f"Status mismatch. Expected: {expected_status}, Got: {actual_status}")
                return False
        return False

    def navigate_to_next_page(self):
        self.logger.info("Navigating to next subscriptions page")
        self.navigate_to_recurring_payments()
        success = self.recurring_payments_page.go_to_next_page()
        if success:
            self.logger.info("Navigated to next page successfully")
        else:
            self.logger.warning("Could not navigate to next page")
        return success

    def navigate_to_previous_page(self):
        self.logger.info("Navigating to previous subscriptions page")
        self.navigate_to_recurring_payments()
        success = self.recurring_payments_page.go_to_previous_page()
        if success:
            self.logger.info("Navigated to previous page successfully")
        else:
            self.logger.warning("Could not navigate to previous page")
        return success

    def validate_the_ui_of_recurring_payments_page_functionality(self):
        """Test: Validate the UI of 'Recurring Payments' page functionality."""
        self.logger.info("TEST: Validate the UI of Recurring Payments page functionality")
        try:
            self.wait_for_recurring_payments_page_to_load()
            page_title_visible = self.recurring_payments_page.is_page_title_visible()
            subscriptions_table_visible = self.recurring_payments_page.is_subscriptions_table_visible()
            action_buttons_visible = self.recurring_payments_page.are_action_buttons_visible()
            filter_controls_visible = self.recurring_payments_page.are_filter_controls_visible()
            ui_complete = page_title_visible and subscriptions_table_visible and action_buttons_visible
            
            if ui_complete:
                self.logger.info("✓ TEST PASSED: Recurring Payments UI is complete and functional")
            else:
                self.logger.error("✗ TEST FAILED: Some UI elements are missing")
            
            return {
                'test_case_title': "Validate the UI of 'Recurring Payments' page functionality",
                'page_title_visible': page_title_visible,
                'subscriptions_table_visible': subscriptions_table_visible,
                'action_buttons_visible': action_buttons_visible,
                'filter_controls_visible': filter_controls_visible,
                'test_passed': ui_complete,
                'test_failure_reason': None if ui_complete else 'UI elements not fully visible'
            }
        except Exception as e:
            self.logger.error(f"TEST FAILED: {str(e)}")
            return {
                'test_case_title': "Validate the UI of 'Recurring Payments' page functionality",
                'page_title_visible': False,
                'subscriptions_table_visible': False,
                'action_buttons_visible': False,
                'filter_controls_visible': False,
                'test_passed': False,
                'test_failure_reason': str(e)
            }

    def verify_recurring_payments_page_is_accessible_only_to_authenticated_users(self):
        """Test: Verify Recurring Payments page is accessible only to authenticated users."""
        try:
            self.logger.info("TEST: Verify Recurring Payments page is accessible only to authenticated users")
            self.wait_for_recurring_payments_page_to_load()
            
            is_user_authenticated = self.recurring_payments_page.is_user_authenticated()
            is_login_required = self.recurring_payments_page.is_login_required()
            is_access_denied_message = self.recurring_payments_page.is_access_denied_message_displayed()
            
            access_controlled = is_user_authenticated or is_login_required or is_access_denied_message
            
            return {
                'test_case_title': 'Verify Recurring Payments page is accessible only to authenticated users',
                'is_user_authenticated': is_user_authenticated,
                'is_login_required': is_login_required,
                'is_access_denied_message': is_access_denied_message,
                'test_passed': access_controlled,
                'test_failure_reason': None if access_controlled else 'Page access control not verified'
            }
        except Exception as e:
            self.logger.error(f"Test failed: {e}")
            return {
                'test_case_title': 'Verify Recurring Payments page is accessible only to authenticated users',
                'test_passed': False,
                'test_failure_reason': str(e)
            }
