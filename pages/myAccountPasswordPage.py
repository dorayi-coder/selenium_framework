from selenium.webdriver.common.by import By
from utilities.basePage import BasePage
from utilities.customLogger import LoggerFactory


class MyAccountPasswordPage(BasePage):
    logger = LoggerFactory.get_logger(__name__)
   
    _password_page_title = (By.XPATH, "//h1[contains(text(), 'Password')] | //h1[contains(text(), 'Change')]")
    _old_password_input = (By.ID, "OldPassword")
    _new_password_input = (By.ID, "NewPassword")
    _confirm_password_input = (By.ID, "ConfirmNewPassword")
    _save_button = (By.XPATH, "//button[contains(text(), 'Save')]")
    _cancel_button = (By.XPATH, "//button[contains(text(), 'Cancel')]")
    _success_message = (By.CLASS_NAME, "success")
    _error_message = (By.CLASS_NAME, "error")
    _validation_error = (By.CLASS_NAME, "field-validation-error")
    _password_mismatch_error = (By.XPATH, "//span[contains(text(), 'match')] | //span[contains(text(), 'confirm')]")
    _old_password_error = (By.XPATH, "//span[contains(text(), 'Old password')] | //span[contains(text(), 'current')]")

    def is_page_loaded(self):
        self.logger.info("Checking if Change Password page is loaded")
        return self.is_element_visible(self._password_page_title)

    def enter_old_password(self, password):
        self.logger.info("Entering old password")
        self.type(self._old_password_input, password)

    def enter_new_password(self, password):
        self.logger.info("Entering new password")
        self.type(self._new_password_input, password)

    def enter_confirm_password(self, password):
        self.logger.info("Entering confirm password")
        self.type(self._confirm_password_input, password)

    def save_password_changes(self):
        self.logger.info("Saving password changes")
        self.click(self._save_button)

    def cancel_password_changes(self):
        self.logger.info("Cancelling password changes")
        self.click(self._cancel_button)

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

    def is_old_password_error_displayed(self):
        self.logger.info("Checking if old password error is displayed")
        return self.is_element_visible(self._old_password_error)

    def get_old_password_error(self):
        self.logger.info("Getting old password error message")
        try:
            error = self.get_text(self._old_password_error)
            self.logger.warning(f"Old password error: {error}")
            return error
        except:
            self.logger.error("Failed to get old password error")
            return None

    def is_password_mismatch_error_displayed(self):
        self.logger.info("Checking if password mismatch error is displayed")
        return self.is_element_visible(self._password_mismatch_error)

    def get_password_mismatch_error(self):
        self.logger.info("Getting password mismatch error message")
        try:
            error = self.get_text(self._password_mismatch_error)
            self.logger.warning(f"Password mismatch error: {error}")
            return error
        except:
            self.logger.error("Failed to get password mismatch error")
            return None
