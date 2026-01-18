from selenium.webdriver.common.by import By
from utilities.basePage import BasePage
from utilities.customLogger import LoggerFactory


class OrderHistoryPage(BasePage):
    logger = LoggerFactory.get_logger(__name__)

    _order_history_page_title = (By.XPATH, "//h1[contains(text(), 'Order')] | //h1[contains(text(), 'History')]")
    _orders_container = (By.CLASS_NAME, "orders-container")
    _order_rows = (By.XPATH, "//table[contains(@class, 'order')]//tbody//tr | //div[contains(@class, 'order-item')]")
    _order_number_cell = (By.XPATH, ".//td[1]//a | .//span[contains(@class, 'order-number')]")
    _order_date_cell = (By.XPATH, ".//td[2] | .//span[contains(@class, 'order-date')]")
    _order_status_cell = (By.XPATH, ".//td[3] | .//span[contains(@class, 'order-status')]")
    _order_total_cell = (By.XPATH, ".//td[4] | .//span[contains(@class, 'order-total')]")
    _view_order_button = (By.XPATH, ".//a[contains(text(), 'View')] | .//button[contains(text(), 'View')]")
    _download_invoice_button = (By.XPATH, ".//a[contains(text(), 'Invoice')] | .//button[contains(text(), 'Invoice')]")
    _re_order_button = (By.XPATH, ".//a[contains(text(), 'Re-order')] | .//button[contains(text(), 'Re-order')]")
    _cancel_order_button = (By.XPATH, ".//a[contains(text(), 'Cancel')] | .//button[contains(text(), 'Cancel')]")
    _no_orders_message = (By.XPATH, "//div[contains(text(), 'no order')] | //p[contains(text(), 'no order')]")
    _orders_table = (By.XPATH, "//table[contains(@class, 'order')]")
    _pagination_container = (By.CLASS_NAME, "pagination")
    _pagination_links = (By.XPATH, "//li[@class='next']//a | //li[@class='prev']//a | //ul[@class='pagination']//li//a")
    _filter_section = (By.CLASS_NAME, "filter-section")
    _status_filter = (By.XPATH, "//select[@name='orderStatus'] | //label[contains(text(), 'Status')]")
    _sort_dropdown = (By.XPATH, "//select[@name='sort'] | //label[contains(text(), 'Sort')]")
    _search_input = (By.XPATH, "//input[contains(@placeholder, 'order')] | //input[@name='searchTerm']")
    _search_button = (By.XPATH, "//button[contains(text(), 'Search')] | //button[@type='submit']")
    _clear_filters_button = (By.XPATH, "//a[contains(text(), 'Clear')] | //button[contains(text(), 'Clear')]")
    _export_button = (By.XPATH, "//a[contains(text(), 'Export')] | //button[contains(text(), 'Export')]")
    _success_message = (By.CLASS_NAME, "success")
    _error_message = (By.CLASS_NAME, "error")
    _warning_message = (By.CLASS_NAME, "warning")
    _order_count_label = (By.XPATH, "//span[contains(text(), 'orders')] | //div[contains(@class, 'order-count')]")

    def is_page_loaded(self):
        self.logger.info("Checking if Order History page is loaded")
        return self.is_element_visible(self._order_history_page_title)

    def is_no_orders_message_displayed(self):
        self.logger.info("Checking if no orders message is displayed")
        return self.is_element_visible(self._no_orders_message)

    def get_orders_count(self):
        self.logger.info("Getting orders count")
        order_rows = self.driver.find_elements(*self._order_rows)
        count = len(order_rows)
        self.logger.info(f"Orders count: {count}")
        return count

    def get_all_orders(self):
        self.logger.info("Getting all orders")
        order_rows = self.driver.find_elements(*self._order_rows)
        orders = []
        for row in order_rows:
            try:
                order_info = {
                    'number': row.find_element(*self._order_number_cell).text if self.is_element_present(self._order_number_cell) else None,
                    'date': row.find_element(*self._order_date_cell).text if self.is_element_present(self._order_date_cell) else None,
                    'status': row.find_element(*self._order_status_cell).text if self.is_element_present(self._order_status_cell) else None,
                    'total': row.find_element(*self._order_total_cell).text if self.is_element_present(self._order_total_cell) else None
                }
                orders.append(order_info)
            except:
                self.logger.warning("Failed to extract order details")
        self.logger.info(f"Retrieved {len(orders)} orders")
        return orders

    def get_order_by_number(self, order_number):
        self.logger.info(f"Getting order by number: {order_number}")
        order_rows = self.driver.find_elements(*self._order_rows)
        for row in order_rows:
            try:
                order_num = row.find_element(*self._order_number_cell).text
                if order_num == order_number:
                    return {
                        'number': order_num,
                        'date': row.find_element(*self._order_date_cell).text if self.is_element_present(self._order_date_cell) else None,
                        'status': row.find_element(*self._order_status_cell).text if self.is_element_present(self._order_status_cell) else None,
                        'total': row.find_element(*self._order_total_cell).text if self.is_element_present(self._order_total_cell) else None
                    }
            except:
                self.logger.warning(f"Failed to find order: {order_number}")
        self.logger.error(f"Order not found: {order_number}")
        return None

    def view_order_by_number(self, order_number):
        self.logger.info(f"Viewing order: {order_number}")
        order_rows = self.driver.find_elements(*self._order_rows)
        for row in order_rows:
            try:
                order_num = row.find_element(*self._order_number_cell).text
                if order_num == order_number:
                    view_button = row.find_element(*self._view_order_button)
                    view_button.click()
                    self.logger.info(f"Clicked view for order: {order_number}")
                    return True
            except:
                self.logger.warning(f"Failed to view order: {order_number}")
        self.logger.error(f"Order not found: {order_number}")
        return False

    def view_order_by_index(self, index):
        self.logger.info(f"Viewing order at index: {index}")
        order_rows = self.driver.find_elements(*self._order_rows)
        if index >= len(order_rows):
            self.logger.error(f"Order index out of range: {index}")
            return False
        try:
            view_button = order_rows[index].find_element(*self._view_order_button)
            view_button.click()
            self.logger.info(f"Clicked view for order at index: {index}")
            return True
        except:
            self.logger.error(f"Failed to view order at index: {index}")
            return False

    def download_invoice_by_number(self, order_number):
        self.logger.info(f"Downloading invoice for order: {order_number}")
        order_rows = self.driver.find_elements(*self._order_rows)
        for row in order_rows:
            try:
                order_num = row.find_element(*self._order_number_cell).text
                if order_num == order_number:
                    invoice_button = row.find_element(*self._download_invoice_button)
                    invoice_button.click()
                    self.logger.info(f"Downloaded invoice for order: {order_number}")
                    return True
            except:
                self.logger.warning(f"Failed to download invoice for order: {order_number}")
        self.logger.error(f"Order not found: {order_number}")
        return False

    def download_invoice_by_index(self, index):
        self.logger.info(f"Downloading invoice for order at index: {index}")
        order_rows = self.driver.find_elements(*self._order_rows)
        if index >= len(order_rows):
            self.logger.error(f"Order index out of range: {index}")
            return False
        try:
            invoice_button = order_rows[index].find_element(*self._download_invoice_button)
            invoice_button.click()
            self.logger.info(f"Downloaded invoice for order at index: {index}")
            return True
        except:
            self.logger.error(f"Failed to download invoice at index: {index}")
            return False

    def re_order_by_number(self, order_number):
        self.logger.info(f"Re-ordering from order: {order_number}")
        order_rows = self.driver.find_elements(*self._order_rows)
        for row in order_rows:
            try:
                order_num = row.find_element(*self._order_number_cell).text
                if order_num == order_number:
                    re_order_button = row.find_element(*self._re_order_button)
                    re_order_button.click()
                    self.logger.info(f"Clicked re-order for order: {order_number}")
                    return True
            except:
                self.logger.warning(f"Failed to re-order from order: {order_number}")
        self.logger.error(f"Order not found: {order_number}")
        return False

    def re_order_by_index(self, index):
        self.logger.info(f"Re-ordering from order at index: {index}")
        order_rows = self.driver.find_elements(*self._order_rows)
        if index >= len(order_rows):
            self.logger.error(f"Order index out of range: {index}")
            return False
        try:
            re_order_button = order_rows[index].find_element(*self._re_order_button)
            re_order_button.click()
            self.logger.info(f"Clicked re-order for order at index: {index}")
            return True
        except:
            self.logger.error(f"Failed to re-order at index: {index}")
            return False

    def cancel_order_by_number(self, order_number):
        self.logger.info(f"Cancelling order: {order_number}")
        order_rows = self.driver.find_elements(*self._order_rows)
        for row in order_rows:
            try:
                order_num = row.find_element(*self._order_number_cell).text
                if order_num == order_number:
                    cancel_button = row.find_element(*self._cancel_order_button)
                    cancel_button.click()
                    self.logger.info(f"Clicked cancel for order: {order_number}")
                    return True
            except:
                self.logger.warning(f"Failed to cancel order: {order_number}")
        self.logger.error(f"Order not found: {order_number}")
        return False

    def cancel_order_by_index(self, index):
        self.logger.info(f"Cancelling order at index: {index}")
        order_rows = self.driver.find_elements(*self._order_rows)
        if index >= len(order_rows):
            self.logger.error(f"Order index out of range: {index}")
            return False
        try:
            cancel_button = order_rows[index].find_element(*self._cancel_order_button)
            cancel_button.click()
            self.logger.info(f"Clicked cancel for order at index: {index}")
            return True
        except:
            self.logger.error(f"Failed to cancel order at index: {index}")
            return False

    def filter_by_status(self, status):
        self.logger.info(f"Filtering orders by status: {status}")
        try:
            status_dropdown = self.driver.find_element(*self._status_filter)
            self.select_dropdown(self._status_filter, status)
            self.logger.info(f"Filtered by status: {status}")
            return True
        except:
            self.logger.error(f"Failed to filter by status: {status}")
            return False

    def sort_orders(self, sort_option):
        self.logger.info(f"Sorting orders by: {sort_option}")
        try:
            self.select_dropdown(self._sort_dropdown, sort_option)
            self.logger.info(f"Sorted by: {sort_option}")
            return True
        except:
            self.logger.error(f"Failed to sort orders: {sort_option}")
            return False

    def search_order(self, search_term):
        self.logger.info(f"Searching for order: {search_term}")
        try:
            self.type(self._search_input, search_term)
            self.click(self._search_button)
            self.logger.info(f"Searched for order: {search_term}")
            return True
        except:
            self.logger.error(f"Failed to search for order: {search_term}")
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

    def get_order_total_by_number(self, order_number):
        """Get total amount for a specific order by order number."""
        self.logger.info(f"Getting total for order: {order_number}")
        try:
            order_rows = self.driver.find_elements(*self._order_rows)
            for row in order_rows:
                try:
                    order_num = row.find_element(*self._order_number_cell).text
                    if order_num == order_number or order_number in order_num:
                        total = row.find_element(*self._order_total_cell).text
                        self.logger.info(f"Order total for {order_number}: {total}")
                        return total
                except:
                    continue
            self.logger.warning(f"Total not found for order: {order_number}")
            return None
        except:
            self.logger.error(f"Failed to get total for order: {order_number}")
            return None

    def is_pagination_visible(self):
        self.logger.info("Checking if pagination is visible")
        return self.is_element_visible(self._pagination_container)

    def is_order_table_visible(self):
        self.logger.info("Checking if order table is visible")
        return self.is_element_visible(self._orders_table)

    def is_order_columns_visible(self):
        self.logger.info("Checking if order columns are visible")
        try:
            rows = self.driver.find_elements(*self._order_rows)
            return len(rows) > 0
        except:
            return False


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

    def export_orders(self):
        self.logger.info("Exporting orders")
        try:
            self.click(self._export_button)
            self.logger.info("Orders exported")
            return True
        except:
            self.logger.error("Failed to export orders")
            return False

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
    def go_to_next_page(self):
        """Navigate to next page in pagination."""
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

