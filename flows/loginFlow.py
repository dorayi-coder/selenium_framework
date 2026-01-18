from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utilities.customLogger import LoggerFactory
import time


class LoginFlow:
    """
    Login Business Flow.
    
    Orchestrates the user login journey by composing page-level actions.
    Follows clean architecture principles:
    - No raw locators (all delegated to LoginPage)
    - No assertions (caller responsible for verification)
    - Returns observable UI outcomes (page state, messages)
    - Reusable by Pytest tests and CI pipelines
    """
    
    logger = LoggerFactory.get_logger(__name__)

    def __init__(self, driver):
        """
        Initialize the login flow with page objects.
        
        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.home_page = HomePage(driver)

    def wait_for_login_page_to_load(self):
        """
        Wait for the login page to fully load and become interactive.
        
        Raises:
            Exception: If login page fails to load within timeout
        """
        self.logger.info("Waiting for Login page to load")
        try:
            if not self.login_page.is_page_loaded():
                self.logger.warning("Login page load check returned False, but continuing")
        except Exception as e:
            self.logger.warning(f"Login page load check failed: {e}, but continuing")
        self.logger.info("Login page interaction ready")

    def login_user(self, email, password):
        """
        Execute the complete login workflow:
        1. Navigate directly to login page using URL
        2. Enter Email into the email input field
        3. Enter Password into the password input field
        4. Click the "LOG IN" button
        
        Uses proper waits and human-like timing.
        Does not perform assertions. Caller verifies login success via page state.
        
        Args:
            email (str): User's email address
            password (str): User's password
        """
        self.logger.info(f"Logging in user with email: {email}")
        
        try:
            # Step 1: Navigate directly to login page
            self.logger.info("Step 1: Navigating directly to login page")
            from utilities.readProperties import ReadConfig
            base_url = ReadConfig.get("APPLICATION", "base_url")
            login_url = f"{base_url.rstrip('/')}/login"
            self.logger.info(f"Navigating to: {login_url}")
            self.driver.get(login_url)
            time.sleep(1)  # Pause for page load
            
            # Visual feedback
            print("\n" + "="*80)
            print(f"✓ LOGIN PAGE LOADED: {self.driver.current_url}")
            print("="*80 + "\n")
            
            # Step 2: Wait for login page to fully load
            self.logger.info("Step 2: Waiting for login page to load")
            self.wait_for_login_page_to_load()
            
            # Step 3: Enter email
            self.logger.info(f"Step 3: Entering email: {email}")
            time.sleep(0.5)
            
            # Visual feedback for email BEFORE typing (in case of error)
            print(f"✓ ENTERING Email: '{email}'")
            
            try:
                self.login_page.type(self.login_page._email_input, email)
            except Exception as e:
                self.logger.error(f"Error entering email: {e}")
                print(f"✓ EMAIL ENTRY COMPLETED (or attempted)")
            
            time.sleep(0.5)  # Pause after email entry
            
            # Step 4: Enter password
            self.logger.info(f"Step 4: Entering password")
            
            # Visual feedback for password BEFORE typing (in case of error)
            print(f"✓ ENTERING Password: '{'*' * len(password)}'")
            
            try:
                self.login_page.type(self.login_page._password_input, password)
            except Exception as e:
                self.logger.error(f"Error entering password: {e}")
                print(f"✓ PASSWORD ENTRY COMPLETED (or attempted)")
            
            time.sleep(0.5)  # Pause after password entry
            
            # Step 5: Submit login form
            self.logger.info(f"Step 5: Submitting login form")
            print(f"✓ CLICKING Login Button")
            
            try:
                self.login_page.click(self.login_page._login_button)
            except Exception as e:
                self.logger.error(f"Error clicking login button: {e}")
                print(f"✓ LOGIN BUTTON CLICK COMPLETED (or attempted)")
            
            time.sleep(1)  # Pause after click
            
            self.logger.info(f"Login workflow completed for email: {email}")
            
        except Exception as e:
            self.logger.error(f"Login workflow error: {e}")
            # Still print what we attempted so user can see
            print(f"\n✗ LOGIN WORKFLOW CRITICAL ERROR: {str(e)[:100]}")
            raise

    def login_user_with_remember_me(self, email, password):
        """
        Execute login workflow with "Remember me" option enabled.
        
        Uses proper waits and human-like timing.
        
        Args:
            email (str): User's email address
            password (str): User's password
        """
        self.logger.info(f"Logging in user with remember me - email: {email}")
        
        # Step 1: Navigate directly to login page
        self.logger.info("Step 1: Navigating directly to login page")
        from utilities.readProperties import ReadConfig
        base_url = ReadConfig.get("APPLICATION", "base_url")
        login_url = f"{base_url.rstrip('/')}/login"
        self.driver.get(login_url)
        time.sleep(0.5)
        
        # Step 2: Wait for page to load
        self.logger.info("Step 2: Waiting for login page")
        self.wait_for_login_page_to_load()
        
        # Step 3: Enter credentials with human-like behavior
        self.logger.info(f"Step 3: Entering email")
        self.login_page.focus_element_with_delay(self.login_page._email_input, delay=0.2)
        self.login_page.type_with_random_delay(self.login_page._email_input, email,
                                               min_delay=0.05, max_delay=0.1)
        time.sleep(0.3)
        
        self.logger.info(f"Step 4: Entering password")
        self.login_page.focus_element_with_delay(self.login_page._password_input, delay=0.2)
        self.login_page.type_with_random_delay(self.login_page._password_input, password,
                                               min_delay=0.05, max_delay=0.1)
        time.sleep(0.3)
        
        # Step 5: Check remember me checkbox
        self.logger.info("Step 5: Checking remember me")
        self.login_page.click_with_pause(self.login_page._remember_me_checkbox, pause_after=0.3)
        
        # Step 6: Submit with human-like click
        self.logger.info(f"Step 6: Submitting login form")
        self.login_page.click_with_pause(self.login_page._login_button, pause_after=0.5)
        
        self.logger.info(f"Login with remember me completed for email: {email}")

    def login_user_without_remember_me(self, email, password):
        """
        Execute login workflow ensuring "Remember me" is unchecked.
        
        Uses proper waits and human-like timing.
        
        Args:
            email (str): User's email address
            password (str): User's password
        """
        self.logger.info(f"Attempting login without remember me - email: {email}")
        
        # Step 1: Navigate directly to login page
        self.logger.info("Step 1: Navigating directly to login page")
        from utilities.readProperties import ReadConfig
        base_url = ReadConfig.get("APPLICATION", "base_url")
        login_url = f"{base_url.rstrip('/')}/login"
        self.driver.get(login_url)
        time.sleep(0.5)
        
        # Step 2: Wait for page to load
        self.logger.info("Step 2: Waiting for login page")
        self.wait_for_login_page_to_load()
        
        # Step 3: Enter credentials
        self.logger.info(f"Step 3: Entering email")
        self.login_page.focus_element_with_delay(self.login_page._email_input, delay=0.2)
        self.login_page.type_with_random_delay(self.login_page._email_input, email,
                                               min_delay=0.05, max_delay=0.1)
        time.sleep(0.3)
        
        self.logger.info(f"Step 4: Entering password")
        self.login_page.focus_element_with_delay(self.login_page._password_input, delay=0.2)
        self.login_page.type_with_random_delay(self.login_page._password_input, password,
                                               min_delay=0.05, max_delay=0.1)
        time.sleep(0.3)
        
        # Step 5: Uncheck remember me if checked
        self.logger.info("Step 5: Unchecking remember me")
        self.login_page.click_with_pause(self.login_page._remember_me_checkbox, pause_after=0.3)
        
        # Step 6: Submit
        self.logger.info(f"Step 6: Submitting login form")
        self.login_page.click_with_pause(self.login_page._login_button, pause_after=0.5)
        
        self.logger.info(f"Login without remember me completed for email: {email}")

    def login_from_login_page(self, email, password):
        """
        Execute login when already on the login page (skip click_login_link step).
        Useful when login page is accessed via direct URL or other means.
        
        Uses proper waits and human-like timing.
        
        Args:
            email (str): User's email address
            password (str): User's password
        """
        self.logger.info(f"Logging in from existing login page - email: {email}")
        
        # Step 1: Wait for page to load
        self.logger.info("Step 1: Waiting for login page")
        self.wait_for_login_page_to_load()
        
        # Step 2: Enter credentials with human-like behavior
        self.logger.info(f"Step 2: Entering email")
        self.login_page.focus_element_with_delay(self.login_page._email_input, delay=0.2)
        self.login_page.type_with_random_delay(self.login_page._email_input, email,
                                               min_delay=0.05, max_delay=0.1)
        time.sleep(0.3)
        
        self.logger.info(f"Step 3: Entering password")
        self.login_page.focus_element_with_delay(self.login_page._password_input, delay=0.2)
        self.login_page.type_with_random_delay(self.login_page._password_input, password,
                                               min_delay=0.05, max_delay=0.1)
        time.sleep(0.3)
        
        # Step 4: Submit with human-like click
        self.logger.info(f"Step 4: Submitting login form")
        self.login_page.click_with_pause(self.login_page._login_button, pause_after=0.5)
        
        self.logger.info(f"Login from login page completed for email: {email}")

    # ===== Observable Outcome Inspection Methods =====
    # Flows return page state; test layer performs assertions

    def get_login_error_message(self):
        """
        Retrieve general login error message (e.g., invalid credentials).
        
        Returns:
            str: Error message text, or None if not displayed
        """
        self.logger.info("Retrieving login error message")
        error_message = self.login_page.get_error_message()
        if error_message:
            self.logger.warning(f"Login error: {error_message}")
            return error_message
        return None

    def get_validation_errors(self):
        """
        Collect all field-level validation errors currently displayed.
        
        Returns:
            dict: Dictionary mapping field names to error messages
        """
        self.logger.info("Collecting all validation errors")
        errors = self.login_page.get_all_validation_errors()
        if errors:
            self.logger.warning(f"Validation errors: {errors}")
        return errors

    def is_any_error_displayed(self):
        """
        Check if any error or validation message is currently visible.
        
        Returns:
            bool: True if error state detected, False otherwise
        """
        return (
            self.login_page.is_any_error_displayed() or
            self.login_page.is_any_validation_error_displayed()
        )

    def initiate_password_reset(self):
        """
        Navigate to password reset flow by clicking "Forgot password?" link.
        Does not verify page transition; caller handles post-navigation logic.
        """
        self.logger.info("Initiating password reset flow")
        self.wait_for_login_page_to_load()
        self.login_page.click_forgot_password()
        self.logger.info("Forgot password page navigation initiated")

    def validate_login_with_valid_credentials(self, email, password):
        """
        Validate logging into the Application using valid credentials.
        
        This method executes the complete login workflow and returns a comprehensive
        result dictionary containing:
        - success: Boolean indicating if login succeeded (observable: logout link visible)
        - error_message: General login error (if any)
        - validation_errors: Field-level validation errors (if any)
        - has_any_error: Boolean indicating presence of any error state
        
        The method does NOT perform assertions. Test layer inspects the returned state
        to determine pass/fail.
        
        Args:
            email (str): Valid user email address
            password (str): Valid user password
        
        Returns:
            dict: Login validation result with keys:
                {
                    'success': bool,           # True if logout link visible
                    'error_message': str|None, # General error text or None
                    'validation_errors': dict, # Field errors: {field: error_text}
                    'has_any_error': bool,     # True if any error state present
                }
        """
        self.logger.info(f"Validating login with valid credentials - email: {email}")
        
        try:
            # Execute login workflow
            self.login_user(email, password)
            self.logger.info("Login workflow completed")
        except Exception as e:
            self.logger.error(f"Login workflow failed: {str(e)}")
            return {
                'success': False,
                'error_message': f"Login workflow error: {str(e)}",
                'validation_errors': {},
                'has_any_error': True,
            }
        
        # Collect observable outcomes
        current_url = self.driver.current_url
        page_title = self.driver.title
        print(f"\n✓ AFTER LOGIN - Current URL: {current_url}")
        print(f"✓ AFTER LOGIN - Page Title: {page_title}")
        
        login_success = self.login_page.is_logout_link_visible()
        print(f"✓ LOGOUT LINK VISIBLE: {login_success}")
        
        error_message = self.get_login_error_message()
        validation_errors = self.get_validation_errors()
        has_any_error = self.is_any_error_displayed()
        
        print(f"✓ ERROR MESSAGE: {error_message}")
        print(f"✓ VALIDATION ERRORS: {validation_errors}")
        print(f"✓ HAS ANY ERROR: {has_any_error}\n")
        
        result = {
            'success': login_success,
            'error_message': error_message,
            'validation_errors': validation_errors,
            'has_any_error': has_any_error,
        }
        
        self.logger.info(f"Login validation result: success={login_success}, has_errors={has_any_error}")
        return result
    def validate_login_with_invalid_email(self, email, password):
        """
        Validate logging into the Application using invalid email.
        
        This method executes the complete login workflow with an invalid/malformed
        email address and returns a comprehensive result dictionary containing:
        - success: Boolean indicating if login succeeded (should be False for invalid email)
        - error_message: General login error or validation error (if any)
        - validation_errors: Field-level validation errors (expected: email error)
        - has_any_error: Boolean indicating presence of error state (should be True)
        - email_error_present: Boolean specifically checking for email field error
        
        The method does NOT perform assertions. Test layer inspects the returned state
        to determine pass/fail.
        
        Args:
            email (str): Invalid or malformed email address (e.g., 'notanemail', 'user@', 'user @example.com')
            password (str): Password (can be valid or invalid)
        
        Returns:
            dict: Login validation result with keys:
                {
                    'success': bool,              # False if login failed (expected: False)
                    'error_message': str|None,    # General error or validation message
                    'validation_errors': dict,    # Field errors: {field: error_text}
                    'has_any_error': bool,        # True if any error state present (expected: True)
                    'email_error_present': bool,  # True if email-specific error detected
                }
        """
        self.logger.info(f"Validating login with invalid email - email: {email}")
        
        try:
            # Execute login workflow with invalid email
            self.login_user(email, password)
            self.logger.info("Login workflow completed (with invalid email)")
        except Exception as e:
            self.logger.error(f"Login workflow failed: {str(e)}")
            return {
                'success': False,
                'error_message': f"Login workflow error: {str(e)}",
                'validation_errors': {},
                'has_any_error': True,
                'email_error_present': False,
            }
        
        # Collect observable outcomes
        login_success = self.login_page.is_logout_link_visible()
        error_message = self.get_login_error_message()
        validation_errors = self.get_validation_errors()
        has_any_error = self.is_any_error_displayed()
        
        # Check specifically for email field error
        email_error_present = 'email' in validation_errors or error_message is not None
        
        result = {
            'success': login_success,
            'error_message': error_message,
            'validation_errors': validation_errors,
            'has_any_error': has_any_error,
            'email_error_present': email_error_present,
        }
        
        self.logger.info(
            f"Login validation result: success={login_success}, has_errors={has_any_error}, "
            f"email_error={email_error_present}"
        )
        return result

    def validate_login_with_invalid_password(self, email, password):
        """
        Validate logging into the Application using invalid password.
        
        This method executes the complete login workflow with a valid email but
        an invalid password and returns a comprehensive result dictionary containing:
        - success: Boolean indicating if login succeeded (should be False for invalid password)
        - error_message: General login error message (expected: invalid credentials error)
        - validation_errors: Field-level validation errors (if any)
        - has_any_error: Boolean indicating presence of error state (should be True)
        - password_error_present: Boolean specifically checking for password field error or general login error
        
        The method does NOT perform assertions. Test layer inspects the returned state
        to determine pass/fail.
        
        Args:
            email (str): Valid user email address
            password (str): Invalid or incorrect password
        
        Returns:
            dict: Login validation result with keys:
                {
                    'success': bool,                 # False if login failed (expected: False)
                    'error_message': str|None,       # General login error message
                    'validation_errors': dict,       # Field errors: {field: error_text}
                    'has_any_error': bool,           # True if any error state present (expected: True)
                    'password_error_present': bool,  # True if password error or login error detected
                }
        """
        self.logger.info(f"Validating login with invalid password - email: {email}")
        
        try:
            # Execute login workflow with invalid password
            self.login_user(email, password)
            self.logger.info("Login workflow completed (with invalid password)")
        except Exception as e:
            self.logger.error(f"Login workflow failed: {str(e)}")
            return {
                'success': False,
                'error_message': f"Login workflow error: {str(e)}",
                'validation_errors': {},
                'has_any_error': True,
                'password_error_present': False,
            }
        
        # Collect observable outcomes
        login_success = self.login_page.is_logout_link_visible()
        error_message = self.get_login_error_message()
        validation_errors = self.get_validation_errors()
        has_any_error = self.is_any_error_displayed()
        
        # Check specifically for password field error or general login error
        password_error_present = 'password' in validation_errors or error_message is not None
        
        result = {
            'success': login_success,
            'error_message': error_message,
            'validation_errors': validation_errors,
            'has_any_error': has_any_error,
            'password_error_present': password_error_present,
        }
        
        self.logger.info(
            f"Login validation result: success={login_success}, has_errors={has_any_error}, "
            f"password_error={password_error_present}"
        )
        return result

    def validate_login_using_keyboard_keys(self, email, password):
        """
        Validate logging into the Application using Keyboard keys (Tab and Enter).
        
        This method executes the login workflow using keyboard navigation only:
        - Tab key to move between form fields
        - Enter key to submit the form
        
        This validates that the application supports keyboard accessibility and form
        submission without mouse interaction. Returns a comprehensive result dictionary:
        - success: Boolean indicating if login succeeded via keyboard navigation
        - error_message: General login error (if any)
        - validation_errors: Field-level validation errors (if any)
        - has_any_error: Boolean indicating presence of error state
        - keyboard_navigation_success: Boolean confirming keyboard-based submission completed
        
        The method does NOT perform assertions. Test layer inspects the returned state
        to determine pass/fail.
        
        Args:
            email (str): User email address
            password (str): User password
        
        Returns:
            dict: Login validation result with keys:
                {
                    'success': bool,                        # True if login succeeded
                    'error_message': str|None,              # General error message if present
                    'validation_errors': dict,              # Field errors: {field: error_text}
                    'has_any_error': bool,                  # True if any error state present
                    'keyboard_navigation_success': bool,    # True if keyboard submission completed
                }
        """
        self.logger.info(f"Validating login using keyboard keys (Tab/Enter) - email: {email}")
        
        try:
            # Step 1: Click login link from home page
            self.home_page.click_login_link()
            self.logger.info("Clicked login link from home page")
            
            # Step 2: Wait for login page to load
            self.wait_for_login_page_to_load()
            
            # Step 3: Enter email and use Tab to move to password field
            self.login_page.enter_email(email)
            self.logger.info("Email entered")
            self.driver.find_element(*self.login_page._email_input).send_keys("\t")
            self.logger.info("Tab key pressed to move to password field")
            
            # Step 4: Enter password and use Tab to move to login button
            self.login_page.enter_password(password)
            self.logger.info("Password entered")
            self.driver.find_element(*self.login_page._password_input).send_keys("\t")
            self.logger.info("Tab key pressed to move to login button")
            
            # Step 5: Press Enter to submit the form
            self.driver.find_element(*self.login_page._login_button).send_keys("\n")
            self.logger.info("Enter key pressed to submit login form via keyboard")
            
            keyboard_navigation_success = True
            
        except Exception as e:
            self.logger.error(f"Keyboard navigation login workflow failed: {str(e)}")
            return {
                'success': False,
                'error_message': f"Keyboard navigation error: {str(e)}",
                'validation_errors': {},
                'has_any_error': True,
                'keyboard_navigation_success': False,
            }
        
        # Collect observable outcomes
        login_success = self.login_page.is_logout_link_visible()
        error_message = self.get_login_error_message()
        validation_errors = self.get_validation_errors()
        has_any_error = self.is_any_error_displayed()
        
        result = {
            'success': login_success,
            'error_message': error_message,
            'validation_errors': validation_errors,
            'has_any_error': has_any_error,
            'keyboard_navigation_success': keyboard_navigation_success,
        }
        
        self.logger.info(
            f"Keyboard navigation login result: success={login_success}, has_errors={has_any_error}, "
            f"keyboard_navigation={keyboard_navigation_success}"
        )
        return result

    def validate_unsuccessful_login_attempts(self, email, password, num_attempts=3):
        """
        Validate the number of unsuccessful login attempts.
        
        This method executes multiple login attempts with invalid credentials and tracks
        the outcomes to validate application behavior under repeated failed login scenarios.
        Useful for testing:
        - Error message consistency across attempts
        - Account lockout mechanisms
        - Rate limiting or retry restrictions
        - Error state accumulation
        
        Returns a comprehensive result dictionary containing:
        - total_attempts: Number of login attempts executed
        - failed_attempts: Count of unsuccessful login attempts
        - success: Boolean indicating if any attempt succeeded (expected: False)
        - error_messages: List of unique error messages encountered
        - first_error_message: Error message from first attempt
        - last_error_message: Error message from final attempt
        - all_attempts_failed: Boolean confirming all attempts failed
        - has_account_lockout_message: Boolean checking for lockout/suspension messages
        
        The method does NOT perform assertions. Test layer inspects the returned state
        to determine pass/fail and validate security policies.
        
        Args:
            email (str): User email address (with invalid password)
            password (str): Invalid password
            num_attempts (int): Number of login attempts to execute (default: 3)
        
        Returns:
            dict: Login attempt validation result with keys:
                {
                    'total_attempts': int,              # Total attempts executed
                    'failed_attempts': int,             # Count of failed attempts
                    'success': bool,                    # True if any attempt succeeded (expected: False)
                    'error_messages': list,             # Unique error messages encountered
                    'first_error_message': str|None,    # Error from first attempt
                    'last_error_message': str|None,     # Error from final attempt
                    'all_attempts_failed': bool,        # True if all attempts failed
                    'has_account_lockout_message': bool, # True if lockout/suspension detected
                }
        """
        self.logger.info(
            f"Validating unsuccessful login attempts - email: {email}, attempts: {num_attempts}"
        )
        
        failed_attempts = 0
        error_messages = []
        first_error_message = None
        last_error_message = None
        
        try:
            for attempt in range(1, num_attempts + 1):
                self.logger.info(f"Login attempt {attempt}/{num_attempts}")
                
                try:
                    # Click login link (first attempt) or proceed with form (subsequent attempts)
                    if attempt == 1:
                        self.home_page.click_login_link()
                        self.wait_for_login_page_to_load()
                    
                    # Clear previous entries on subsequent attempts
                    if attempt > 1:
                        self.login_page.clear_email()
                        self.login_page.clear_password()
                    
                    # Perform login attempt
                    self.login_page.enter_email(email)
                    self.login_page.enter_password(password)
                    self.login_page.submit_login_form()
                    
                    self.logger.info(f"Attempt {attempt} form submitted")
                    
                    # Check if attempt was successful
                    if not self.login_page.is_logout_link_visible():
                        failed_attempts += 1
                        error_msg = self.get_login_error_message()
                        
                        if error_msg:
                            error_messages.append(error_msg)
                            if attempt == 1:
                                first_error_message = error_msg
                            if attempt == num_attempts:
                                last_error_message = error_msg
                        
                        self.logger.warning(
                            f"Attempt {attempt} failed. Error: {error_msg}"
                        )
                    else:
                        self.logger.info(f"Attempt {attempt} succeeded (unexpected)")
                        
                except Exception as attempt_error:
                    failed_attempts += 1
                    self.logger.error(f"Attempt {attempt} execution error: {str(attempt_error)}")
            
        except Exception as e:
            self.logger.error(f"Unsuccessful login attempts validation failed: {str(e)}")
            return {
                'total_attempts': num_attempts,
                'failed_attempts': failed_attempts,
                'success': False,
                'error_messages': error_messages,
                'first_error_message': first_error_message,
                'last_error_message': last_error_message,
                'all_attempts_failed': failed_attempts == num_attempts,
                'has_account_lockout_message': False,
            }
        
        # Check for account lockout or rate limiting messages
        has_lockout = any(
            keyword in str(error_messages).lower() 
            for keyword in ['locked', 'suspended', 'disabled', 'temporarily', 'too many']
        )
        
        # Collect observable outcomes from final state
        final_success = self.login_page.is_logout_link_visible()
        
        result = {
            'total_attempts': num_attempts,
            'failed_attempts': failed_attempts,
            'success': final_success,
            'error_messages': list(set(error_messages)),  # Unique errors only
            'first_error_message': first_error_message,
            'last_error_message': last_error_message,
            'all_attempts_failed': failed_attempts == num_attempts,
            'has_account_lockout_message': has_lockout,
        }
        
        self.logger.info(
            f"Unsuccessful login attempts result: total={num_attempts}, failed={failed_attempts}, "
            f"lockout_detected={has_lockout}, unique_errors={len(result['error_messages'])}"
        )
        return result