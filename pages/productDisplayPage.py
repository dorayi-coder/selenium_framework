from selenium.webdriver.common.by import By
from utilities.basePage import BasePage
from utilities.customLogger import LoggerFactory


class ProductDisplayPage(BasePage):
    logger = LoggerFactory.get_logger(__name__)

    _product_name = (By.XPATH, "//h1[@class='product-name']")
    _product_price = (By.CLASS_NAME, "product-price")
    _product_description = (By.CLASS_NAME, "product-description")
    _product_rating = (By.CLASS_NAME, "product-rating")
    _product_review_count = (By.XPATH, "//span[contains(@class, 'review-count')]")
    _product_image = (By.CLASS_NAME, "product-image")
    _product_gallery = (By.CLASS_NAME, "product-gallery")
    _product_sku = (By.XPATH, "//span[contains(@class, 'sku')]")
    _product_availability = (By.CLASS_NAME, "availability")
    _stock_status = (By.CLASS_NAME, "stock-status")
    _quantity_input = (By.ID, "product-quantity")
    _add_to_cart_button = (By.ID, "add-to-cart")
    _add_to_wishlist_button = (By.XPATH, "//button[contains(@class, 'add-to-wishlist')]")
    _add_to_compare_button = (By.XPATH, "//button[contains(@class, 'add-to-compare')]")
    _reviews_tab = (By.XPATH, "//a[contains(text(), 'Reviews')]")
    _reviews_section = (By.CLASS_NAME, "product-reviews")
    _write_review_button = (By.XPATH, "//button[contains(text(), 'Write a review')]")
    _success_message = (By.CLASS_NAME, "success")
    _error_message = (By.CLASS_NAME, "error")
    _related_products = (By.CLASS_NAME, "related-products")
    _product_attributes = (By.CLASS_NAME, "product-attribute")
    _size_selector = (By.ID, "product-size")
    _color_selector = (By.ID, "product-color")
    _back_button = (By.XPATH, "//a[contains(text(), 'Back')]")

    def is_page_loaded(self):
        self.logger.info("Checking if Product Display page is loaded")
        return self.is_element_visible(self._product_name)

    def get_product_name(self):
        self.logger.info("Getting product name")
        return self.get_text(self._product_name)

    def get_product_price(self):
        self.logger.info("Getting product price")
        return self.get_text(self._product_price)

    def get_product_description(self):
        self.logger.info("Getting product description")
        if self.is_element_present(self._product_description):
            return self.get_text(self._product_description)
        return None

    def get_product_rating(self):
        self.logger.info("Getting product rating")
        if self.is_element_present(self._product_rating):
            return self.get_text(self._product_rating)
        return None

    def get_review_count(self):
        self.logger.info("Getting product review count")
        if self.is_element_present(self._product_review_count):
            return self.get_text(self._product_review_count)
        return None

    def get_product_sku(self):
        self.logger.info("Getting product SKU")
        if self.is_element_present(self._product_sku):
            return self.get_text(self._product_sku)
        return None

    def get_availability_status(self):
        self.logger.info("Getting product availability status")
        if self.is_element_present(self._product_availability):
            return self.get_text(self._product_availability)
        return None

    def get_stock_status(self):
        self.logger.info("Getting product stock status")
        if self.is_element_present(self._stock_status):
            return self.get_text(self._stock_status)
        return None

    def is_product_in_stock(self):
        self.logger.info("Checking if product is in stock")
        stock_status = self.get_stock_status()
        return "in stock" in stock_status.lower() if stock_status else False

    def enter_quantity(self, quantity):
        self.logger.info(f"Entering quantity: {quantity}")
        self.type(self._quantity_input, str(quantity))

    def add_product_to_cart(self):
        self.logger.info("Adding product to cart")
        self.click(self._add_to_cart_button)

    def add_product_to_wishlist(self):
        self.logger.info("Adding product to wishlist")
        self.click(self._add_to_wishlist_button)

    def add_product_to_compare(self):
        self.logger.info("Adding product to compare")
        self.click(self._add_to_compare_button)

    def select_size(self, size):
        self.logger.info(f"Selecting size: {size}")
        if self.is_element_present(self._size_selector):
            self.select_dropdown(self._size_selector, size)

    def select_color(self, color):
        self.logger.info(f"Selecting color: {color}")
        if self.is_element_present(self._color_selector):
            self.select_dropdown(self._color_selector, color)

    def click_reviews_tab(self):
        self.logger.info("Clicking reviews tab")
        self.click(self._reviews_tab)

    def are_reviews_visible(self):
        self.logger.info("Checking if reviews are visible")
        return self.is_element_visible(self._reviews_section)

    def click_write_review_button(self):
        self.logger.info("Clicking write review button")
        self.click(self._write_review_button)

    def are_related_products_displayed(self):
        self.logger.info("Checking if related products are displayed")
        return self.is_element_visible(self._related_products)

    def is_success_message_displayed(self):
        self.logger.info("Checking if success message is displayed")
        return self.is_element_visible(self._success_message)

    def get_success_message(self):
        self.logger.info("Retrieving success message")
        if self.is_element_present(self._success_message):
            return self.get_text(self._success_message)
        return None

    def is_error_message_displayed(self):
        self.logger.info("Checking if error message is displayed")
        return self.is_element_visible(self._error_message)

    def get_error_message(self):
        self.logger.info("Retrieving error message")
        if self.is_element_present(self._error_message):
            return self.get_text(self._error_message)
        return None

    def click_back(self):
        self.logger.info("Clicking back button")
        self.click(self._back_button)

    def is_add_to_cart_button_enabled(self):
        self.logger.info("Checking if add to cart button is enabled")
        try:
            button = self.driver.find_element(*self._add_to_cart_button)
            return button.is_enabled()
        except Exception as e:
            self.logger.error(f"Error checking add to cart button: {e}")
            return False

    def is_product_visible(self):
        self.logger.info("Checking if product is visible")
        return self.is_element_visible(self._product_name)

    def is_product_image_visible(self):
        self.logger.info("Checking if product image is visible")
        return self.is_element_visible(self._product_image)



    def is_product_name_visible(self):
        self.logger.info("Checking if product name is visible")
        return self.is_element_visible(self._product_name)

    def is_product_sku_visible(self):
        self.logger.info("Checking if product SKU is visible")
        return self.is_element_visible(self._product_sku)

    def get_product_category(self):
        self.logger.info("Getting product category")
        try:
            category_elem = self.driver.find_element(By.XPATH, "//a[@class='breadcrumb-item'][2]")
            return category_elem.text
        except:
            self.logger.warning("Product category not found")
            return None

    def is_breadcrumb_visible(self):
        self.logger.info("Checking if breadcrumb is visible")
        try:
            breadcrumb = self.driver.find_element(By.CLASS_NAME, "breadcrumb")
            return breadcrumb.is_displayed()
        except:
            return False

    def get_breadcrumb_path(self):
        self.logger.info("Getting breadcrumb path")
        try:
            breadcrumb_items = self.driver.find_elements(By.XPATH, "//a[@class='breadcrumb-item']")
            path = " > ".join([item.text for item in breadcrumb_items])
            return path
        except:
            self.logger.warning("Breadcrumb path not found")
            return None

    def get_last_modified_timestamp(self):
        self.logger.info("Getting last modified timestamp")
        try:
            timestamp = self.driver.find_element(By.XPATH, "//meta[@http-equiv='last-modified']").get_attribute("content")
            return timestamp
        except:
            self.logger.warning("Last modified timestamp not found")
            return None

    def is_page_fresh(self):
        self.logger.info("Checking if page is fresh (not cached)")
        try:
            cache_control = self.driver.find_element(By.XPATH, "//meta[@http-equiv='cache-control']")
            return cache_control is not None
        except:
            self.logger.warning("Cache control meta tag not found")
            return True
