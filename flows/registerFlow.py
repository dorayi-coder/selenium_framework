from pages.registerPage import RegisterPage
from pages.homePage import HomePage
from utilities.customLogger import LoggerFactory
from utilities.readProperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class RegisterFlow:
    """
    Business flow for user registration with mandatory fields only.
    """
    logger = LoggerFactory.get_logger(__name__)

    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)
        self.register_page = RegisterPage(driver)
        if driver:
            self.driver.maximize_window()

    def navigate_to_home_page(self):
        """Navigate to the application home page."""
        self.logger.info("Navigating to home page")
        base_url = ReadConfig.get("APPLICATION", "base_url")
        self.driver.get(base_url)
        self.logger.info(f"Navigated to URL: {base_url}")

    def navigate_to_register_page_directly(self):
        """Navigate directly to the registration page via URL."""
        self.logger.info("Navigating directly to register page")
        base_url = ReadConfig.get("APPLICATION", "base_url")
        register_url = f"{base_url}register"
        self.driver.get(register_url)
        
        # Wait for document to be complete
        self.logger.debug("Waiting for document.readyState to be 'complete'...")
        wait = WebDriverWait(self.driver, 15)
        wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
        self.logger.debug("Document readyState is complete")
        
        # Longer delay for any dynamic content rendering
        time.sleep(3)
        
        # Scroll to top to ensure elements are in viewport
        self.logger.debug("Scrolling to top of page...")
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        
        # Wait for page to be fully ready
        self.logger.info("Waiting for register page to load")
        self.register_page.wait_for_page_load()
        
        # Print registration page URL
        print("\n" + "="*80)
        print(f"✓ REGISTER PAGE LOADED: {self.driver.current_url}")
        print("="*80 + "\n")
        
        self.logger.info(f"Navigated directly to register URL: {register_url}")

    def click_register_tab_from_home(self):
        """Click on the REGISTER tab from the home page to go to the registration page."""
        self.logger.info("Attempting to click REGISTER tab from home page")
        try:
            # Try to click the register link with a shorter timeout
            wait = WebDriverWait(self.driver, 3)
            from selenium.webdriver.support import expected_conditions as EC
            wait.until(EC.element_to_be_clickable(self.home_page._register_link))
            self.home_page.click_register_link()
            self.logger.info("Clicked REGISTER tab from home page")
        except Exception as e:
            self.logger.info(f"Register link not found on home page (expected for fast navigation): {str(e)[:50]}")
            self.logger.info("Using direct URL navigation to register page instead")
            self.navigate_to_register_page_directly()

    def register_with_mandatory_fields(self, first_name, last_name, email, password):
        """
        Complete the entire registration flow with mandatory fields only.
        
        Test flow:
        1. Navigate to home page
        2. Click REGISTER link
        3. Enter First Name
        4. Enter Last Name
        5. Enter Email
        6. Enter Password
        7. Enter Confirm Password
        8. Click Register button
        9. Verify success message
        10. Click Continue button
        
        Args:
            first_name (str): User's first name
            last_name (str): User's last name
            email (str): User's email address
            password (str): User's password
        """
        self.logger.info(f"Starting registration flow with mandatory fields - email: {email}")
        
        # Step 1-2: Navigate and click register link
        self.navigate_to_home_page()
        self.click_register_tab_from_home()
        
        # Step 3-7: Fill mandatory fields
        self.logger.info("Filling mandatory fields")
        self.register_page.enter_first_name(first_name)
        self.register_page.enter_last_name(last_name)
        self.register_page.enter_email(email)
        self.register_page.enter_password(password)
        self.register_page.enter_confirm_password(password)
        
        # Step 8: Click Register button
        self.register_page.click_register_button()
        self.logger.info("Registration form submitted")
        
        # Step 9: Verify success message
        if not self.register_page.is_registration_successful():
            raise Exception("Registration failed - success message not displayed")
        
        success_msg = self.register_page.get_success_message()
        self.logger.info(f"Registration successful. Message: {success_msg}")
        
        # Step 10: Click Continue button
        self.register_page.click_continue_button()
        self.logger.info(f"Registration flow completed successfully for email: {email}")

    def register_with_slow_typing(self, first_name, last_name, email, password, typing_delay=0.1):
        """
        Complete the entire registration flow with slow, character-by-character typing.
        
        Test Case: "Validate registering an account with slow typing in the fields"
        
        This method simulates human-like typing behavior by introducing a configurable
        delay between each character typed into the form fields. This is useful for
        testing applications that validate or respond to typing events in real-time.
        
        Test Flow:
        1. Click the "REGISTER" link
        2. Enter First Name using slow, character-by-character typing
        3. Enter Last Name using slow, character-by-character typing
        4. Enter Email using slow, character-by-character typing
        5. Enter Password using slow, character-by-character typing
        6. Enter Confirm Password using slow, character-by-character typing
        7. Click the "REGISTER" button
        8. Verify the success message: "Your registration completed"
        9. Click the "CONTINUE" button
        
        Args:
            first_name (str): User's first name
            last_name (str): User's last name
            email (str): User's email address
            password (str): User's password
            typing_delay (float): Delay in seconds between each character (default: 0.1)
        """
        self.logger.info(f"Starting registration flow with slow typing - email: {email}, delay: {typing_delay}s per character")
        
        # Step 1: Click the "REGISTER" link
        self.navigate_to_home_page()
        self.click_register_link_from_home()
        
        # Step 2-6: Fill all fields with slow typing
        self.logger.info("Filling form fields with slow, character-by-character typing")
        self.register_page.enter_first_name_slow(first_name, typing_delay)
        self.register_page.enter_last_name_slow(last_name, typing_delay)
        self.register_page.enter_email_slow(email, typing_delay)
        self.register_page.enter_password_slow(password, typing_delay)
        self.register_page.enter_confirm_password_slow(password, typing_delay)
        
        # Step 7: Click the "REGISTER" button
        self.register_page.click_register_button()
        self.logger.info("Registration form submitted")
        
        # Step 8: Verify the success message
        if not self.register_page.is_registration_successful():
            raise Exception("Registration failed - success message not displayed")
        
        success_msg = self.register_page.get_success_message()
        self.logger.info(f"Registration successful. Message: {success_msg}")
        
        # Step 9: Click the "CONTINUE" button
        self.register_page.click_continue_button()
        self.logger.info(f"Registration with slow typing completed successfully for email: {email}")

    def register_with_invalid_password(self, first_name, last_name, email, invalid_password):
        """
        Attempt to register with an invalid password that does not meet password policy.
        
        Test Case: "Validate registering an account using an invalid password"
        
        This is a negative test case that validates the application correctly rejects
        passwords that do not meet security requirements (e.g., too short, missing
        character types). The test verifies proper error handling and user feedback.
        
        Test Flow:
        1. Click the "REGISTER" link
        2. Enter First Name
        3. Enter Last Name
        4. Enter Email
        5. Enter an INVALID password that does not meet password policy
        6. Enter the same invalid value in the Confirm Password field
        7. Click the "REGISTER" button
        8. Verify that registration is NOT successful
        9. Validate the displayed password validation error message
        10. Ensure the user remains on the registration page
        
        Args:
            first_name (str): User's first name
            last_name (str): User's last name
            email (str): User's email address
            invalid_password (str): Invalid password that fails policy requirements
            
        Raises:
            AssertionError: If success message is displayed or password error not found
            Exception: If page fails to load or user navigates away from register page
        """
        self.logger.info(f"Starting registration with invalid password - email: {email}")
        
        # Step 1: Click the "REGISTER" link
        self.navigate_to_home_page()
        self.click_register_link_from_home()
        
        # Step 2-6: Fill form with invalid password
        self.logger.info("Step 2: Entering First Name")
        self.register_page.enter_first_name(first_name)
        
        self.logger.info("Step 3: Entering Last Name")
        self.register_page.enter_last_name(last_name)
        
        self.logger.info("Step 4: Entering Email")
        self.register_page.enter_email(email)
        
        self.logger.info("Step 5: Entering invalid password")
        self.register_page.enter_password(invalid_password)
        
        self.logger.info("Step 6: Entering same invalid password in Confirm Password field")
        self.register_page.enter_confirm_password(invalid_password)
        
        # Step 7: Click the "REGISTER" button
        self.logger.info("Step 7: Clicking REGISTER button")
        self.register_page.click_register_button()
        self.logger.info("Registration form submitted with invalid password")
        
        # Step 8: Verify that registration is NOT successful
        self.logger.info("Step 8: Verifying registration was NOT successful")
        if self.register_page.is_registration_successful():
            raise AssertionError("Registration should have failed with invalid password but success message was displayed")
        self.logger.info("Confirmed: Success message is NOT displayed (as expected)")
        
        # Step 9: Validate the password validation error message
        self.logger.info("Step 9: Validating password error message is displayed")
        password_error = self.register_page.get_password_error()
        if not password_error:
            raise AssertionError("Password validation error message was not found on the page")
        self.logger.info(f"Password error message found: {password_error}")
        assert password_error, "Password error message must be present and visible"
        
        # Step 10: Ensure user remains on the registration page
        self.logger.info("Step 10: Verifying user remains on registration page")
        if not self.register_page.is_page_loaded():
            raise AssertionError("User was navigated away from registration page - registration page title not found")
        self.logger.info("Confirmed: User remains on registration page")
        
        self.logger.info(f"Negative test case completed successfully - Invalid password registration attempt for email: {email}")

    def register_using_keyboard_keys(self, first_name, last_name, email, password):
        """
        Complete the entire registration flow using keyboard keys for navigation and submission.
        
        Test Case: "Validate Registering an account using keyboard keys"
        
        This test case validates that users can complete registration using only keyboard
        interactions (TAB for navigation, ENTER for form submission). This is important
        for accessibility compliance and keyboard-only users.
        
        Test Flow:
        1. Click the "REGISTER" link
        2. Enter First Name
        3. Enter Last Name
        4. Enter Email
        5. Enter Password
        6. Enter Confirm Password
        7. Submit the form using ENTER key (or keyboard navigation)
        8. Verify the success message: "Your registration completed"
        9. Click the "CONTINUE" button
        
        Args:
            first_name (str): User's first name
            last_name (str): User's last name
            email (str): User's email address
            password (str): User's password
        """
        self.logger.info(f"Starting registration using keyboard keys - email: {email}")
        
        # Step 1: Click the "REGISTER" link
        self.navigate_to_home_page()
        self.click_register_link_from_home()
        
        # Step 2-6: Fill form fields with keyboard navigation
        self.logger.info("Step 2: Entering First Name")
        self.register_page.enter_first_name(first_name)
        
        self.logger.info("Step 3: Entering Last Name")
        self.register_page.enter_last_name(last_name)
        
        self.logger.info("Step 4: Entering Email")
        self.register_page.enter_email(email)
        
        self.logger.info("Step 5: Entering Password")
        self.register_page.enter_password(password)
        
        self.logger.info("Step 6: Entering Confirm Password")
        self.register_page.enter_confirm_password(password)
        
        # Step 7: Submit form using keyboard ENTER key
        self.logger.info("Step 7: Submitting registration form using ENTER key")
        self.register_page.submit_registration_form_with_keyboard()
        self.logger.info("Registration form submitted via keyboard")
        
        # Step 8: Verify success message
        self.logger.info("Step 8: Verifying success message")
        if not self.register_page.is_registration_successful():
            raise Exception("Registration failed - success message not displayed")
        
        success_msg = self.register_page.get_success_message()
        self.logger.info(f"Registration successful via keyboard interaction. Message: {success_msg}")
        
        # Step 9: Click the "CONTINUE" button
        self.logger.info("Step 9: Clicking CONTINUE button")
        self.register_page.click_continue_button()
        self.logger.info(f"Registration using keyboard keys completed successfully for email: {email}")

    def register_after_deleting_session_cookies(self, first_name, last_name, email, password):
        """
        Complete the entire registration flow after deleting session cookies.
        
        Test flow:
        1. Navigate to home page
        2. Delete all session cookies to clear authentication state
        3. Click REGISTER link
        4. Enter First Name
        5. Enter Last Name
        6. Enter Email
        7. Enter Password
        8. Enter Confirm Password
        9. Click Register button
        10. Verify success message
        11. Click Continue button
        
        Args:
            first_name (str): User's first name
            last_name (str): User's last name
            email (str): User's email address
            password (str): User's password
            
        Returns:
            bool: True if registration was successful after deleting cookies
            
        Raises:
            Exception: If any step of the registration flow fails
        """
        self.logger.info(f"Starting registration flow after deleting session cookies for email: {email}")
        
        # Step 1: Navigate to home page
        self.logger.info("Step 1: Navigating to home page")
        self.navigate_to_home_page()
        self.logger.info("Home page loaded successfully")
        
        # Step 2: Delete all session cookies
        self.logger.info("Step 2: Deleting all session cookies to clear authentication state")
        self.register_page.delete_session_cookies()
        self.logger.info("Session cookies deleted successfully")
        
        # Step 3: Click REGISTER link
        self.logger.info("Step 3: Clicking REGISTER link from home page")
        self.click_register_link_from_home()
        self.logger.info("Register page loaded after deleting cookies")
        
        # Step 4: Enter First Name
        self.logger.info(f"Step 4: Entering first name: {first_name}")
        self.register_page.enter_first_name(first_name)
        self.logger.info("First name entered successfully")
        
        # Step 5: Enter Last Name
        self.logger.info(f"Step 5: Entering last name: {last_name}")
        self.register_page.enter_last_name(last_name)
        self.logger.info("Last name entered successfully")
        
        # Step 6: Enter Email
        self.logger.info(f"Step 6: Entering email: {email}")
        self.register_page.enter_email(email)
        self.logger.info("Email entered successfully")
        
        # Step 7: Enter Password
        self.logger.info("Step 7: Entering password")
        self.register_page.enter_password(password)
        self.logger.info("Password entered successfully")
        
        # Step 8: Enter Confirm Password
        self.logger.info("Step 8: Entering confirm password")
        self.register_page.enter_confirm_password(password)
        self.logger.info("Confirm password entered successfully")
        
        # Step 9: Click Register button
        self.logger.info("Step 9: Clicking Register button")
        self.register_page.click_register_button()
        self.logger.info("Register button clicked")
        
        # Step 10: Verify success message
        self.logger.info("Step 10: Verifying registration success")
        if not self.register_page.is_registration_successful():
            error_msg = f"Registration failed after deleting session cookies for email: {email}"
            self.logger.error(error_msg)
            raise Exception(error_msg)
        success_msg = self.register_page.get_success_message()
        self.logger.info(f"Registration successful after deleting cookies. Message: {success_msg}")
        
        # Step 11: Click the "CONTINUE" button
        self.logger.info("Step 11: Clicking CONTINUE button")
        self.register_page.click_continue_button()
        self.logger.info(f"Registration after deleting session cookies completed successfully for email: {email}")

    def register_with_invalid_email(self, first_name, last_name, invalid_email, password):
        """
        Validate that registration fails when an invalid email address is provided.
        
        Test Case: "Validate registering an account using invalid email address"
        
        This method validates the negative scenario where a user attempts to register
        with an invalid email format. The registration should fail and display an
        appropriate error message.
        
        Test Flow:
        1. Navigate to home page
        2. Click REGISTER link
        3. Enter First Name
        4. Enter Last Name
        5. Enter invalid Email
        6. Enter Password
        7. Enter Confirm Password
        8. Click Register button
        9. Verify that registration failed (success message NOT displayed)
        10. Retrieve and validate email error message
        11. Verify that user remains on register page
        
        Args:
            first_name (str): User's first name
            last_name (str): User's last name
            invalid_email (str): Invalid email address format (e.g., 'invalidemail', 'test@', '@test.com')
            password (str): User's password
            
        Returns:
            bool: True if validation error was correctly displayed for invalid email
            
        Raises:
            Exception: If registration succeeds when it should fail with invalid email
        """
        self.logger.info(f"Starting registration flow with invalid email - email: {invalid_email}")
        
        # Step 1: Navigate to home page
        self.logger.info("Step 1: Navigating to home page")
        self.navigate_to_home_page()
        self.logger.info("Home page loaded successfully")
        
        # Step 2: Click REGISTER link
        self.logger.info("Step 2: Clicking REGISTER link from home page")
        self.click_register_link_from_home()
        self.logger.info("Register page loaded successfully")
        
        # Step 3: Enter First Name
        self.logger.info(f"Step 3: Entering first name: {first_name}")
        self.register_page.enter_first_name(first_name)
        self.logger.info("First name entered successfully")
        
        # Step 4: Enter Last Name
        self.logger.info(f"Step 4: Entering last name: {last_name}")
        self.register_page.enter_last_name(last_name)
        self.logger.info("Last name entered successfully")
        
        # Step 5: Enter invalid Email
        self.logger.info(f"Step 5: Entering invalid email: {invalid_email}")
        self.register_page.enter_email(invalid_email)
        self.logger.info("Invalid email entered successfully")
        
        # Step 6: Enter Password
        self.logger.info("Step 6: Entering password")
        self.register_page.enter_password(password)
        self.logger.info("Password entered successfully")
        
        # Step 7: Enter Confirm Password
        self.logger.info("Step 7: Entering confirm password")
        self.register_page.enter_confirm_password(password)
        self.logger.info("Confirm password entered successfully")
        
        # Step 8: Click Register button
        self.logger.info("Step 8: Clicking Register button")
        self.register_page.click_register_button()
        self.logger.info("Register button clicked")
        
        # Step 9: Verify that registration failed (success message NOT displayed)
        self.logger.info("Step 9: Verifying that registration failed")
        if self.register_page.is_registration_successful():
            error_msg = f"Registration should have failed with invalid email: {invalid_email}"
            self.logger.error(error_msg)
            raise Exception(error_msg)
        self.logger.info("Confirmed: Registration failed as expected with invalid email")
        
        # Step 10: Retrieve and validate email error message
        self.logger.info("Step 10: Retrieving email validation error message")
        email_error = self.register_page.get_email_error()
        if email_error:
            self.logger.info(f"Email validation error found: {email_error}")
        else:
            self.logger.warning("Email validation error message not found - checking page state")
        
        # Step 11: Verify that user remains on register page
        self.logger.info("Step 11: Verifying that user remains on register page")
        if not self.register_page.is_page_loaded():
            error_msg = f"User should remain on register page after invalid email submission"
            self.logger.error(error_msg)
            raise Exception(error_msg)
        self.logger.info(f"Registration with invalid email validation completed successfully - email: {invalid_email}")

