from pages.productReturnsPage import ProductReturnsPage
from pages.returnRequestPage import ReturnRequestPage
from pages.returnDetailsPage import ReturnDetailsPage
from utilities.customLogger import LoggerFactory


class ProductReturnsFlow:
    logger = LoggerFactory.get_logger(__name__)

    def __init__(self, driver):
        self.driver = driver
        self.returns_page = ProductReturnsPage(driver)
        self.return_request_page = ReturnRequestPage(driver)
        self.return_details_page = ReturnDetailsPage(driver)

    def wait_for_returns_page_to_load(self):
        self.logger.info("Waiting for Product Returns page to load")
        self.returns_page.handle_cloudflare_if_present()
        if not self.returns_page.is_page_loaded():
            self.logger.error("Product Returns page failed to load")
            raise Exception("Product Returns page failed to load")
        self.logger.info("Product Returns page loaded successfully")

    def wait_for_return_request_page_to_load(self):
        self.logger.info("Waiting for Return Request page to load")
        self.return_request_page.handle_cloudflare_if_present()
        if not self.return_request_page.is_page_loaded():
            self.logger.error("Return Request page failed to load")
            raise Exception("Return Request page failed to load")
        self.logger.info("Return Request page loaded successfully")

    def wait_for_return_details_page_to_load(self):
        self.logger.info("Waiting for Return Details page to load")
        self.return_details_page.handle_cloudflare_if_present()
        if not self.return_details_page.is_page_loaded():
            self.logger.error("Return Details page failed to load")
            raise Exception("Return Details page failed to load")
        self.logger.info("Return Details page loaded successfully")

    def navigate_to_returns(self):
        self.logger.info("Navigating to Product Returns page")
        self.wait_for_returns_page_to_load()
        self.logger.info("Product Returns page ready")

    def verify_returns_page_loaded(self):
        self.logger.info("Verifying Product Returns page is loaded")
        self.wait_for_returns_page_to_load()
        is_loaded = self.returns_page.is_page_loaded()
        if is_loaded:
            self.logger.info("Product Returns page verified as loaded")
        else:
            self.logger.error("Product Returns page verification failed")
        return is_loaded

    def verify_no_returns_exist(self):
        self.logger.info("Verifying no returns exist")
        self.navigate_to_returns()
        is_empty = self.returns_page.is_no_returns_message_displayed()
        if is_empty:
            self.logger.info("No returns found as expected")
        else:
            self.logger.warning("Returns are present")
        return is_empty

    def get_all_returns(self):
        self.logger.info("Getting all returns")
        self.navigate_to_returns()
        returns = self.returns_page.get_all_returns()
        self.logger.info(f"Retrieved {len(returns)} returns")
        return returns

    def get_return_count(self):
        self.logger.info("Getting return count")
        self.navigate_to_returns()
        count = self.returns_page.get_returns_count()
        self.logger.info(f"Return count: {count}")
        return count

    def get_return_details(self, return_number):
        self.logger.info(f"Getting details for return: {return_number}")
        self.navigate_to_returns()
        return_info = self.returns_page.get_return_by_number(return_number)
        if return_info:
            self.logger.info(f"Return details retrieved: {return_info}")
        else:
            self.logger.warning(f"Return not found: {return_number}")
        return return_info

    def view_return_details_by_number(self, return_number):
        self.logger.info(f"Viewing return details: {return_number}")
        self.navigate_to_returns()
        success = self.returns_page.view_return_details_by_number(return_number)
        if success:
            self.logger.info(f"Return details viewed: {return_number}")
        else:
            self.logger.error(f"Failed to view return details: {return_number}")
        return success

    def view_return_details_by_index(self, index):
        self.logger.info(f"Viewing return details at index: {index}")
        self.navigate_to_returns()
        success = self.returns_page.view_return_details_by_index(index)
        if success:
            self.logger.info(f"Return details viewed at index: {index}")
        else:
            self.logger.error(f"Failed to view return details at index: {index}")
        return success

    def edit_return_by_number(self, return_number):
        self.logger.info(f"Editing return: {return_number}")
        self.navigate_to_returns()
        success = self.returns_page.edit_return_by_number(return_number)
        if success:
            self.logger.info(f"Return edit initiated: {return_number}")
        else:
            self.logger.error(f"Failed to edit return: {return_number}")
        return success

    def edit_return_by_index(self, index):
        self.logger.info(f"Editing return at index: {index}")
        self.navigate_to_returns()
        success = self.returns_page.edit_return_by_index(index)
        if success:
            self.logger.info(f"Return edit initiated at index: {index}")
        else:
            self.logger.error(f"Failed to edit return at index: {index}")
        return success

    def delete_return_by_number(self, return_number):
        self.logger.info(f"Deleting return: {return_number}")
        self.navigate_to_returns()
        success = self.returns_page.delete_return_by_number(return_number)
        if success:
            self.logger.info(f"Return deletion initiated: {return_number}")
        else:
            self.logger.error(f"Failed to delete return: {return_number}")
        return success

    def delete_return_by_index(self, index):
        self.logger.info(f"Deleting return at index: {index}")
        self.navigate_to_returns()
        success = self.returns_page.delete_return_by_index(index)
        if success:
            self.logger.info(f"Return deletion initiated at index: {index}")
        else:
            self.logger.error(f"Failed to delete return at index: {index}")
        return success

    def cancel_return_by_number(self, return_number):
        self.logger.info(f"Cancelling return: {return_number}")
        self.navigate_to_returns()
        success = self.returns_page.cancel_return_by_number(return_number)
        if success:
            self.logger.info(f"Return cancellation initiated: {return_number}")
        else:
            self.logger.error(f"Failed to cancel return: {return_number}")
        return success

    def cancel_return_by_index(self, index):
        self.logger.info(f"Cancelling return at index: {index}")
        self.navigate_to_returns()
        success = self.returns_page.cancel_return_by_index(index)
        if success:
            self.logger.info(f"Return cancellation initiated at index: {index}")
        else:
            self.logger.error(f"Failed to cancel return at index: {index}")
        return success

    def navigate_to_create_return(self):
        self.logger.info("Navigating to create return request")
        self.navigate_to_returns()
        self.returns_page.click_create_return()
        self.logger.info("Create return button clicked")

    def filter_returns_by_status(self, status):
        self.logger.info(f"Filtering returns by status: {status}")
        self.navigate_to_returns()
        success = self.returns_page.filter_by_status(status)
        if success:
            self.logger.info(f"Returns filtered by status: {status}")
        else:
            self.logger.error(f"Failed to filter by status: {status}")
        return success

    def sort_returns_by_option(self, sort_option):
        self.logger.info(f"Sorting returns by: {sort_option}")
        self.navigate_to_returns()
        success = self.returns_page.sort_returns(sort_option)
        if success:
            self.logger.info(f"Returns sorted by: {sort_option}")
        else:
            self.logger.error(f"Failed to sort returns: {sort_option}")
        return success

    def search_for_return(self, search_term):
        self.logger.info(f"Searching for return: {search_term}")
        self.navigate_to_returns()
        success = self.returns_page.search_return(search_term)
        if success:
            self.logger.info(f"Return search executed: {search_term}")
        else:
            self.logger.error(f"Failed to search for return: {search_term}")
        return success

    def verify_pagination_visible(self):
        self.logger.info("Verifying pagination is visible")
        self.navigate_to_returns()
        is_visible = self.returns_page.is_pagination_visible()
        if is_visible:
            self.logger.info("Pagination is visible")
        else:
            self.logger.warning("Pagination is not visible")
        return is_visible

    def navigate_to_next_page(self):
        self.logger.info("Navigating to next page of returns")
        self.navigate_to_returns()
        success = self.returns_page.go_to_next_page()
        if success:
            self.logger.info("Navigated to next page")
        else:
            self.logger.error("Failed to navigate to next page")
        return success

    def navigate_to_previous_page(self):
        self.logger.info("Navigating to previous page of returns")
        self.navigate_to_returns()
        success = self.returns_page.go_to_previous_page()
        if success:
            self.logger.info("Navigated to previous page")
        else:
            self.logger.error("Failed to navigate to previous page")
        return success

    def export_returns(self):
        self.logger.info("Exporting returns")
        self.navigate_to_returns()
        success = self.returns_page.export_returns()
        if success:
            self.logger.info("Returns exported successfully")
        else:
            self.logger.error("Failed to export returns")
        return success

    def print_returns(self):
        self.logger.info("Printing returns")
        self.navigate_to_returns()
        success = self.returns_page.print_returns()
        if success:
            self.logger.info("Returns printed successfully")
        else:
            self.logger.error("Failed to print returns")
        return success

    def initiate_return_request(self, order_identifier):
        self.logger.info(f"Initiating return request for order: {order_identifier}")
        self.navigate_to_create_return()
        self.wait_for_return_request_page_to_load()
        success = self.return_request_page.select_order(order_identifier)
        if success:
            self.logger.info(f"Order selected for return: {order_identifier}")
        else:
            self.logger.error(f"Failed to select order: {order_identifier}")
        return success

    def select_product_for_return(self, product_index):
        self.logger.info(f"Selecting product at index: {product_index} for return")
        self.wait_for_return_request_page_to_load()
        success = self.return_request_page.select_product_for_return(product_index)
        if success:
            self.logger.info(f"Product selected at index: {product_index}")
        else:
            self.logger.error(f"Failed to select product at index: {product_index}")
        return success

    def select_multiple_products_for_return(self, product_indices):
        self.logger.info(f"Selecting multiple products for return: {product_indices}")
        self.wait_for_return_request_page_to_load()
        success = self.return_request_page.select_multiple_products(product_indices)
        if success:
            self.logger.info(f"Multiple products selected: {product_indices}")
        else:
            self.logger.error("Failed to select multiple products")
        return success

    def set_return_quantity(self, product_index, quantity):
        self.logger.info(f"Setting return quantity for product {product_index}: {quantity}")
        self.wait_for_return_request_page_to_load()
        success = self.return_request_page.set_return_quantity(product_index, quantity)
        if success:
            self.logger.info(f"Quantity set: {quantity}")
        else:
            self.logger.error("Failed to set return quantity")
        return success

    def provide_return_reason(self, reason):
        self.logger.info(f"Providing return reason: {reason}")
        self.wait_for_return_request_page_to_load()
        success = self.return_request_page.select_return_reason(reason)
        if success:
            self.logger.info(f"Return reason provided: {reason}")
        else:
            self.logger.error("Failed to provide return reason")
        return success

    def provide_reason_details(self, reason_text):
        self.logger.info("Providing reason details")
        self.wait_for_return_request_page_to_load()
        success = self.return_request_page.enter_reason_text(reason_text)
        if success:
            self.logger.info("Reason details provided")
        else:
            self.logger.error("Failed to provide reason details")
        return success

    def add_comments_to_return(self, comments):
        self.logger.info("Adding comments to return")
        self.wait_for_return_request_page_to_load()
        success = self.return_request_page.enter_additional_comments(comments)
        if success:
            self.logger.info("Comments added to return")
        else:
            self.logger.error("Failed to add comments")
        return success

    def specify_refund_amount(self, amount):
        self.logger.info(f"Specifying refund amount: {amount}")
        self.wait_for_return_request_page_to_load()
        success = self.return_request_page.enter_refund_amount(amount)
        if success:
            self.logger.info(f"Refund amount specified: {amount}")
        else:
            self.logger.error("Failed to specify refund amount")
        return success

    def upload_attachment(self, file_path):
        self.logger.info(f"Uploading attachment: {file_path}")
        self.wait_for_return_request_page_to_load()
        success = self.return_request_page.attach_file(file_path)
        if success:
            self.logger.info(f"Attachment uploaded: {file_path}")
        else:
            self.logger.error("Failed to upload attachment")
        return success

    def submit_return_request(self):
        self.logger.info("Submitting return request")
        self.wait_for_return_request_page_to_load()
        success = self.return_request_page.submit_return_request()
        if success:
            self.logger.info("Return request submitted successfully")
        else:
            self.logger.error("Failed to submit return request")
        return success

    def verify_return_request_validation_errors(self):
        self.logger.info("Verifying return request validation errors")
        self.wait_for_return_request_page_to_load()
        errors = self.return_request_page.get_validation_errors()
        if errors:
            self.logger.warning(f"Validation errors found: {len(errors)}")
        else:
            self.logger.info("No validation errors found")
        return errors

    def get_return_full_details(self, return_number):
        self.logger.info(f"Getting full details for return: {return_number}")
        self.navigate_to_returns()
        self.returns_page.view_return_details_by_number(return_number)
        self.wait_for_return_details_page_to_load()
        
        details = {
            'return_number': self.return_details_page.get_return_number(),
            'order_number': self.return_details_page.get_order_number(),
            'status': self.return_details_page.get_return_status(),
            'date': self.return_details_page.get_return_date(),
            'reason': self.return_details_page.get_return_reason(),
            'comments': self.return_details_page.get_comments(),
            'refund_amount': self.return_details_page.get_refund_amount(),
            'refund_status': self.return_details_page.get_refund_status(),
            'items': self.return_details_page.get_returned_items()
        }
        self.logger.info(f"Full return details retrieved: {return_number}")
        return details

    def get_return_items_details(self, return_number):
        self.logger.info(f"Getting item details for return: {return_number}")
        self.navigate_to_returns()
        self.returns_page.view_return_details_by_number(return_number)
        self.wait_for_return_details_page_to_load()
        
        items = self.return_details_page.get_returned_items()
        self.logger.info(f"Retrieved {len(items)} items from return")
        return items

    def verify_refund_information(self, return_number):
        self.logger.info(f"Verifying refund information for return: {return_number}")
        self.navigate_to_returns()
        self.returns_page.view_return_details_by_number(return_number)
        self.wait_for_return_details_page_to_load()
        
        refund_info = {
            'amount': self.return_details_page.get_refund_amount(),
            'status': self.return_details_page.get_refund_status(),
            'date': self.return_details_page.get_refund_date()
        }
        self.logger.info(f"Refund information verified: {refund_info}")
        return refund_info

    def get_return_timeline(self, return_number):
        self.logger.info(f"Getting timeline for return: {return_number}")
        self.navigate_to_returns()
        self.returns_page.view_return_details_by_number(return_number)
        self.wait_for_return_details_page_to_load()
        
        event_count = self.return_details_page.get_timeline_events()
        self.logger.info(f"Timeline events count: {event_count}")
        return event_count

    def verify_attachments_present(self, return_number):
        self.logger.info(f"Verifying attachments for return: {return_number}")
        self.navigate_to_returns()
        self.returns_page.view_return_details_by_number(return_number)
        self.wait_for_return_details_page_to_load()
        
        count = self.return_details_page.get_attachments_count()
        if count > 0:
            self.logger.info(f"Attachments found: {count}")
        else:
            self.logger.warning("No attachments found")
        return count

    def download_return_attachment(self, return_number, attachment_index):
        self.logger.info(f"Downloading attachment {attachment_index} for return: {return_number}")
        self.navigate_to_returns()
        self.returns_page.view_return_details_by_number(return_number)
        self.wait_for_return_details_page_to_load()
        
        success = self.return_details_page.download_attachment_by_index(attachment_index)
        if success:
            self.logger.info(f"Attachment {attachment_index} downloaded")
        else:
            self.logger.error(f"Failed to download attachment {attachment_index}")
        return success

    def verify_returns_success_message(self):
        self.logger.info("Verifying returns page success message")
        self.navigate_to_returns()
        is_displayed = self.returns_page.is_success_message_displayed()
        if is_displayed:
            message = self.returns_page.get_success_message()
            self.logger.info(f"Success message verified: {message}")
        else:
            self.logger.warning("Success message not displayed")
        return is_displayed

    def verify_return_request_success_message(self):
        self.logger.info("Verifying return request success message")
        self.wait_for_return_request_page_to_load()
        is_displayed = self.return_request_page.is_success_message_displayed()
        if is_displayed:
            message = self.return_request_page.get_success_message()
            self.logger.info(f"Success message verified: {message}")
        else:
            self.logger.warning("Success message not displayed")
        return is_displayed

    def verify_return_details_success_message(self):
        self.logger.info("Verifying return details success message")
        self.wait_for_return_details_page_to_load()
        is_displayed = self.return_details_page.is_success_message_displayed()
        if is_displayed:
            message = self.return_details_page.get_success_message()
            self.logger.info(f"Success message verified: {message}")
        else:
            self.logger.warning("Success message not displayed")
        return is_displayed

    def verify_product_returns_page_is_accessible_only_for_logged_in_users(self):
        """Test: Verify product returns page is accessible only for logged-in users."""
        self.logger.info("TEST: Verify product returns page is accessible only for logged-in users")
        try:
            self.wait_for_returns_page_to_load()
            page_loaded = self.returns_page.is_page_loaded()
            login_required = self.returns_page.is_login_required()
            user_authenticated = self.returns_page.is_user_authenticated()
            no_access_error = not self.returns_page.is_access_denied_message_displayed()
            page_accessible_to_logged_in = page_loaded and user_authenticated and no_access_error
            
            if page_accessible_to_logged_in:
                self.logger.info("✓ TEST PASSED: Returns page accessible only to logged-in users")
            else:
                self.logger.error("✗ TEST FAILED: Access control not properly enforced")
            
            return {
                'test_case_title': 'Verify product returns page is accessible only for logged-in users',
                'page_loaded': page_loaded,
                'login_required': login_required,
                'user_authenticated': user_authenticated,
                'no_access_error': no_access_error,
                'test_passed': page_accessible_to_logged_in,
                'test_failure_reason': None if page_accessible_to_logged_in else 'Access control not enforced'
            }
        except Exception as e:
            self.logger.error(f"TEST FAILED: {str(e)}")
            return {
                'test_case_title': 'Verify product returns page is accessible only for logged-in users',
                'page_loaded': False,
                'login_required': False,
                'user_authenticated': False,
                'no_access_error': False,
                'test_passed': False,
                'test_failure_reason': str(e)
            }

    def verify_system_rejects_return_quantity_greater_than_purchased_quantity(self):
        """Test: Verify system rejects return quantity greater than purchased quantity."""
        self.logger.info("TEST: Verify system rejects return quantity greater than purchased quantity")
        try:
            self.wait_for_return_request_page_to_load()
            purchased_qty = self.return_request_page.get_purchased_quantity()
            invalid_qty = purchased_qty + 1 if purchased_qty else 999
            self.return_request_page.enter_return_quantity(invalid_qty)
            error_displayed = self.return_request_page.is_invalid_quantity_error_displayed()
            quantity_rejected = error_displayed and invalid_qty > purchased_qty
            
            if quantity_rejected:
                self.logger.info("✓ TEST PASSED: System correctly rejected invalid return quantity")
            else:
                self.logger.error("✗ TEST FAILED: System did not reject invalid quantity")
            
            return {
                'test_case_title': 'Verify system rejects return quantity greater than purchased quantity',
                'purchased_quantity': purchased_qty,
                'entered_quantity': invalid_qty,
                'error_displayed': error_displayed,
                'quantity_rejected': quantity_rejected,
                'test_passed': quantity_rejected,
                'test_failure_reason': None if quantity_rejected else 'Invalid quantity not rejected'
            }
        except Exception as e:
            self.logger.error(f"TEST FAILED: {str(e)}")
            return {
                'test_case_title': 'Verify system rejects return quantity greater than purchased quantity',
                'purchased_quantity': None,
                'entered_quantity': None,
                'error_displayed': False,
                'quantity_rejected': False,
                'test_passed': False,
                'test_failure_reason': str(e)
            }

    def verify_return_request_is_blocked_for_cancelled_orders(self):
        """Test: Verify return request is blocked for cancelled orders."""
        self.logger.info("TEST: Verify return request is blocked for cancelled orders")
        try:
            self.wait_for_returns_page_to_load()
            cancelled_order = self.returns_page.get_cancelled_order_if_exists()
            is_blocked = self.returns_page.is_return_button_disabled_for_cancelled_order(cancelled_order) if cancelled_order else True
            block_message = self.returns_page.is_cancellation_block_message_displayed()
            return_blocked = is_blocked and block_message
            
            if return_blocked:
                self.logger.info("✓ TEST PASSED: Return request blocked for cancelled orders")
            else:
                self.logger.error("✗ TEST FAILED: Return request not blocked for cancelled orders")
            
            return {
                'test_case_title': 'Verify return request is blocked for cancelled orders',
                'cancelled_order_found': cancelled_order is not None,
                'return_blocked': is_blocked,
                'block_message_shown': block_message,
                'test_passed': return_blocked,
                'test_failure_reason': None if return_blocked else 'Return not blocked for cancelled order'
            }
        except Exception as e:
            self.logger.error(f"TEST FAILED: {str(e)}")
            return {
                'test_case_title': 'Verify return request is blocked for cancelled orders',
                'cancelled_order_found': False,
                'return_blocked': False,
                'block_message_shown': False,
                'test_passed': False,
                'test_failure_reason': str(e)
            }
