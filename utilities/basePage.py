from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from utilities.customLogger import LoggerFactory
from utilities.readProperties import ReadConfig
import time
import random


class BasePage:
    logger = LoggerFactory.get_logger(__name__)

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver, int(ReadConfig.get("TIMEOUTS", "explicit_wait"))
        )
        # Ensure Cloudflare Turnstile is handled on page load
        self._handle_cloudflare_on_init()

    def click(self, locator):
        try:
            # CRITICAL: Handle Cloudflare Turnstile before interacting with page
            self._ensure_cloudflare_resolved(locator)
            
            self.logger.debug(f"Clicking on element: {locator}")
            element = self.wait.until(EC.element_to_be_clickable(locator))
            
            # Scroll to element to ensure it's visible
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(0.5)  # Brief wait after scrolling
            
            element.click()
        except TimeoutException:
            self.logger.error(f"Timeout: Element not clickable: {locator}")
            raise

    def type(self, locator, text):
        try:
            # CRITICAL: Handle Cloudflare Turnstile before interacting with page
            self._ensure_cloudflare_resolved(locator)
            
            self.logger.debug(f"Typing '{text}' into element: {locator}")
            self.logger.info(f"Waiting for presence of element with 10s timeout: {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.logger.info(f"Element found, clearing and typing...")
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Successfully typed into element")
        except TimeoutException as te:
            self.logger.error(f"Timeout: Element not found: {locator}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error while typing: {str(e)}")
            raise

    def type_slow(self, locator, text, delay=0.1):
        try:
            # CRITICAL: Handle Cloudflare Turnstile before interacting with page
            self._ensure_cloudflare_resolved(locator)
            
            self.logger.debug(f"Typing '{text}' into element with delay {delay}s: {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
            for character in text:
                element.send_keys(character)
                time.sleep(delay)
        except TimeoutException:
            self.logger.error(f"Timeout: Element not found: {locator}")
            raise

    def get_text(self, locator):
        try:
            # CRITICAL: Handle Cloudflare Turnstile before interacting with page
            self._ensure_cloudflare_resolved(locator)
            
            self.logger.debug(f"Getting text from element: {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element.text
        except TimeoutException:
            self.logger.error(f"Timeout: Element not found: {locator}")
            raise

    def is_element_visible(self, locator):
        try:
            # CRITICAL: Handle Cloudflare Turnstile before checking visibility
            self._ensure_cloudflare_resolved(locator)
            
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False



    def select_dropdown(self, locator, value):
        try:
            from selenium.webdriver.support.select import Select

            self.logger.debug(f"Selecting value '{value}' from dropdown: {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            dropdown = Select(element)
            dropdown.select_by_value(value)
        except TimeoutException:
            self.logger.error(f"Timeout: Dropdown not found: {locator}")
            raise

    def is_checkbox_selected(self, locator):
        try:
            # CRITICAL: Handle Cloudflare Turnstile before interacting with page
            self._ensure_cloudflare_resolved(locator)
            
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element.is_selected()
        except TimeoutException:
            self.logger.error(f"Timeout: Checkbox not found: {locator}")
            raise

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def find_elements(self, locator):
        try:
            self.logger.debug(f"Finding elements: {locator}")
            return self.driver.find_elements(*locator)
        except NoSuchElementException:
            self.logger.warning(f"No elements found: {locator}")
            return []

    def select_dropdown_by_text(self, locator, text):
        try:
            # CRITICAL: Handle Cloudflare Turnstile before interacting with page
            self._ensure_cloudflare_resolved(locator)
            
            from selenium.webdriver.support.select import Select

            self.logger.debug(f"Selecting text '{text}' from dropdown: {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            dropdown = Select(element)
            dropdown.select_by_visible_text(text)
        except TimeoutException:
            self.logger.error(f"Timeout: Dropdown not found: {locator}")
            raise

    def double_click(self, locator):
        try:
            # CRITICAL: Handle Cloudflare Turnstile before interacting with page
            self._ensure_cloudflare_resolved(locator)
            
            from selenium.webdriver.common.action_chains import ActionChains

            self.logger.debug(f"Double clicking on element: {locator}")
            element = self.wait.until(EC.element_to_be_clickable(locator))
            ActionChains(self.driver).double_click(element).perform()
        except TimeoutException:
            self.logger.error(f"Timeout: Element not clickable: {locator}")
            raise

    def right_click(self, locator):
        try:
            # CRITICAL: Handle Cloudflare Turnstile before interacting with page
            self._ensure_cloudflare_resolved(locator)
            
            from selenium.webdriver.common.action_chains import ActionChains

            self.logger.debug(f"Right clicking on element: {locator}")
            element = self.wait.until(EC.element_to_be_clickable(locator))
            ActionChains(self.driver).context_click(element).perform()
        except TimeoutException:
            self.logger.error(f"Timeout: Element not clickable: {locator}")
            raise

    def hover_over(self, locator):
        try:
            # CRITICAL: Handle Cloudflare Turnstile before interacting with page
            self._ensure_cloudflare_resolved(locator)
            
            from selenium.webdriver.common.action_chains import ActionChains

            self.logger.debug(f"Hovering over element: {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            ActionChains(self.driver).move_to_element(element).perform()
        except TimeoutException:
            self.logger.error(f"Timeout: Element not found: {locator}")
            raise

    def get_attribute(self, locator, attribute_name):
        try:
            # CRITICAL: Handle Cloudflare Turnstile before interacting with page
            self._ensure_cloudflare_resolved(locator)
            
            self.logger.debug(f"Getting attribute '{attribute_name}' from element: {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element.get_attribute(attribute_name)
        except TimeoutException:
            self.logger.error(f"Timeout: Element not found: {locator}")
            raise

    def clear_field(self, locator):
        try:
            # CRITICAL: Handle Cloudflare Turnstile before interacting with page
            self._ensure_cloudflare_resolved(locator)
            
            self.logger.debug(f"Clearing field: {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
        except TimeoutException:
            self.logger.error(f"Timeout: Element not found: {locator}")
            raise

    def submit_form(self, locator):
        try:
            # CRITICAL: Handle Cloudflare Turnstile before interacting with page
            self._ensure_cloudflare_resolved(locator)
            
            self.logger.debug(f"Submitting form: {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.submit()
        except TimeoutException:
            self.logger.error(f"Timeout: Form element not found: {locator}")
            raise

    def wait_for_element_to_disappear(self, locator):
        try:
            # CRITICAL: Handle Cloudflare Turnstile before checking disappearance
            self._ensure_cloudflare_resolved(locator)
            
            self.logger.debug(f"Waiting for element to disappear: {locator}")
            self.wait.until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            self.logger.error(f"Timeout: Element did not disappear: {locator}")
            return False

    def scroll_to_element(self, locator):
        try:
            # CRITICAL: Handle Cloudflare Turnstile before interacting with page
            self._ensure_cloudflare_resolved(locator)
            
            self.logger.debug(f"Scrolling to element: {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except TimeoutException:
            self.logger.error(f"Timeout: Element not found: {locator}")
            raise

    # ==================== HUMAN-LIKE BEHAVIOR METHODS ====================
    
    def type_with_random_delay(self, locator, text, min_delay=0.05, max_delay=0.15):
        """Type text with random delays between characters for human-like behavior.
        
        Args:
            locator: Element locator tuple
            text (str): Text to type
            min_delay (float): Minimum delay in seconds between characters (default: 0.05)
            max_delay (float): Maximum delay in seconds between characters (default: 0.15)
        """
        try:
            self._ensure_cloudflare_resolved(locator)
            
            self.logger.info(f"Typing with random delay (human-like): '{text}' into {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
            
            for character in text:
                element.send_keys(character)
                # Random delay between each character
                random_delay = random.uniform(min_delay, max_delay)
                time.sleep(random_delay)
                
            self.logger.info(f"Typing completed with human-like behavior")
        except TimeoutException:
            self.logger.error(f"Timeout: Element not found: {locator}")
            raise
    
    def click_with_pause(self, locator, pause_after=0.3):
        """Click element and pause briefly after for human-like behavior.
        
        Args:
            locator: Element locator tuple
            pause_after (float): Pause duration after click in seconds (default: 0.3)
        """
        try:
            self._ensure_cloudflare_resolved(locator)
            
            self.logger.debug(f"Clicking with pause: {locator}")
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(0.5)
            element.click()
            time.sleep(pause_after)
            self.logger.info(f"Clicked with {pause_after}s pause for human-like behavior")
        except TimeoutException:
            self.logger.error(f"Timeout: Element not clickable: {locator}")
            raise
    
    def type_with_tab_navigation(self, locator, text, use_tab=False):
        """Type text and optionally use TAB to move to next field.
        
        Args:
            locator: Element locator tuple
            text (str): Text to type
            use_tab (bool): If True, press TAB after typing to move to next field
        """
        try:
            self._ensure_cloudflare_resolved(locator)
            
            self.logger.info(f"Typing with TAB navigation: '{text}' into {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            
            if use_tab:
                time.sleep(0.2)
                element.send_keys(Keys.TAB)
                self.logger.info("TAB key pressed to move to next field")
        except TimeoutException:
            self.logger.error(f"Timeout: Element not found: {locator}")
            raise
    
    def move_to_element_slowly(self, locator, duration=1.0):
        """Move mouse to element slowly for human-like behavior.
        
        Args:
            locator: Element locator tuple
            duration (float): Duration of mouse movement in seconds (default: 1.0)
        """
        try:
            self._ensure_cloudflare_resolved(locator)
            
            self.logger.debug(f"Moving to element slowly: {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            
            # Scroll element into view first
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(0.3)
            
            # Move cursor slowly to element
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            time.sleep(duration)
            
            self.logger.info(f"Mouse moved to element over {duration}s")
        except TimeoutException:
            self.logger.error(f"Timeout: Element not found: {locator}")
            raise
    
    def focus_element_with_delay(self, locator, delay=0.3):
        """Focus element with delay before interaction.
        
        Args:
            locator: Element locator tuple
            delay (float): Delay before focusing in seconds (default: 0.3)
        """
        try:
            self._ensure_cloudflare_resolved(locator)
            
            self.logger.debug(f"Focusing element with delay: {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            
            # Scroll into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(delay)
            
            # Click to focus
            element.click()
            time.sleep(0.2)
            
            self.logger.info(f"Element focused with {delay}s delay")
        except TimeoutException:
            self.logger.error(f"Timeout: Element not found: {locator}")
            raise
    
    def wait_for_element_with_visual_stability(self, locator, wait_time=0.5):
        """Wait for element to be stable and not moving before interaction.
        
        Args:
            locator: Element locator tuple
            wait_time (float): Time to wait for element stability (default: 0.5)
            
        Returns:
            bool: True if element is stable
        """
        try:
            self.logger.debug(f"Waiting for element stability: {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            
            # Get initial position
            initial_rect = element.rect
            time.sleep(wait_time)
            
            # Get final position
            final_rect = element.rect
            
            # Check if position changed
            is_stable = (initial_rect['x'] == final_rect['x'] and 
                        initial_rect['y'] == final_rect['y'])
            
            if is_stable:
                self.logger.info("Element is stable - safe to interact")
                return True
            else:
                self.logger.warning("Element moved during stability check")
                return False
        except TimeoutException:
            self.logger.error(f"Timeout: Element not found: {locator}")
            return False
    
    def scroll_slowly_to_element(self, locator, scroll_pause=0.2):
        """Scroll slowly to element in smooth motion.
        
        Args:
            locator: Element locator tuple
            scroll_pause (float): Pause between scroll steps (default: 0.2)
        """
        try:
            self._ensure_cloudflare_resolved(locator)
            
            self.logger.debug(f"Scrolling slowly to element: {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            
            # Smooth scroll with multiple steps
            location = element.location
            self.driver.execute_script(
                "window.scrollBy(0, " + str(location['y']) + ");",
                element
            )
            time.sleep(scroll_pause)
            
            self.logger.info(f"Smoothly scrolled to element")
        except TimeoutException:
            self.logger.error(f"Timeout: Element not found: {locator}")
            raise
    
    def wait_and_click_with_retry(self, locator, retry_count=3, wait_between_retries=0.5):
        """Click element with retry logic for stability.
        
        Args:
            locator: Element locator tuple
            retry_count (int): Number of retry attempts (default: 3)
            wait_between_retries (float): Wait time between retries (default: 0.5)
            
        Returns:
            bool: True if click was successful
        """
        for attempt in range(retry_count):
            try:
                self._ensure_cloudflare_resolved(locator)
                
                self.logger.info(f"Click attempt {attempt + 1}/{retry_count}")
                element = self.wait.until(EC.element_to_be_clickable(locator))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(0.3)
                element.click()
                
                self.logger.info(f"Successfully clicked after {attempt + 1} attempt(s)")
                return True
            except (TimeoutException, Exception) as e:
                if attempt < retry_count - 1:
                    self.logger.warning(f"Click failed, retrying in {wait_between_retries}s...")
                    time.sleep(wait_between_retries)
                else:
                    self.logger.error(f"Click failed after {retry_count} attempts: {str(e)}")
                    raise
        
        return False
