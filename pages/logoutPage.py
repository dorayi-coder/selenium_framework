from selenium.webdriver.common.by import By
from utilities.basePage import BasePage
from utilities.customLogger import LoggerFactory


class LogoutPage(BasePage):
    logger = LoggerFactory.get_logger(__name__)
    # AI hints for intelligent locator suggestion
        self.logger.info("Checking if logout option is visible")
        return self.is_element_visible(self._logout_link) or self.is_element_visible(self._logout_button)

    def is_user_logged_in(self):
        self.logger.info("Checking if user is logged in")
        return self.is_element_visible(self._logged_in_indicator)

    def click_logout(self):
        self.logger.info("Clicking logout link")
        if self.is_element_visible(self._logout_link):
            self.click(self._logout_link)
        elif self.is_element_visible(self._logout_button):
            self.click(self._logout_button)
        else:
            self.logger.error("Logout option not found")
            raise Exception("Logout option not found on page")

    def is_logout_successful(self):
        self.logger.info("Checking if logout was successful")
        return self.is_element_visible(self._login_page_title)

    def is_user_logged_out(self):
        self.logger.info("Checking if user is logged out")
        logged_out = not self.is_user_logged_in()
        return logged_out

    def click_account_dropdown(self):
        self.logger.info("Clicking account dropdown")
        if self.is_element_visible(self._account_dropdown):
            self.click(self._account_dropdown)
        else:
            self.logger.error("Account dropdown not found")
            raise Exception("Account dropdown not found on page")

    def logout_from_dropdown(self):
        self.logger.info("Logging out via account dropdown")
        self.click_account_dropdown()
        self.click_logout()
