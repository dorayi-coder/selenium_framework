from pages.homePage import HomePage
from utilities.customLogger import LoggerFactory


class HomePageFlow:
    logger = LoggerFactory.get_logger(__name__)

    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)

    def wait_for_home_page_to_load(self):
        self.logger.info("Waiting for Home page to load")
        self.home_page.handle_cloudflare_if_present()
        if not self.home_page.is_page_loaded():
            self.logger.error("Home page failed to load")
            raise Exception("Home page failed to load")
        self.logger.info("Home page loaded successfully")

    def navigate_to_home_page(self):
        self.logger.info("Navigating to home page")
        self.home_page.navigate_to_home_page()
        self.wait_for_home_page_to_load()

    def search_product(self, product_name):
        self.logger.info(f"Searching for product: {product_name}")
        self.wait_for_home_page_to_load()
        self.home_page.search_for_product(product_name)
        self.logger.info(f"Search submitted for product: {product_name}")

    def browse_category(self, category_name):
        self.logger.info(f"Browsing category: {category_name}")
        self.wait_for_home_page_to_load()
        success = self.home_page.click_category_menu_item(category_name)
        if success:
            self.logger.info(f"Successfully navigated to category: {category_name}")
        else:
            self.logger.warning(f"Failed to navigate to category: {category_name}")
        return success

    def browse_popular_category(self, category_name):
        self.logger.info(f"Browsing popular category: {category_name}")
        self.wait_for_home_page_to_load()
        success = self.home_page.click_popular_category(category_name)
        if success:
            self.logger.info(f"Successfully navigated to popular category: {category_name}")
        else:
            self.logger.warning(f"Failed to navigate to popular category: {category_name}")
        return success

    def get_featured_products_list(self):
        self.logger.info("Retrieving featured products list")
        self.wait_for_home_page_to_load()
        products = self.home_page.get_all_featured_product_names()
        self.logger.info(f"Retrieved {len(products)} featured products")
        return products

    def get_new_products_list(self):
        self.logger.info("Retrieving new products list")
        self.wait_for_home_page_to_load()
        products = self.home_page.get_all_new_product_names()
        self.logger.info(f"Retrieved {len(products)} new products")
        return products

    def get_all_categories(self):
        self.logger.info("Retrieving all categories")
        self.wait_for_home_page_to_load()
        categories = self.home_page.get_all_category_menu_items()
        self.logger.info(f"Retrieved {len(categories)} categories")
        return categories

    def get_all_popular_categories(self):
        self.logger.info("Retrieving all popular categories")
        self.wait_for_home_page_to_load()
        categories = self.home_page.get_all_popular_categories()
        self.logger.info(f"Retrieved {len(categories)} popular categories")
        return categories

    def navigate_to_login(self):
        self.logger.info("Navigating to login page from home")
        self.wait_for_home_page_to_load()
        self.home_page.click_login_link()
        self.logger.info("Login link clicked")

    def navigate_to_register(self):
        self.logger.info("Navigating to registration page from home")
        self.wait_for_home_page_to_load()
        self.home_page.click_register_link()
        self.logger.info("Register link clicked")

    def navigate_to_cart(self):
        self.logger.info("Navigating to cart from home")
        self.wait_for_home_page_to_load()
        self.home_page.click_cart_icon()
        self.logger.info("Cart icon clicked")

    def navigate_to_wishlist(self):
        self.logger.info("Navigating to wishlist from home")
        self.wait_for_home_page_to_load()
        self.home_page.click_wishlist_icon()
        self.logger.info("Wishlist icon clicked")

    def navigate_to_account(self):
        self.logger.info("Navigating to account from home")
        self.wait_for_home_page_to_load()
        self.home_page.click_account_icon()
        self.logger.info("Account icon clicked")

    def verify_user_not_logged_in(self):
        self.logger.info("Verifying user is not logged in")
        self.wait_for_home_page_to_load()
        is_login_visible = self.home_page.is_login_link_visible()
        if is_login_visible:
            self.logger.info("User is not logged in - login link is visible")
        else:
            self.logger.warning("User appears to be logged in - login link not visible")
        return is_login_visible

    def verify_user_logged_in(self):
        self.logger.info("Verifying user is logged in")
        self.wait_for_home_page_to_load()
        is_account_visible = self.home_page.is_account_icon_visible()
        if is_account_visible:
            self.logger.info("User is logged in - account icon is visible")
        else:
            self.logger.warning("User does not appear to be logged in - account icon not visible")
        return is_account_visible

    def subscribe_to_newsletter(self, email):
        self.logger.info(f"Subscribing to newsletter with email: {email}")
        self.wait_for_home_page_to_load()
        self.home_page.subscribe_to_newsletter(email)
        self.logger.info(f"Newsletter subscription submitted for email: {email}")

    def verify_newsletter_available(self):
        self.logger.info("Verifying newsletter subscription is available")
        self.wait_for_home_page_to_load()
        is_available = self.home_page.is_newsletter_subscription_available()
        if is_available:
            self.logger.info("Newsletter subscription is available")
        else:
            self.logger.warning("Newsletter subscription is not available")
        return is_available

    def get_homepage_summary(self):
        self.logger.info("Getting home page summary")
        self.wait_for_home_page_to_load()
        summary = {
            'page_title': self.home_page.get_page_title(),
            'featured_products_count': self.home_page.get_featured_products_count(),
            'new_products_count': self.home_page.get_new_products_count(),
            'carousel_present': self.home_page.is_carousel_present(),
            'carousel_items_count': self.home_page.get_carousel_items_count(),
            'promotion_banner_visible': self.home_page.is_promotion_banner_visible(),
            'categories': self.home_page.get_all_category_menu_items(),
            'newsletter_available': self.home_page.is_newsletter_subscription_available()
        }
        self.logger.info("Home page summary retrieved successfully")
        return summary

    def get_footer_information(self):
        self.logger.info("Getting footer information")
        self.wait_for_home_page_to_load()
        footer_links = self.home_page.get_all_footer_links()
        self.logger.info(f"Retrieved {len(footer_links)} footer links")
        return footer_links

    def verify_homepage_is_loaded(self):
        self.logger.info("Verifying home page is loaded")
        self.wait_for_home_page_to_load()
        is_loaded = self.home_page.is_page_loaded()
        if is_loaded:
            self.logger.info("Home page is loaded successfully")
        else:
            self.logger.error("Home page failed to load")
        return is_loaded

    def change_currency(self, currency_code):
        self.logger.info(f"Changing currency to: {currency_code}")
        self.wait_for_home_page_to_load()
        success = self.home_page.select_currency(currency_code)
        if success:
            self.logger.info(f"Currency changed to: {currency_code}")
        else:
            self.logger.warning(f"Failed to change currency to: {currency_code}")
        return success

    def change_language(self, language_name):
        self.logger.info(f"Changing language to: {language_name}")
        self.wait_for_home_page_to_load()
        success = self.home_page.select_language(language_name)
        if success:
            self.logger.info(f"Language changed to: {language_name}")
        else:
            self.logger.warning(f"Failed to change language to: {language_name}")
        return success

    def verify_featured_products_displayed(self):
        self.logger.info("Verifying featured products are displayed")
        self.wait_for_home_page_to_load()
        count = self.home_page.get_featured_products_count()
        is_displayed = count > 0
        if is_displayed:
            self.logger.info(f"Featured products are displayed - count: {count}")
        else:
            self.logger.warning("No featured products are displayed")
        return is_displayed

    def verify_new_products_displayed(self):
        self.logger.info("Verifying new products are displayed")
        self.wait_for_home_page_to_load()
        count = self.home_page.get_new_products_count()
        is_displayed = count > 0
        if is_displayed:
            self.logger.info(f"New products are displayed - count: {count}")
        else:
            self.logger.warning("No new products are displayed")
        return is_displayed
