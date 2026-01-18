from selenium.webdriver.common.by import By
from utilities.basePage import BasePage
from utilities.customLogger import LoggerFactory


class TransactionsPage(BasePage):
    logger = LoggerFactory.get_logger(__name__)
    # AI hints for intelligent locator suggestion
    def is_page_loaded(self):
        self.logger.info("Checking if Transactions page is loaded")
        return self.is_element_visible(self._transactions_page_title)

    def is_no_transactions_message_displayed(self):
        self.logger.info("Checking if no transactions message is displayed")
        return self.is_element_visible(self._no_transactions_message)

    def get_transactions_count(self):
        self.logger.info("Getting transactions count")
        transaction_rows = self.find_elements(self._transaction_rows)
        count = len(transaction_rows)
        self.logger.info(f"Transactions count: {count}")
        return count

    def get_all_transactions(self):
        self.logger.info("Getting all transactions")
        transaction_rows = self.find_elements(self._transaction_rows)
        transactions = []
        for row in transaction_rows:
            try:
                transaction_id_elem = row.find_elements(*self._transaction_id_cell)
                transaction_type_elem = row.find_elements(*self._transaction_type_cell)
                transaction_amount_elem = row.find_elements(*self._transaction_amount_cell)
                transaction_date_elem = row.find_elements(*self._transaction_date_cell)
                transaction_status_elem = row.find_elements(*self._transaction_status_cell)
                transaction_method_elem = row.find_elements(*self._transaction_method_cell)

                transaction_info = {
                    'id': transaction_id_elem[0].text if transaction_id_elem else None,
                    'type': transaction_type_elem[0].text if transaction_type_elem else None,
                    'amount': transaction_amount_elem[0].text if transaction_amount_elem else None,
                    'date': transaction_date_elem[0].text if transaction_date_elem else None,
                    'status': transaction_status_elem[0].text if transaction_status_elem else None,
                    'method': transaction_method_elem[0].text if transaction_method_elem else None
                }
                transactions.append(transaction_info)
            except Exception as e:
                self.logger.warning(f"Failed to extract transaction details: {e}")
        self.logger.info(f"Retrieved {len(transactions)} transactions")
        return transactions

    def get_transaction_by_id(self, transaction_id):
        self.logger.info(f"Getting transaction by ID: {transaction_id}")
        transaction_rows = self.find_elements(self._transaction_rows)
        for row in transaction_rows:
            try:
                transaction_id_elem = row.find_elements(*self._transaction_id_cell)
                if transaction_id_elem and transaction_id_elem[0].text == transaction_id:
                    transaction_type_elem = row.find_elements(*self._transaction_type_cell)
                    transaction_amount_elem = row.find_elements(*self._transaction_amount_cell)
                    transaction_date_elem = row.find_elements(*self._transaction_date_cell)
                    transaction_status_elem = row.find_elements(*self._transaction_status_cell)
                    transaction_method_elem = row.find_elements(*self._transaction_method_cell)

                    return {
                        'id': transaction_id,
                        'type': transaction_type_elem[0].text if transaction_type_elem else None,
                        'amount': transaction_amount_elem[0].text if transaction_amount_elem else None,
                        'date': transaction_date_elem[0].text if transaction_date_elem else None,
                        'status': transaction_status_elem[0].text if transaction_status_elem else None,
                        'method': transaction_method_elem[0].text if transaction_method_elem else None
                    }
            except Exception as e:
                self.logger.warning(f"Failed to find transaction: {e}")
        self.logger.error(f"Transaction not found: {transaction_id}")
        return None

    def get_transactions_by_type(self, transaction_type):
        self.logger.info(f"Getting transactions by type: {transaction_type}")
        transaction_rows = self.find_elements(self._transaction_rows)
        transactions = []
        for row in transaction_rows:
            try:
                transaction_type_elem = row.find_elements(*self._transaction_type_cell)
                if transaction_type_elem and transaction_type_elem[0].text == transaction_type:
                    transaction_id_elem = row.find_elements(*self._transaction_id_cell)
                    transaction_amount_elem = row.find_elements(*self._transaction_amount_cell)
                    transaction_date_elem = row.find_elements(*self._transaction_date_cell)
                    transaction_status_elem = row.find_elements(*self._transaction_status_cell)

                    transactions.append({
                        'id': transaction_id_elem[0].text if transaction_id_elem else None,
                        'type': transaction_type,
                        'amount': transaction_amount_elem[0].text if transaction_amount_elem else None,
                        'date': transaction_date_elem[0].text if transaction_date_elem else None,
                        'status': transaction_status_elem[0].text if transaction_status_elem else None
                    })
            except Exception as e:
                self.logger.warning(f"Failed to extract transaction: {e}")
        self.logger.info(f"Retrieved {len(transactions)} transactions of type {transaction_type}")
        return transactions

    def get_transactions_by_status(self, status):
        self.logger.info(f"Getting transactions by status: {status}")
        transaction_rows = self.find_elements(self._transaction_rows)
        transactions = []
        for row in transaction_rows:
            try:
                transaction_status_elem = row.find_elements(*self._transaction_status_cell)
                if transaction_status_elem and transaction_status_elem[0].text == status:
                    transaction_id_elem = row.find_elements(*self._transaction_id_cell)
                    transaction_type_elem = row.find_elements(*self._transaction_type_cell)
                    transaction_amount_elem = row.find_elements(*self._transaction_amount_cell)
                    transaction_date_elem = row.find_elements(*self._transaction_date_cell)

                    transactions.append({
                        'id': transaction_id_elem[0].text if transaction_id_elem else None,
                        'type': transaction_type_elem[0].text if transaction_type_elem else None,
                        'amount': transaction_amount_elem[0].text if transaction_amount_elem else None,
                        'date': transaction_date_elem[0].text if transaction_date_elem else None,
                        'status': status
                    })
            except Exception as e:
                self.logger.warning(f"Failed to extract transaction: {e}")
        self.logger.info(f"Retrieved {len(transactions)} transactions with status {status}")
        return transactions

    def view_transaction_by_id(self, transaction_id):
        self.logger.info(f"Viewing transaction: {transaction_id}")
        transaction_rows = self.find_elements(self._transaction_rows)
        for row in transaction_rows:
            try:
                transaction_id_elem = row.find_elements(*self._transaction_id_cell)
                if transaction_id_elem and transaction_id_elem[0].text == transaction_id:
                    view_button_elem = row.find_elements(*self._view_transaction_button)
                    if view_button_elem:
                        view_button_elem[0].click()
                        self.logger.info(f"Clicked view for transaction: {transaction_id}")
                        return True
            except Exception as e:
                self.logger.warning(f"Failed to view transaction: {e}")
        self.logger.error(f"Transaction not found: {transaction_id}")
        return False

    def download_receipt_by_id(self, transaction_id):
        self.logger.info(f"Downloading receipt for transaction: {transaction_id}")
        transaction_rows = self.find_elements(self._transaction_rows)
        for row in transaction_rows:
            try:
                transaction_id_elem = row.find_elements(*self._transaction_id_cell)
                if transaction_id_elem and transaction_id_elem[0].text == transaction_id:
                    receipt_button_elem = row.find_elements(*self._download_receipt_button)
                    if receipt_button_elem:
                        receipt_button_elem[0].click()
                        self.logger.info(f"Downloaded receipt for transaction: {transaction_id}")
                        return True
            except Exception as e:
                self.logger.warning(f"Failed to download receipt: {e}")
        self.logger.error(f"Transaction not found: {transaction_id}")
        return False

    def refund_transaction_by_id(self, transaction_id):
        self.logger.info(f"Initiating refund for transaction: {transaction_id}")
        transaction_rows = self.find_elements(self._transaction_rows)
        for row in transaction_rows:
            try:
                transaction_id_elem = row.find_elements(*self._transaction_id_cell)
                if transaction_id_elem and transaction_id_elem[0].text == transaction_id:
                    refund_button_elem = row.find_elements(*self._refund_button)
                    if refund_button_elem:
                        refund_button_elem[0].click()
                        self.logger.info(f"Refund initiated for transaction: {transaction_id}")
                        return True
            except Exception as e:
                self.logger.warning(f"Failed to refund transaction: {e}")
        self.logger.error(f"Transaction not found: {transaction_id}")
        return False

    def filter_by_type(self, transaction_type):
        self.logger.info(f"Filtering transactions by type: {transaction_type}")
        try:
            self.select_dropdown_by_text(self._type_filter, transaction_type)
            self.logger.info(f"Filtered by type: {transaction_type}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to filter by type: {e}")
            return False

    def filter_by_status(self, status):
        self.logger.info(f"Filtering transactions by status: {status}")
        try:
            self.select_dropdown_by_text(self._status_filter, status)
            self.logger.info(f"Filtered by status: {status}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to filter by status: {e}")
            return False

    def filter_by_amount_range(self, amount_range):
        self.logger.info(f"Filtering transactions by amount range: {amount_range}")
        try:
            self.select_dropdown_by_text(self._amount_filter, amount_range)
            self.logger.info(f"Filtered by amount range: {amount_range}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to filter by amount range: {e}")
            return False

    def filter_by_date_range(self, from_date, to_date):
        self.logger.info(f"Filtering transactions by date range: {from_date} to {to_date}")
        try:
            self.type(self._date_filter_from, from_date)
            self.type(self._date_filter_to, to_date)
            self.logger.info(f"Filtered by date range")
            return True
        except Exception as e:
            self.logger.error(f"Failed to filter by date range: {e}")
            return False

    def sort_transactions(self, sort_option):
        self.logger.info(f"Sorting transactions by: {sort_option}")
        try:
            self.select_dropdown_by_text(self._sort_dropdown, sort_option)
            self.logger.info(f"Sorted by: {sort_option}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to sort transactions: {e}")
            return False

    def search_transaction(self, search_term):
        self.logger.info(f"Searching for transaction: {search_term}")
        try:
            self.type(self._search_input, search_term)
            self.click(self._search_button)
            self.logger.info(f"Searched for transaction: {search_term}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to search for transaction: {e}")
            return False

    def clear_filters(self):
        self.logger.info("Clearing all filters")
        try:
            self.click(self._clear_filters_button)
            self.logger.info("Filters cleared")
            return True
        except Exception as e:
            self.logger.error(f"Failed to clear filters: {e}")
            return False

    def go_to_next_page(self):
        self.logger.info("Going to next page")
        try:
            pagination_links = self.find_elements(self._pagination_links)
            for link in pagination_links:
                link_class = link.get_attribute('class')
                if link_class and 'next' in link_class.lower():
                    link.click()
                    self.logger.info("Navigated to next page")
                    return True
            self.logger.warning("Next page link not found")
            return False
        except Exception as e:
            self.logger.error(f"Failed to navigate to next page: {e}")
            return False

    def go_to_previous_page(self):
        self.logger.info("Going to previous page")
        try:
            pagination_links = self.find_elements(self._pagination_links)
            for link in pagination_links:
                link_class = link.get_attribute('class')
                if link_class and 'prev' in link_class.lower():
                    link.click()
                    self.logger.info("Navigated to previous page")
                    return True
            self.logger.warning("Previous page link not found")
            return False
        except Exception as e:
            self.logger.error(f"Failed to navigate to previous page: {e}")
            return False

    def export_transactions(self):
        self.logger.info("Exporting transactions")
        try:
            self.click(self._export_button)
            self.logger.info("Transactions exported")
            return True
        except Exception as e:
            self.logger.error(f"Failed to export transactions: {e}")
            return False

    def print_transactions(self):
        self.logger.info("Printing transactions")
        try:
            self.click(self._print_button)
            self.logger.info("Transactions printed")
            return True
        except Exception as e:
            self.logger.error(f"Failed to print transactions: {e}")
            return False

    def select_currency(self, currency):
        self.logger.info(f"Selecting currency: {currency}")
        try:
            self.select_dropdown_by_text(self._currency_selector, currency)
            self.logger.info(f"Currency selected: {currency}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to select currency: {e}")
            return False

    def get_success_message(self):
        self.logger.info("Getting success message")
        try:
            message = self.get_text(self._success_message)
            self.logger.info("Success message retrieved")
            return message
        except Exception as e:
            self.logger.error(f"Failed to get success message: {e}")
            return None

    def get_error_message(self):
        self.logger.info("Getting error message")
        try:
            message = self.get_text(self._error_message)
            self.logger.warning("Error message retrieved")
            return message
        except Exception as e:
            self.logger.error(f"Failed to get error message: {e}")
            return None

    def get_warning_message(self):
        self.logger.info("Getting warning message")
        try:
            message = self.get_text(self._warning_message)
            self.logger.warning("Warning message retrieved")
            return message
        except Exception as e:
            self.logger.error(f"Failed to get warning message: {e}")
            return None

    def get_info_message(self):
        self.logger.info("Getting info message")
        try:
            message = self.get_text(self._info_message)
            self.logger.info("Info message retrieved")
            return message
        except Exception as e:
            self.logger.error(f"Failed to get info message: {e}")
            return None
