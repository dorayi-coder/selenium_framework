from pages.logoutPage import LogoutPage
from utilities.customLogger import LoggerFactory


class LogoutFlow:
    logger = LoggerFactory.get_logger(__name__)

    def __init__(self, driver):
        self.driver = driver
        self.logout_page = LogoutPage(driver)

    def logout_user(self):
        self.logger.info("Initiating user logout")
        self.logout_page.handle_cloudflare_if_present()
        if not self.logout_page.is_logout_option_visible():
            self.logger.error("Logout option not available")
            raise Exception("Logout option not available on current page")
        self.logout_page.click_logout()
        self.logger.info("User logout completed")

    def logout_user_from_dropdown(self):
        self.logger.info("Initiating user logout from account dropdown")
        self.logout_page.handle_cloudflare_if_present()
        if not self.logout_page.is_logout_option_visible():
            self.logger.error("Logout option not available")
            raise Exception("Logout option not available on current page")
        self.logout_page.logout_from_dropdown()
        self.logger.info("User logout from dropdown completed")

    def verify_logout_success(self):
        self.logger.info("Verifying logout was successful")
        is_successful = self.logout_page.is_logout_successful()
        if is_successful:
            self.logger.info("Logout verification successful - user redirected to login page")
            return True
        else:
            self.logger.warning("Logout verification failed")
            return False

    def verify_user_logged_out(self):
        self.logger.info("Verifying user is logged out")
        is_logged_out = self.logout_page.is_user_logged_out()
        if is_logged_out:
            self.logger.info("User verified as logged out")
            return True
        else:
            self.logger.warning("User still appears to be logged in")
            return False

    def is_logout_option_available(self):
        self.logger.info("Checking if logout option is available")
        return self.logout_page.is_logout_option_visible()

    def is_user_currently_logged_in(self):
        self.logger.info("Checking if user is currently logged in")
        return self.logout_page.is_user_logged_in()
