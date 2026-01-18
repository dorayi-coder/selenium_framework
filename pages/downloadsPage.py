from selenium.webdriver.common.by import By
from utilities.basePage import BasePage
from utilities.customLogger import LoggerFactory


class DownloadsPage(BasePage):
    logger = LoggerFactory.get_logger(__name__)


    _downloads_page_title = (By.XPATH, "//h1[contains(text(), 'Download')] | //h1[contains(text(), 'Downloads')]")
    _downloads_container = (By.CLASS_NAME, "downloads-container")
    _downloads_table = (By.XPATH, "//table[contains(@class, 'download')]")
    _download_rows = (By.XPATH, "//table[contains(@class, 'download')]//tbody//tr | //div[contains(@class, 'download-item')]")
    _product_name_cell = (By.XPATH, ".//td[1] | .//span[contains(@class, 'product-name')]")
    _order_number_cell = (By.XPATH, ".//td[2]//a | .//span[contains(@class, 'order-number')]")
    _download_date_cell = (By.XPATH, ".//td[3] | .//span[contains(@class, 'download-date')]")
    _download_count_cell = (By.XPATH, ".//td[4] | .//span[contains(@class, 'download-count')]")
    _download_remaining_cell = (By.XPATH, ".//td[5] | .//span[contains(@class, 'download-remaining')]")
    _download_expiration_cell = (By.XPATH, ".//td[6] | .//span[contains(@class, 'expiration-date')]")
    _download_button = (By.XPATH, ".//a[contains(text(), 'Download')] | .//button[contains(text(), 'Download')]")
    _download_link = (By.XPATH, ".//a[contains(@class, 'download-link')]")
    _no_downloads_message = (By.XPATH, "//div[contains(text(), 'no download')] | //p[contains(text(), 'download')]")
    _downloads_summary_section = (By.CLASS_NAME, "downloads-summary")
    _total_downloads_count = (By.XPATH, "//span[contains(text(), 'Total')] | //div[contains(@class, 'total-downloads')]")
    _active_downloads_count = (By.XPATH, "//span[contains(text(), 'Active')] | //div[contains(@class, 'active-downloads')]")
    _expired_downloads_count = (By.XPATH, "//span[contains(text(), 'Expired')] | //div[contains(@class, 'expired-downloads')]")
    _filter_section = (By.CLASS_NAME, "filter-section")
    _status_filter = (By.XPATH, "//select[@name='status'] | //label[contains(text(), 'Status')]")
    _search_input = (By.XPATH, "//input[contains(@placeholder, 'search')] | //input[@name='searchTerm']")
    _search_button = (By.XPATH, "//button[contains(text(), 'Search')] | //button[@type='submit']")
    _sort_dropdown = (By.XPATH, "//select[@name='sort'] | //label[contains(text(), 'Sort')]")
    _clear_filters_button = (By.XPATH, "//a[contains(text(), 'Clear')] | //button[contains(text(), 'Clear')]")
    _pagination_container = (By.CLASS_NAME, "pagination")
    _pagination_links = (By.XPATH, "//li[@class='next']//a | //li[@class='prev']//a | //ul[@class='pagination']//li//a")
    _export_button = (By.XPATH, "//a[contains(text(), 'Export')] | //button[contains(text(), 'Export')]")
    _print_button = (By.XPATH, "//a[contains(text(), 'Print')] | //button[contains(text(), 'Print')]")
    _instructions_section = (By.CLASS_NAME, "download-instructions")
    _instructions_text = (By.XPATH, ".//p | .//div[contains(@class, 'instruction')]")
    _license_agreement_section = (By.CLASS_NAME, "license-agreement")
    _license_text = (By.XPATH, ".//p | .//div[contains(@class, 'license')]")
    _success_message = (By.CLASS_NAME, "success")
    _error_message = (By.CLASS_NAME, "error")
    _info_message = (By.CLASS_NAME, "info")
    _warning_message = (By.CLASS_NAME, "warning")
    _file_size_cell = (By.XPATH, ".//td[contains(@class, 'size')] | .//span[contains(@class, 'file-size')]")
    _file_type_cell = (By.XPATH, ".//td[contains(@class, 'type')] | .//span[contains(@class, 'file-type')]")

    def is_page_loaded(self):
        self.logger.info("Checking if Downloads page is loaded")
        return self.is_element_visible(self._downloads_page_title)

    def is_no_downloads_message_displayed(self):
        self.logger.info("Checking if no downloads message is displayed")
        return self.is_element_visible(self._no_downloads_message)

    def get_downloads_count(self):
        self.logger.info("Getting downloads count")
        download_rows = self.driver.find_elements(*self._download_rows)
        count = len(download_rows)
        self.logger.info(f"Downloads count: {count}")
        return count

    def get_all_downloads(self):
        self.logger.info("Getting all downloads")
        download_rows = self.driver.find_elements(*self._download_rows)
        downloads = []
        for row in download_rows:
            try:
                download_info = {
                    'product_name': row.find_element(*self._product_name_cell).text if self.is_element_present(self._product_name_cell) else None,
                    'order_number': row.find_element(*self._order_number_cell).text if self.is_element_present(self._order_number_cell) else None,
                    'download_date': row.find_element(*self._download_date_cell).text if self.is_element_present(self._download_date_cell) else None,
                    'download_count': row.find_element(*self._download_count_cell).text if self.is_element_present(self._download_count_cell) else None,
                    'remaining': row.find_element(*self._download_remaining_cell).text if self.is_element_present(self._download_remaining_cell) else None,
                    'expiration': row.find_element(*self._download_expiration_cell).text if self.is_element_present(self._download_expiration_cell) else None
                }
                downloads.append(download_info)
            except:
                self.logger.warning("Failed to extract download details")
        self.logger.info(f"Retrieved {len(downloads)} downloads")
        return downloads

    def get_download_by_product_name(self, product_name):
        self.logger.info(f"Getting download by product name: {product_name}")
        download_rows = self.driver.find_elements(*self._download_rows)
        for row in download_rows:
            try:
                prod_name = row.find_element(*self._product_name_cell).text
                if prod_name == product_name:
                    return {
                        'product_name': prod_name,
                        'order_number': row.find_element(*self._order_number_cell).text if self.is_element_present(self._order_number_cell) else None,
                        'download_date': row.find_element(*self._download_date_cell).text if self.is_element_present(self._download_date_cell) else None,
                        'download_count': row.find_element(*self._download_count_cell).text if self.is_element_present(self._download_count_cell) else None,
                        'remaining': row.find_element(*self._download_remaining_cell).text if self.is_element_present(self._download_remaining_cell) else None,
                        'expiration': row.find_element(*self._download_expiration_cell).text if self.is_element_present(self._download_expiration_cell) else None
                    }
            except:
                self.logger.warning(f"Failed to find download: {product_name}")
        self.logger.error(f"Download not found: {product_name}")
        return None

    def download_by_product_name(self, product_name):
        self.logger.info(f"Downloading product: {product_name}")
        download_rows = self.driver.find_elements(*self._download_rows)
        for row in download_rows:
            try:
                prod_name = row.find_element(*self._product_name_cell).text
                if prod_name == product_name:
                    download_button = row.find_element(*self._download_button)
                    download_button.click()
                    self.logger.info(f"Downloaded product: {product_name}")
                    return True
            except:
                self.logger.warning(f"Failed to download product: {product_name}")
        self.logger.error(f"Product not found: {product_name}")
        return False

    def download_by_index(self, index):
        self.logger.info(f"Downloading at index: {index}")
        download_rows = self.driver.find_elements(*self._download_rows)
        if index >= len(download_rows):
            self.logger.error(f"Download index out of range: {index}")
            return False
        try:
            download_button = download_rows[index].find_element(*self._download_button)
            download_button.click()
            self.logger.info(f"Downloaded at index: {index}")
            return True
        except:
            self.logger.error(f"Failed to download at index: {index}")
            return False

    def is_download_available_by_product_name(self, product_name):
        self.logger.info(f"Checking if download is available: {product_name}")
        download = self.get_download_by_product_name(product_name)
        if download:
            remaining = download.get('remaining', '0')
            is_available = remaining and int(remaining) > 0
            self.logger.info(f"Download available for {product_name}: {is_available}")
            return is_available
        return False

    def is_download_expired_by_product_name(self, product_name):
        self.logger.info(f"Checking if download is expired: {product_name}")
        download = self.get_download_by_product_name(product_name)
        if download:
            expiration = download.get('expiration', '')
            is_expired = 'expired' in expiration.lower()
            self.logger.info(f"Download expired for {product_name}: {is_expired}")
            return is_expired
        return False

    def filter_by_status(self, status):
        self.logger.info(f"Filtering downloads by status: {status}")
        try:
            self.select_dropdown(self._status_filter, status)
            self.logger.info(f"Filtered by status: {status}")
            return True
        except:
            self.logger.error(f"Failed to filter by status: {status}")
            return False

    def sort_downloads(self, sort_option):
        self.logger.info(f"Sorting downloads by: {sort_option}")
        try:
            self.select_dropdown(self._sort_dropdown, sort_option)
            self.logger.info(f"Sorted by: {sort_option}")
            return True
        except:
            self.logger.error(f"Failed to sort downloads: {sort_option}")
            return False

    def search_download(self, search_term):
        self.logger.info(f"Searching for download: {search_term}")
        try:
            self.type(self._search_input, search_term)
            self.click(self._search_button)
            self.logger.info(f"Searched for download: {search_term}")
            return True
        except:
            self.logger.error(f"Failed to search for download: {search_term}")
            return False

    def clear_filters(self):
        self.logger.info("Clearing all filters")
        try:
            self.click(self._clear_filters_button)
            self.logger.info("Filters cleared")
            return True
        except:
            self.logger.error("Failed to clear filters")
            return False

    def is_pagination_visible(self):
        self.logger.info("Checking if pagination is visible")
        return self.is_element_visible(self._pagination_container)

    def go_to_next_page(self):
        self.logger.info("Going to next page")
        try:
            pagination_links = self.driver.find_elements(*self._pagination_links)
            for link in pagination_links:
                if 'next' in link.get_attribute('class').lower():
                    link.click()
                    self.logger.info("Navigated to next page")
                    return True
            self.logger.warning("Next page link not found")
            return False
        except:
            self.logger.error("Failed to navigate to next page")
            return False

    def go_to_previous_page(self):
        self.logger.info("Going to previous page")
        try:
            pagination_links = self.driver.find_elements(*self._pagination_links)
            for link in pagination_links:
                if 'prev' in link.get_attribute('class').lower():
                    link.click()
                    self.logger.info("Navigated to previous page")
                    return True
            self.logger.warning("Previous page link not found")
            return False
        except:
            self.logger.error("Failed to navigate to previous page")
            return False

    def export_downloads(self):
        self.logger.info("Exporting downloads")
        try:
            self.click(self._export_button)
            self.logger.info("Downloads exported")
            return True
        except:
            self.logger.error("Failed to export downloads")
            return False

    def print_downloads(self):
        self.logger.info("Printing downloads")
        try:
            self.click(self._print_button)
            self.logger.info("Downloads printed")
            return True
        except:
            self.logger.error("Failed to print downloads")
            return False

    def is_instructions_section_visible(self):
        self.logger.info("Checking if instructions section is visible")
        return self.is_element_visible(self._instructions_section)

    def get_instructions_text(self):
        self.logger.info("Getting instructions text")
        try:
            instructions = self.get_text(self._instructions_text)
            self.logger.info(f"Instructions: {instructions}")
            return instructions
        except:
            self.logger.error("Failed to get instructions")
            return None

    def is_license_agreement_visible(self):
        self.logger.info("Checking if license agreement is visible")
        return self.is_element_visible(self._license_agreement_section)

    def get_license_text(self):
        self.logger.info("Getting license agreement text")
        try:
            license_text = self.get_text(self._license_text)
            self.logger.info(f"License text retrieved")
            return license_text
        except:
            self.logger.error("Failed to get license text")
            return None

    def is_success_message_displayed(self):
        self.logger.info("Checking if success message is displayed")
        return self.is_element_visible(self._success_message)

    def get_success_message(self):
        self.logger.info("Getting success message")
        try:
            message = self.get_text(self._success_message)
            self.logger.info(f"Success message: {message}")
            return message
        except:
            self.logger.error("Failed to get success message")
            return None

    def is_error_message_displayed(self):
        self.logger.info("Checking if error message is displayed")
        return self.is_element_visible(self._error_message)

    def get_error_message(self):
        self.logger.info("Getting error message")
        try:
            message = self.get_text(self._error_message)
            self.logger.warning(f"Error message: {message}")
            return message
        except:
            self.logger.error("Failed to get error message")
            return None

    def is_info_message_displayed(self):
        self.logger.info("Checking if info message is displayed")
        return self.is_element_visible(self._info_message)

    def get_info_message(self):
        self.logger.info("Getting info message")
        try:
            message = self.get_text(self._info_message)
            self.logger.info(f"Info message: {message}")
            return message
        except:
            self.logger.error("Failed to get info message")
            return None

    def is_warning_message_displayed(self):
        self.logger.info("Checking if warning message is displayed")
        return self.is_element_visible(self._warning_message)

    def get_warning_message(self):
        self.logger.info("Getting warning message")
        try:
            message = self.get_text(self._warning_message)
            self.logger.warning(f"Warning message: {message}")
            return message
        except:
            self.logger.error("Failed to get warning message")
            return None

    def get_total_downloads_count(self):
        self.logger.info("Getting total downloads count from label")
        try:
            count_text = self.get_text(self._downloads_page_title)
            # Extract count from title if it contains number
            import re
            match = re.search(r'\d+', count_text)
            if match:
                count = int(match.group())
                self.logger.info(f"Total downloads count: {count}")
                return count
            return 0
        except Exception as e:
            self.logger.error(f"Failed to get total downloads count: {e}")
            return 0

    def download_all_visible_downloads(self):
        self.logger.info("Downloading all visible downloads")
        try:
            download_rows = self.find_elements(self._download_rows)
            success_count = 0
            for index, row in enumerate(download_rows):
                try:
                    download_button_elem = row.find_elements(*self._download_button)
                    if download_button_elem:
                        download_button_elem[0].click()
                        success_count += 1
                        self.logger.debug(f"Downloaded item {index + 1}")
                except Exception as e:
                    self.logger.warning(f"Failed to download item {index + 1}: {e}")
            self.logger.info(f"Downloaded {success_count} out of {len(download_rows)} items")
            return success_count == len(download_rows)
        except Exception as e:
            self.logger.error(f"Failed to download all downloads: {e}")
            return False

    def filter_and_sort_downloads(self, status=None, sort_option=None):
        self.logger.info(f"Filtering by status: {status}, sorting by: {sort_option}")
        try:
            if status:
                self.filter_by_status(status)
            if sort_option:
                self.sort_downloads(sort_option)
            self.logger.info("Filter and sort applied successfully")
            return True
        except Exception as e:
            self.logger.error(f"Failed to filter and sort: {e}")
            return False

    def get_expired_downloads(self):
        self.logger.info("Getting expired downloads")
        try:
            downloads = self.get_all_downloads()
            expired = [d for d in downloads if d and 'Expired' in str(d.get('status', ''))]
            self.logger.info(f"Found {len(expired)} expired downloads")
            return expired
        except Exception as e:
            self.logger.error(f"Failed to get expired downloads: {e}")
            return []

    def get_active_downloads(self):
        self.logger.info("Getting active downloads")
        try:
            downloads = self.get_all_downloads()
            active = [d for d in downloads if d and 'Active' in str(d.get('status', ''))]
            self.logger.info(f"Found {len(active)} active downloads")
            return active
        except Exception as e:
            self.logger.error(f"Failed to get active downloads: {e}")
            return []

    def check_download_availability(self, product_name):
        self.logger.info(f"Checking availability for product: {product_name}")
        try:
            download = self.get_download_by_product_name(product_name)
            if download:
                status = download.get('status', '').lower()
                is_available = 'expired' not in status and 'unavailable' not in status
                self.logger.info(f"Product {product_name} availability: {is_available}")
                return is_available
            self.logger.warning(f"Product not found: {product_name}")
            return False
        except Exception as e:
            self.logger.error(f"Failed to check availability: {e}")
            return False

    def get_downloads_with_remaining_count(self):
        self.logger.info("Getting downloads with remaining download count")
        try:
            downloads = self.get_all_downloads()
            downloads_with_remaining = [d for d in downloads if d and d.get('remaining')]
            self.logger.info(f"Found {len(downloads_with_remaining)} downloads with remaining count")
            return downloads_with_remaining
        except Exception as e:
            self.logger.error(f"Failed to get downloads with remaining count: {e}")
            return []

    def get_downloads_expiring_soon(self, days_threshold=7):
        self.logger.info(f"Getting downloads expiring within {days_threshold} days")
        try:
            from datetime import datetime, timedelta
            downloads = self.get_all_downloads()
            expiring_soon = []
            threshold_date = datetime.now() + timedelta(days=days_threshold)
            
            for d in downloads:
                if d and d.get('expiration'):
                    try:
                        exp_date = datetime.strptime(str(d.get('expiration')), '%Y-%m-%d')
                        if exp_date <= threshold_date:
                            expiring_soon.append(d)
                    except:
                        pass
            
            self.logger.info(f"Found {len(expiring_soon)} downloads expiring soon")
            return expiring_soon
        except Exception as e:
            self.logger.error(f"Failed to get expiring downloads: {e}")
            return []

    def get_download_count_statistics(self):
        self.logger.info("Getting download count statistics")
        try:
            downloads = self.get_all_downloads()
            total = len(downloads)
            active = len(self.get_active_downloads())
            expired = len(self.get_expired_downloads())
            
            stats = {
                'total_downloads': total,
                'active_downloads': active,
                'expired_downloads': expired,
                'percentage_active': (active / total * 100) if total > 0 else 0
            }
            self.logger.info(f"Download statistics: {stats}")
            return stats
        except Exception as e:
            self.logger.error(f"Failed to get statistics: {e}")
            return {}

    def is_download_available_by_index(self, index):
        self.logger.info(f"Checking if download at index {index} is available")
        try:
            download_rows = self.find_elements(self._download_rows)
            if index < len(download_rows):
                status_elem = download_rows[index].find_elements(*self._transaction_status_cell)
                if status_elem:
                    status = status_elem[0].text.lower()
                    is_available = 'expired' not in status and 'unavailable' not in status
                    self.logger.info(f"Download at index {index} availability: {is_available}")
                    return is_available
            self.logger.warning(f"Index out of range: {index}")
            return False
        except Exception as e:
            self.logger.error(f"Failed to check availability: {e}")
            return False

    def bulk_search_downloads(self, search_terms_list):
        self.logger.info(f"Bulk searching for downloads: {search_terms_list}")
        try:
            results = {}
            for search_term in search_terms_list:
                self.search_download(search_term)
                results[search_term] = self.get_all_downloads()
                self.clear_filters()
            self.logger.info(f"Bulk search completed for {len(results)} terms")
            return results
        except Exception as e:
            self.logger.error(f"Failed to bulk search: {e}")
            return {}

    def is_user_authenticated(self):
        self.logger.info("Checking if user is authenticated")
        try:
            user_menu = self.driver.find_element(By.XPATH, "//a[contains(@class, 'account')] | //span[contains(@class, 'username')]")
            return user_menu.is_displayed()
        except:
            return False

    def is_login_required(self):
        self.logger.info("Checking if login is required")
        try:
            login_prompt = self.driver.find_element(By.XPATH, "//div[contains(text(), 'login')] | //a[contains(text(), 'Log in')]")
            return login_prompt.is_displayed()
        except:
            return False

    def is_access_denied_message_displayed(self):
        self.logger.info("Checking if access denied message is displayed")
        try:
            access_denied = self.driver.find_element(By.XPATH, "//div[contains(text(), 'access')] | //div[contains(text(), 'denied')] | //div[contains(text(), 'not authorized')]")
            return access_denied.is_displayed()
        except:
            return False



    def has_downloadable_items(self):
        self.logger.info("Checking if page has downloadable items")
        try:
            items = self.driver.find_elements(*self._download_items)
            return len(items) > 0
        except:
            return False

    def is_purchase_confirmed(self):
        self.logger.info("Checking if purchase is confirmed")
        try:
            confirmation = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Purchased')] | //span[contains(text(), 'Order')] | //div[contains(@class, 'order-info')]")
            return confirmation.is_displayed()
        except:
            return False

    def are_download_items_visible(self):
        self.logger.info("Checking if download items are visible")
        items = self.driver.find_elements(*self._download_items)
        if not items:
            return False
        return all(item.is_displayed() for item in items[:3]) if len(items) > 0 else False

    def is_purchase_restriction_error_displayed(self):
        self.logger.info("Checking if purchase restriction error is displayed")
        try:
            error = self.driver.find_element(By.XPATH, "//div[contains(text(), 'purchase')] | //div[contains(text(), 'not available')] | //span[contains(text(), 'restricted')]")
            return error.is_displayed()
        except:
            return False
