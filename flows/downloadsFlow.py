from pages.downloadsPage import DownloadsPage
from utilities.customLogger import LoggerFactory


class DownloadsFlow:
    logger = LoggerFactory.get_logger(__name__)

    def __init__(self, driver):
        self.driver = driver
        self.downloads_page = DownloadsPage(driver)

    def wait_for_downloads_page_to_load(self):
        self.logger.info("Waiting for Downloads page to load")
        self.downloads_page.handle_cloudflare_if_present()
        if not self.downloads_page.is_page_loaded():
            self.logger.error("Downloads page failed to load")
            raise Exception("Downloads page failed to load")
        self.logger.info("Downloads page loaded successfully")

    def navigate_to_downloads(self):
        self.logger.info("Navigating to Downloads page")
        self.wait_for_downloads_page_to_load()
        self.logger.info("Downloads page ready")

    def verify_downloads_page_loaded(self):
        self.logger.info("Verifying Downloads page is loaded")
        self.wait_for_downloads_page_to_load()
        is_loaded = self.downloads_page.is_page_loaded()
        if is_loaded:
            self.logger.info("Downloads page verified as loaded")
        else:
            self.logger.error("Downloads page verification failed")
        return is_loaded

    def verify_no_downloads_exist(self):
        self.logger.info("Verifying no downloads exist")
        self.navigate_to_downloads()
        is_empty = self.downloads_page.is_no_downloads_message_displayed()
        if is_empty:
            self.logger.info("No downloads found as expected")
        else:
            self.logger.warning("Downloads are present")
        return is_empty

    def get_all_downloads(self):
        self.logger.info("Getting all downloads")
        self.navigate_to_downloads()
        downloads = self.downloads_page.get_all_downloads()
        self.logger.info(f"Retrieved {len(downloads)} downloads")
        return downloads

    def get_downloads_count(self):
        self.logger.info("Getting downloads count")
        self.navigate_to_downloads()
        count = self.downloads_page.get_downloads_count()
        self.logger.info(f"Downloads count: {count}")
        return count

    def get_download_details(self, product_name):
        self.logger.info(f"Getting details for download: {product_name}")
        self.navigate_to_downloads()
        download = self.downloads_page.get_download_by_product_name(product_name)
        if download:
            self.logger.info(f"Download details retrieved: {download}")
        else:
            self.logger.warning(f"Download not found: {product_name}")
        return download

    def download_by_product_name(self, product_name):
        self.logger.info(f"Downloading product: {product_name}")
        self.navigate_to_downloads()
        success = self.downloads_page.download_by_product_name(product_name)
        if success:
            self.logger.info(f"Product downloaded: {product_name}")
        else:
            self.logger.error(f"Failed to download product: {product_name}")
        return success

    def download_by_index(self, index):
        self.logger.info(f"Downloading at index: {index}")
        self.navigate_to_downloads()
        success = self.downloads_page.download_by_index(index)
        if success:
            self.logger.info(f"Downloaded at index: {index}")
        else:
            self.logger.error(f"Failed to download at index: {index}")
        return success

    def verify_download_available(self, product_name):
        self.logger.info(f"Verifying download is available: {product_name}")
        self.navigate_to_downloads()
        is_available = self.downloads_page.is_download_available_by_product_name(product_name)
        if is_available:
            self.logger.info(f"Download is available: {product_name}")
        else:
            self.logger.warning(f"Download is not available: {product_name}")
        return is_available

    def verify_download_expired(self, product_name):
        self.logger.info(f"Verifying download is expired: {product_name}")
        self.navigate_to_downloads()
        is_expired = self.downloads_page.is_download_expired_by_product_name(product_name)
        if is_expired:
            self.logger.info(f"Download is expired: {product_name}")
        else:
            self.logger.info(f"Download is not expired: {product_name}")
        return is_expired

    def filter_downloads_by_status(self, status):
        self.logger.info(f"Filtering downloads by status: {status}")
        self.navigate_to_downloads()
        success = self.downloads_page.filter_by_status(status)
        if success:
            self.logger.info(f"Downloads filtered by status: {status}")
        else:
            self.logger.error(f"Failed to filter by status: {status}")
        return success

    def sort_downloads_by_option(self, sort_option):
        self.logger.info(f"Sorting downloads by: {sort_option}")
        self.navigate_to_downloads()
        success = self.downloads_page.sort_downloads(sort_option)
        if success:
            self.logger.info(f"Downloads sorted by: {sort_option}")
        else:
            self.logger.error(f"Failed to sort downloads: {sort_option}")
        return success

    def search_for_download(self, search_term):
        self.logger.info(f"Searching for download: {search_term}")
        self.navigate_to_downloads()
        success = self.downloads_page.search_download(search_term)
        if success:
            self.logger.info(f"Download search executed: {search_term}")
        else:
            self.logger.error(f"Failed to search for download: {search_term}")
        return success

    def clear_all_filters(self):
        self.logger.info("Clearing all filters")
        self.navigate_to_downloads()
        success = self.downloads_page.clear_filters()
        if success:
            self.logger.info("All filters cleared")
        else:
            self.logger.error("Failed to clear filters")
        return success

    def verify_pagination_visible(self):
        self.logger.info("Verifying pagination is visible")
        self.navigate_to_downloads()
        is_visible = self.downloads_page.is_pagination_visible()
        if is_visible:
            self.logger.info("Pagination is visible")
        else:
            self.logger.warning("Pagination is not visible")
        return is_visible

    def navigate_to_next_page(self):
        self.logger.info("Navigating to next page of downloads")
        self.navigate_to_downloads()
        success = self.downloads_page.go_to_next_page()
        if success:
            self.logger.info("Navigated to next page")
        else:
            self.logger.error("Failed to navigate to next page")
        return success

    def navigate_to_previous_page(self):
        self.logger.info("Navigating to previous page of downloads")
        self.navigate_to_downloads()
        success = self.downloads_page.go_to_previous_page()
        if success:
            self.logger.info("Navigated to previous page")
        else:
            self.logger.error("Failed to navigate to previous page")
        return success

    def export_downloads(self):
        self.logger.info("Exporting downloads")
        self.navigate_to_downloads()
        success = self.downloads_page.export_downloads()
        if success:
            self.logger.info("Downloads exported successfully")
        else:
            self.logger.error("Failed to export downloads")
        return success

    def print_downloads(self):
        self.logger.info("Printing downloads")
        self.navigate_to_downloads()
        success = self.downloads_page.print_downloads()
        if success:
            self.logger.info("Downloads printed successfully")
        else:
            self.logger.error("Failed to print downloads")
        return success

    def verify_instructions_present(self):
        self.logger.info("Verifying instructions section is visible")
        self.navigate_to_downloads()
        is_visible = self.downloads_page.is_instructions_section_visible()
        if is_visible:
            self.logger.info("Instructions section is visible")
            instructions = self.downloads_page.get_instructions_text()
            self.logger.info(f"Instructions retrieved")
        else:
            self.logger.warning("Instructions section is not visible")
        return is_visible

    def verify_license_agreement_present(self):
        self.logger.info("Verifying license agreement is visible")
        self.navigate_to_downloads()
        is_visible = self.downloads_page.is_license_agreement_visible()
        if is_visible:
            self.logger.info("License agreement section is visible")
            license_text = self.downloads_page.get_license_text()
            self.logger.info(f"License text retrieved")
        else:
            self.logger.warning("License agreement section is not visible")
        return is_visible

    def get_instructions_text(self):
        self.logger.info("Getting instructions text")
        self.navigate_to_downloads()
        instructions = self.downloads_page.get_instructions_text()
        if instructions:
            self.logger.info("Instructions text retrieved")
        else:
            self.logger.warning("Failed to retrieve instructions text")
        return instructions

    def get_license_agreement_text(self):
        self.logger.info("Getting license agreement text")
        self.navigate_to_downloads()
        license_text = self.downloads_page.get_license_text()
        if license_text:
            self.logger.info("License text retrieved")
        else:
            self.logger.warning("Failed to retrieve license text")
        return license_text

    def verify_success_message(self):
        self.logger.info("Verifying success message is displayed")
        self.navigate_to_downloads()
        is_displayed = self.downloads_page.is_success_message_displayed()
        if is_displayed:
            message = self.downloads_page.get_success_message()
            self.logger.info(f"Success message verified: {message}")
        else:
            self.logger.warning("Success message not displayed")
        return is_displayed

    def verify_error_message(self):
        self.logger.info("Verifying error message is displayed")
        self.navigate_to_downloads()
        is_displayed = self.downloads_page.is_error_message_displayed()
        if is_displayed:
            message = self.downloads_page.get_error_message()
            self.logger.warning(f"Error message verified: {message}")
        else:
            self.logger.info("Error message not displayed")
        return is_displayed

    def verify_info_message(self):
        self.logger.info("Verifying info message is displayed")
        self.navigate_to_downloads()
        is_displayed = self.downloads_page.is_info_message_displayed()
        if is_displayed:
            message = self.downloads_page.get_info_message()
            self.logger.info(f"Info message verified: {message}")
        else:
            self.logger.warning("Info message not displayed")
        return is_displayed

    def verify_warning_message(self):
        self.logger.info("Verifying warning message is displayed")
        self.navigate_to_downloads()
        is_displayed = self.downloads_page.is_warning_message_displayed()
        if is_displayed:
            message = self.downloads_page.get_warning_message()
            self.logger.warning(f"Warning message verified: {message}")
        else:
            self.logger.info("Warning message not displayed")
        return is_displayed

    def verify_downloads_page_is_accessible_only_to_authenticated_users(self):
        """Test: Verify Downloads page is accessible only to authenticated users."""
        self.logger.info("TEST: Verify Downloads page is accessible only to authenticated users")
        try:
            self.wait_for_downloads_page_to_load()
            page_loaded = self.downloads_page.is_page_loaded()
            user_authenticated = self.downloads_page.is_user_authenticated()
            login_required = self.downloads_page.is_login_required()
            no_access_error = not self.downloads_page.is_access_denied_message_displayed()
            page_accessible = page_loaded and user_authenticated and no_access_error
            
            if page_accessible:
                self.logger.info("✓ TEST PASSED: Downloads page accessible only to authenticated users")
            else:
                self.logger.error("✗ TEST FAILED: Access control not properly enforced")
            
            return {
                'test_case_title': 'Verify Downloads page is accessible only to authenticated users',
                'page_loaded': page_loaded,
                'user_authenticated': user_authenticated,
                'login_required': login_required,
                'no_access_error': no_access_error,
                'test_passed': page_accessible,
                'test_failure_reason': None if page_accessible else 'Access not properly restricted'
            }
        except Exception as e:
            self.logger.error(f"TEST FAILED: {str(e)}")
            return {
                'test_case_title': 'Verify Downloads page is accessible only to authenticated users',
                'page_loaded': False,
                'user_authenticated': False,
                'login_required': False,
                'no_access_error': False,
                'test_passed': False,
                'test_failure_reason': str(e)
            }

    def verify_downloadable_items_are_visible_only_after_successful_purchase(self):
        """Test: Verify downloadable items are visible only after successful purchase."""
        self.logger.info("TEST: Verify downloadable items are visible only after successful purchase")
        try:
            self.wait_for_downloads_page_to_load()
            has_downloads = self.downloads_page.has_downloadable_items()
            purchase_confirmed = self.downloads_page.is_purchase_confirmed()
            items_visible = self.downloads_page.are_download_items_visible()
            no_restriction_error = not self.downloads_page.is_purchase_restriction_error_displayed()
            downloads_available = has_downloads and purchase_confirmed and items_visible and no_restriction_error
            
            if downloads_available:
                self.logger.info("✓ TEST PASSED: Downloadable items visible only after purchase")
            else:
                self.logger.error("✗ TEST FAILED: Download items not properly gated")
            
            return {
                'test_case_title': 'Verify downloadable items are visible only after successful purchase',
                'has_downloads': has_downloads,
                'purchase_confirmed': purchase_confirmed,
                'items_visible': items_visible,
                'no_restriction_error': no_restriction_error,
                'test_passed': downloads_available,
                'test_failure_reason': None if downloads_available else 'Downloads not properly restricted to purchases'
            }
        except Exception as e:
            self.logger.error(f"TEST FAILED: {str(e)}")
            return {
                'test_case_title': 'Verify downloadable items are visible only after successful purchase',
                'has_downloads': False,
                'purchase_confirmed': False,
                'items_visible': False,
                'no_restriction_error': False,
                'test_passed': False,
                'test_failure_reason': str(e)
            }
