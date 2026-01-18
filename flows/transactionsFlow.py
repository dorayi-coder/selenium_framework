from pages.transactionsPage import TransactionsPage
from utilities.customLogger import LoggerFactory


class TransactionsFlow:
    logger = LoggerFactory.get_logger(__name__)

    def __init__(self, driver):
        self.driver = driver
        self.transactions_page = TransactionsPage(driver)

    def wait_for_transactions_page_to_load(self):
        self.logger.info("Waiting for Transactions page to load")
        self.transactions_page.handle_cloudflare_if_present()
        if not self.transactions_page.is_page_loaded():
            self.logger.error("Transactions page failed to load")
            raise Exception("Transactions page failed to load")
        self.logger.info("Transactions page loaded successfully")

    def navigate_to_transactions(self):
        self.logger.info("Navigating to Transactions page")
        self.wait_for_transactions_page_to_load()
        self.logger.info("Transactions page ready")

    def verify_transactions_page_loaded(self):
        self.logger.info("Verifying Transactions page is loaded")
        self.wait_for_transactions_page_to_load()
        is_loaded = self.transactions_page.is_page_loaded()
        if is_loaded:
            self.logger.info("Transactions page verified as loaded")
        else:
            self.logger.error("Transactions page verification failed")
        return is_loaded

    def verify_no_transactions_exist(self):
        self.logger.info("Verifying no transactions exist")
        self.navigate_to_transactions()
        is_empty = self.transactions_page.is_no_transactions_message_displayed()
        if is_empty:
            self.logger.info("No transactions found as expected")
        else:
            self.logger.warning("Transactions are present")
        return is_empty

    def get_all_transactions(self):
        self.logger.info("Getting all transactions")
        self.navigate_to_transactions()
        transactions = self.transactions_page.get_all_transactions()
        self.logger.info(f"Retrieved {len(transactions)} transactions")
        return transactions

    def get_transaction_count(self):
        self.logger.info("Getting transaction count")
        self.navigate_to_transactions()
        count = self.transactions_page.get_transactions_count()
        self.logger.info(f"Transaction count: {count}")
        return count

    def get_transaction_details(self, transaction_id):
        self.logger.info(f"Getting details for transaction: {transaction_id}")
        self.navigate_to_transactions()
        transaction = self.transactions_page.get_transaction_by_id(transaction_id)
        if transaction:
            self.logger.info(f"Transaction details retrieved: {transaction}")
        else:
            self.logger.warning(f"Transaction not found: {transaction_id}")
        return transaction

    def view_transaction_by_id(self, transaction_id):
        self.logger.info(f"Viewing transaction: {transaction_id}")
        self.navigate_to_transactions()
        success = self.transactions_page.view_transaction_by_id(transaction_id)
        if success:
            self.logger.info(f"Transaction viewed: {transaction_id}")
        else:
            self.logger.error(f"Failed to view transaction: {transaction_id}")
        return success

    def download_receipt(self, transaction_id):
        self.logger.info(f"Downloading receipt for transaction: {transaction_id}")
        self.navigate_to_transactions()
        success = self.transactions_page.download_receipt_by_id(transaction_id)
        if success:
            self.logger.info(f"Receipt downloaded for transaction: {transaction_id}")
        else:
            self.logger.error(f"Failed to download receipt for transaction: {transaction_id}")
        return success

    def initiate_refund(self, transaction_id):
        self.logger.info(f"Initiating refund for transaction: {transaction_id}")
        self.navigate_to_transactions()
        success = self.transactions_page.refund_transaction_by_id(transaction_id)
        if success:
            self.logger.info(f"Refund initiated for transaction: {transaction_id}")
        else:
            self.logger.error(f"Failed to initiate refund for transaction: {transaction_id}")
        return success

    def filter_transactions_by_type(self, transaction_type):
        self.logger.info(f"Filtering transactions by type: {transaction_type}")
        self.navigate_to_transactions()
        success = self.transactions_page.filter_by_type(transaction_type)
        if success:
            transactions = self.transactions_page.get_transactions_by_type(transaction_type)
            self.logger.info(f"Found {len(transactions)} transactions of type {transaction_type}")
            return transactions
        else:
            self.logger.error(f"Failed to filter by type: {transaction_type}")
            return []

    def filter_transactions_by_status(self, status):
        self.logger.info(f"Filtering transactions by status: {status}")
        self.navigate_to_transactions()
        success = self.transactions_page.filter_by_status(status)
        if success:
            transactions = self.transactions_page.get_transactions_by_status(status)
            self.logger.info(f"Found {len(transactions)} transactions with status {status}")
            return transactions
        else:
            self.logger.error(f"Failed to filter by status: {status}")
            return []

    def filter_transactions_by_amount_range(self, amount_range):
        self.logger.info(f"Filtering transactions by amount range: {amount_range}")
        self.navigate_to_transactions()
        success = self.transactions_page.filter_by_amount_range(amount_range)
        if success:
            self.logger.info(f"Filtered by amount range: {amount_range}")
        else:
            self.logger.error(f"Failed to filter by amount range: {amount_range}")
        return success

    def filter_transactions_by_date_range(self, from_date, to_date):
        self.logger.info(f"Filtering transactions by date range: {from_date} to {to_date}")
        self.navigate_to_transactions()
        success = self.transactions_page.filter_by_date_range(from_date, to_date)
        if success:
            self.logger.info(f"Filtered by date range: {from_date} to {to_date}")
        else:
            self.logger.error(f"Failed to filter by date range")
        return success

    def sort_transactions(self, sort_option):
        self.logger.info(f"Sorting transactions by: {sort_option}")
        self.navigate_to_transactions()
        success = self.transactions_page.sort_transactions(sort_option)
        if success:
            self.logger.info(f"Transactions sorted by: {sort_option}")
        else:
            self.logger.error(f"Failed to sort transactions")
        return success

    def search_transactions(self, search_term):
        self.logger.info(f"Searching for transactions: {search_term}")
        self.navigate_to_transactions()
        success = self.transactions_page.search_transaction(search_term)
        if success:
            self.logger.info(f"Search completed for: {search_term}")
        else:
            self.logger.error(f"Failed to search for transactions")
        return success

    def clear_all_filters(self):
        self.logger.info("Clearing all transaction filters")
        self.navigate_to_transactions()
        success = self.transactions_page.clear_filters()
        if success:
            self.logger.info("All filters cleared")
        else:
            self.logger.error("Failed to clear filters")
        return success

    def export_transactions_data(self):
        self.logger.info("Exporting transactions data")
        self.navigate_to_transactions()
        success = self.transactions_page.export_transactions()
        if success:
            self.logger.info("Transactions data exported")
        else:
            self.logger.error("Failed to export transactions")
        return success

    def print_transactions_data(self):
        self.logger.info("Printing transactions data")
        self.navigate_to_transactions()
        success = self.transactions_page.print_transactions()
        if success:
            self.logger.info("Transactions data printed")
        else:
            self.logger.error("Failed to print transactions")
        return success

    def change_currency(self, currency):
        self.logger.info(f"Changing currency to: {currency}")
        self.navigate_to_transactions()
        success = self.transactions_page.select_currency(currency)
        if success:
            self.logger.info(f"Currency changed to: {currency}")
        else:
            self.logger.error(f"Failed to change currency")
        return success

    def get_total_transaction_amount(self):
        self.logger.info("Getting total transaction amount")
        self.navigate_to_transactions()
        transactions = self.transactions_page.get_all_transactions()
        total = 0
        for transaction in transactions:
            try:
                # Remove currency symbols and convert to float
                amount_str = str(transaction.get('amount', '0')).replace('$', '').replace(',', '')
                total += float(amount_str)
            except (ValueError, AttributeError):
                self.logger.warning(f"Failed to parse amount: {transaction.get('amount')}")
        self.logger.info(f"Total transaction amount: {total}")
        return total

    def verify_transaction_status(self, transaction_id, expected_status):
        self.logger.info(f"Verifying transaction {transaction_id} has status {expected_status}")
        transaction = self.get_transaction_details(transaction_id)
        if transaction:
            actual_status = transaction.get('status', '').lower()
            expected_status_lower = expected_status.lower()
            if actual_status == expected_status_lower:
                self.logger.info(f"Transaction status verified: {expected_status}")
                return True
            else:
                self.logger.error(f"Status mismatch. Expected: {expected_status}, Got: {actual_status}")
                return False
        return False

    def navigate_to_next_page(self):
        self.logger.info("Navigating to next transactions page")
        self.navigate_to_transactions()
        success = self.transactions_page.go_to_next_page()
        if success:
            self.logger.info("Navigated to next page successfully")
        else:
            self.logger.warning("Could not navigate to next page")
        return success

    def navigate_to_previous_page(self):
        self.logger.info("Navigating to previous transactions page")
        self.navigate_to_transactions()
        success = self.transactions_page.go_to_previous_page()
        if success:
            self.logger.info("Navigated to previous page successfully")
        else:
            self.logger.warning("Could not navigate to previous page")
        return success
