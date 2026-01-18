from pages.forgotPasswordPage import ForgotPasswordPage
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from pages.resetPasswordPage import ResetPasswordPage
from utilities.customLogger import LoggerFactory


class ForgotPasswordFlow:
    """
    Forgot Password / Password Recovery Business Flow.
    
    Orchestrates the password recovery journey by composing page-level actions.
    Follows clean architecture principles:
    - No raw locators (all delegated to page objects)
    - No assertions (caller responsible for verification)
    - Returns observable UI outcomes (messages, page state)
    - Reusable by Pytest tests and CI pipelines
    - Strictly separates navigation, UI interaction, and outcome capture
    
    Business Flow:
    1. Click "LOG IN" link on the home page
    2. Click "Forgot password?" link on the login page
    3. Verify navigation to password recovery page
    4. Enter email address into recovery field
    5. Click "RECOVER" button
    6. Capture and expose confirmation message
    """
    
    logger = LoggerFactory.get_logger(__name__)

    def __init__(self, driver):
        """
        Initialize the forgot password flow with page objects.
        
        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.home_page = HomePage(driver)
        self.login_page = LoginPage(driver)
        self.forgot_password_page = ForgotPasswordPage(driver)
        self.reset_password_page = ResetPasswordPage(driver)

    # ===== Page Load Verification Methods =====
    def wait_for_forgot_password_page_to_load(self):
        """
        Wait for the password recovery page to fully load and become interactive.
        Handles Cloudflare bypass if necessary.
        
        Raises:
            Exception: If forgot password page fails to load within timeout
        """
        self.logger.info("Waiting for Forgot Password page to load")
        self.forgot_password_page.handle_cloudflare_if_present()
        if not self.forgot_password_page.is_page_loaded():
            self.logger.error("Forgot Password page failed to load")
            raise Exception("Forgot Password page failed to load")
        self.logger.info("Forgot Password page loaded successfully")

    def wait_for_reset_password_page_to_load(self):
        """
        Wait for the reset password page (post-recovery-link-click) to fully load.
        Handles Cloudflare bypass if necessary.
        
        Raises:
            Exception: If reset password page fails to load within timeout
        """
        self.logger.info("Waiting for Reset Password page to load")
        self.reset_password_page.handle_cloudflare_if_present()
        if not self.reset_password_page.is_page_loaded():
            self.logger.error("Reset Password page failed to load")
            raise Exception("Reset Password page failed to load")
        self.logger.info("Reset Password page loaded successfully")

    # ===== Core Password Recovery Workflow =====
    def navigate_to_password_recovery(self):
        """
        Execute the navigation sequence from home page to password recovery page.
        
        Workflow:
        1. Click the "LOG IN" link on the home page
        2. Click the "Forgot password?" link on the login page
        3. Verify arrival at password recovery page
        
        Raises:
            Exception: If navigation fails or page fails to load
        """
        self.logger.info("Starting navigation to password recovery page")
        
        # Step 1: Click login link on home page
        self.logger.info("Step 1: Clicking LOG IN link on home page")
        self.home_page.click_login_link()
        self.logger.info("LOG IN link clicked")
        
        # Step 2: Click forgot password link on login page
        self.logger.info("Step 2: Clicking Forgot password? link on login page")
        self.login_page.click_forgot_password()
        self.logger.info("Forgot password? link clicked")
        
        # Step 3: Verify arrival at password recovery page
        self.logger.info("Step 3: Verifying navigation to password recovery page")
        self.wait_for_forgot_password_page_to_load()
        self.logger.info("Successfully navigated to password recovery page")

    def request_password_recovery(self, email):
        """
        Execute the password recovery request workflow.
        
        Assumes the password recovery page is already loaded.
        
        Workflow:
        1. Enter email address into the recovery email field
        2. Click the "RECOVER" button
        3. Wait briefly for response
        
        Args:
            email (str): The email address to request recovery for
            
        Note:
            Does not perform assertions. Caller verifies recovery success 
            via get_recovery_confirmation_message() or is_recovery_confirmed()
        """
        self.logger.info(f"Requesting password recovery for email: {email}")
        self.wait_for_forgot_password_page_to_load()
        
        # Step 1: Enter email
        self.logger.info(f"Entering email: {email}")
        self.forgot_password_page.enter_email(email)
        
        # Step 2: Submit recovery request
        self.logger.info("Submitting password recovery request")
        self.forgot_password_page.submit_recovery_request()
        
        self.logger.info(f"Password recovery request submitted for email: {email}")

    # ===== Complete Password Recovery Workflow (Navigation + Recovery) =====
    def recover_password_via_email(self, email):
        """
        Execute the COMPLETE password recovery workflow from start to finish.
        
        Workflow:
        1. Navigate from home → login → forgot password page
        2. Enter email address
        3. Submit recovery request
        4. Return the confirmation message (observable outcome)
        
        Args:
            email (str): The email address to request password recovery for
            
        Returns:
            dict: Observable UI outcome containing:
                - 'success': bool indicating if confirmation message appeared
                - 'message': str containing confirmation/error message
                - 'page_url': str of final page URL
                
        Note:
            Does not perform assertions. Caller determines test success 
            by examining returned message content.
        """
        self.logger.info(f"Starting complete password recovery workflow for email: {email}")
        
        # Navigate to password recovery
        self.navigate_to_password_recovery()
        
        # Request recovery
        self.request_password_recovery(email)
        
        # Capture observable UI outcome
        confirmation_message = self.get_recovery_confirmation_message()
        is_confirmed = self.is_recovery_confirmed()
        
        self.logger.info(f"Password recovery workflow complete. Confirmation: {is_confirmed}, Message: {confirmation_message}")
        
        return {
            'success': is_confirmed,
            'message': confirmation_message,
            'page_url': self.driver.current_url
        }

    # ===== Observable UI Outcome Methods (for test verification) =====
    def is_recovery_confirmed(self):
        """
        Check if the password recovery has been confirmed by checking for 
        the confirmation message on the page.
        
        Returns:
            bool: True if confirmation message is visible, False otherwise
        """
        self.logger.info("Verifying recovery confirmation")
        return self.forgot_password_page.is_recovery_confirmation_displayed()

    def get_recovery_confirmation_message(self):
        """
        Retrieve the password recovery confirmation message.
        This message confirms that a reset link has been sent to the email.
        
        Returns:
            str: The confirmation message text, or None if not displayed
        """
        self.logger.info("Retrieving recovery confirmation message")
        return self.forgot_password_page.get_recovery_confirmation_message()

    def is_recovery_email_sent(self):
        """
        Check if the recovery email has been sent (success state).
        
        Returns:
            bool: True if success message visible, False otherwise
        """
        self.logger.info("Verifying recovery email was sent")
        return self.forgot_password_page.is_recovery_email_sent()

    def get_recovery_success_message(self):
        """
        Retrieve the success message if displayed.
        
        Returns:
            str: Success message text, or None if not present
        """
        self.logger.info("Retrieving recovery success message")
        return self.forgot_password_page.get_success_message()

    # ===== Error Outcome Methods (for test verification) =====
    def get_recovery_request_error(self):
        """
        Retrieve any error message from the recovery request.
        This could indicate server errors or invalid email scenarios.
        
        Returns:
            str: The error message text, or None if no error displayed
        """
        self.logger.info("Retrieving recovery request error")
        return self.forgot_password_page.get_error_message()

    def is_recovery_error_displayed(self):
        """
        Check if any error is displayed on the password recovery page.
        
        Returns:
            bool: True if error is visible, False otherwise
        """
        self.logger.info("Checking if recovery error is displayed")
        return self.forgot_password_page.is_any_error_displayed()

    def get_recovery_validation_errors(self):
        """
        Collect all validation errors on the recovery page.
        Useful for form submission validation scenarios.
        
        Returns:
            dict: Dictionary of field names and their validation errors
        """
        self.logger.info("Collecting recovery validation errors")
        errors = {}

        email_error = self.forgot_password_page.get_email_validation_error()
        if email_error:
            errors["email"] = email_error
            
        general_error = self.forgot_password_page.get_error_message()
        if general_error:
            errors["general"] = general_error

        self.logger.info(f"Recovery validation errors found: {errors}")
        return errors

    # ===== Password Reset Actions (POST-Recovery Link Click) =====
    def reset_password_with_new_password(self, new_password):
        """
        Execute password reset with a new password.
        Assumes the reset password page has been accessed via recovery link.
        
        Args:
            new_password (str): The new password to set
            
        Note:
            Does not perform assertions. Caller verifies reset success.
        """
        self.logger.info("Resetting password with new password")
        self.wait_for_reset_password_page_to_load()
        self.reset_password_page.enter_new_password(new_password)
        self.reset_password_page.enter_confirm_password(new_password)
        self.reset_password_page.submit_reset_password()
        self.logger.info("Password reset submitted")

    def reset_password_with_mismatched_passwords(self, new_password, confirm_password):
        """
        Attempt password reset with mismatched passwords.
        Useful for testing validation logic.
        
        Args:
            new_password (str): The new password
            confirm_password (str): The confirmation password (intentionally different)
            
        Note:
            Does not perform assertions. Caller verifies validation error display.
        """
        self.logger.info("Attempting password reset with mismatched passwords")
        self.wait_for_reset_password_page_to_load()
        self.reset_password_page.enter_new_password(new_password)
        self.reset_password_page.enter_confirm_password(confirm_password)
        self.reset_password_page.submit_reset_password()
        self.logger.info("Password reset attempted with mismatched passwords")

    # ===== Password Reset Observable Outcome Methods =====
    def is_password_reset_successful(self):
        """
        Check if the password reset has been successful.
        
        Returns:
            bool: True if success message is visible, False otherwise
        """
        self.logger.info("Verifying password reset success")
        return self.reset_password_page.is_password_reset_successful()

    def get_password_reset_success_message(self):
        """
        Retrieve the password reset success message.
        
        Returns:
            str: Success message text, or None if not displayed
        """
        self.logger.info("Retrieving password reset success message")
        return self.reset_password_page.get_success_message()

    def get_password_reset_error(self):
        """
        Retrieve any error message from password reset.
        
        Returns:
            str: The error message text, or None if no error displayed
        """
        self.logger.info("Retrieving password reset error")
        return self.reset_password_page.get_error_message()

    def get_password_reset_validation_errors(self):
        """
        Collect all validation errors on the reset password page.
        
        Returns:
            dict: Dictionary of field names and their validation errors
        """
        self.logger.info("Collecting password reset validation errors")
        errors = {}

        new_password_error = self.reset_password_page.get_new_password_error()
        if new_password_error:
            errors["new_password"] = new_password_error

        confirm_password_error = self.reset_password_page.get_confirm_password_error()
        if confirm_password_error:
            errors["confirm_password"] = confirm_password_error

        general_error = self.reset_password_page.get_error_message()
        if general_error:
            errors["general"] = general_error

        self.logger.info(f"Reset password validation errors found: {errors}")
        return errors

    def verify_recovery_email_sent(self):
        """
        Verify that the password recovery email has been sent.
        
        Returns:
            bool: True if recovery email sent confirmation is visible, False otherwise
        """
        self.logger.info("Verifying recovery email was sent")
        return self.is_recovery_email_sent()

    def initiate_and_complete_password_reset(self, email, new_password):
        self.logger.info(f"Initiating complete password reset flow for email: {email}")
        self.request_password_recovery(email)
        if self.verify_recovery_email_sent():
            self.logger.info("Recovery email sent successfully. Ready for password reset.")
            return True
        else:
            self.logger.error("Recovery email not sent. Cannot complete password reset.")
            return False

    def navigate_back_to_login_from_forgot_password(self):
        self.logger.info("Navigating back to login from Forgot Password page")
        self.wait_for_forgot_password_page_to_load()
        self.forgot_password_page.click_back_to_login()
        self.logger.info("Navigation to login page initiated")

    def navigate_back_to_login_from_reset_password(self):
        self.logger.info("Navigating back to login from Reset Password page")
        self.wait_for_reset_password_page_to_load()
        self.reset_password_page.click_back_to_login()
        self.logger.info("Navigation to login page initiated")
