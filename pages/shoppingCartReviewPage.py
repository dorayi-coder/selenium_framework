from selenium.webdriver.common.by import By
from utilities.basePage import BasePage
from utilities.customLogger import LoggerFactory


class ShoppingCartReviewPage(BasePage):
    logger = LoggerFactory.get_logger(__name__)

    # AI hints for intelligent locator suggestion
        return self.is_element_visible(self._cart_review_title)

    def is_cart_empty(self):
        self.logger.info("Checking if cart is empty")
        return self.is_element_visible(self._empty_cart_message)

    def get_number_of_items(self):
        self.logger.info("Getting number of items in cart review")
        try:
            items = self.driver.find_elements(*self._product_item)
            count = len(items)
            self.logger.info(f"Number of items: {count}")
            return count
        except Exception as e:
            self.logger.error(f"Error getting item count: {e}")
            return 0

    def get_all_product_details(self):
        self.logger.info("Getting all product details")
        try:
            products = []
            names = self.driver.find_elements(*self._product_name)
            prices = self.driver.find_elements(*self._product_price)
            quantities = self.driver.find_elements(*self._product_quantity)
            subtotals = self.driver.find_elements(*self._product_subtotal)

            for i in range(len(names)):
                product = {
                    "name": names[i].text if i < len(names) else None,
                    "price": prices[i].text if i < len(prices) else None,
                    "quantity": quantities[i].text if i < len(quantities) else None,
                    "subtotal": subtotals[i].text if i < len(subtotals) else None
                }
                products.append(product)
            
            self.logger.info(f"Retrieved {len(products)} product details")
            return products
        except Exception as e:
            self.logger.error(f"Error getting product details: {e}")
            return []

    def get_cart_summary(self):
        self.logger.info("Getting cart summary")
        summary = {
            "subtotal": self.get_subtotal(),
            "shipping": self.get_shipping_cost(),
            "tax": self.get_tax(),
            "discount": self.get_discount(),
            "total": self.get_total()
        }
        self.logger.info(f"Cart summary: {summary}")
        return summary

    def get_subtotal(self):
        self.logger.info("Getting subtotal")
        if self.is_element_present(self._subtotal_amount):
            return self.get_text(self._subtotal_amount)
        return None

    def get_shipping_cost(self):
        self.logger.info("Getting shipping cost")
        if self.is_element_present(self._shipping_amount):
            return self.get_text(self._shipping_amount)
        return None

    def get_tax(self):
        self.logger.info("Getting tax amount")
        if self.is_element_present(self._tax_amount):
            return self.get_text(self._tax_amount)
        return None

    def get_total(self):
        self.logger.info("Getting total amount")
        if self.is_element_present(self._total_amount):
            return self.get_text(self._total_amount)
        return None

    def get_discount(self):
        self.logger.info("Getting discount amount")
        if self.is_element_present(self._discount_amount):
            return self.get_text(self._discount_amount)
        return None

    def apply_voucher_code(self, voucher_code):
        self.logger.info(f"Applying voucher code: {voucher_code}")
        self.type(self._voucher_input, voucher_code)
        self.click(self._apply_voucher_button)
        self.logger.info(f"Voucher code {voucher_code} applied")

    def is_discount_applied(self):
        self.logger.info("Checking if discount is applied")
        return self.is_element_visible(self._discount_section)

    def select_shipping_method(self, method_index):
        self.logger.info(f"Selecting shipping method at index {method_index}")
        try:
            methods = self.driver.find_elements(*self._shipping_method_radio)
            if method_index < len(methods):
                methods[method_index].click()
                self.logger.info(f"Shipping method {method_index} selected")
            else:
                self.logger.error(f"Shipping method index {method_index} out of range")
        except Exception as e:
            self.logger.error(f"Error selecting shipping method: {e}")

    def get_estimated_delivery_date(self):
        self.logger.info("Getting estimated delivery date")
        if self.is_element_present(self._estimated_delivery):
            return self.get_text(self._estimated_delivery)
        return None

    def enter_gift_message(self, message):
        self.logger.info("Entering gift message")
        if self.is_element_present(self._gift_message_input):
            self.type(self._gift_message_input, message)
            self.logger.info("Gift message entered")

    def enable_gift_wrap(self):
        self.logger.info("Enabling gift wrap")
        if self.is_element_present(self._gift_wrap_checkbox):
            if not self.is_checkbox_selected(self._gift_wrap_checkbox):
                self.click(self._gift_wrap_checkbox)
                self.logger.info("Gift wrap enabled")

    def disable_gift_wrap(self):
        self.logger.info("Disabling gift wrap")
        if self.is_element_present(self._gift_wrap_checkbox):
            if self.is_checkbox_selected(self._gift_wrap_checkbox):
                self.click(self._gift_wrap_checkbox)
                self.logger.info("Gift wrap disabled")

    def accept_terms_and_conditions(self):
        self.logger.info("Accepting terms and conditions")
        if not self.is_checkbox_selected(self._terms_checkbox):
            self.click(self._terms_checkbox)
            self.logger.info("Terms and conditions accepted")

    def decline_terms_and_conditions(self):
        self.logger.info("Declining terms and conditions")
        if self.is_checkbox_selected(self._terms_checkbox):
            self.click(self._terms_checkbox)
            self.logger.info("Terms and conditions declined")

    def proceed_to_checkout(self):
        self.logger.info("Proceeding to checkout")
        if self.is_element_visible(self._checkout_button):
            self.click(self._checkout_button)
        elif self.is_element_visible(self._proceed_checkout_button):
            self.click(self._proceed_checkout_button)
        else:
            self.logger.error("Checkout button not found")

    def edit_cart(self):
        self.logger.info("Editing cart")
        self.click(self._edit_cart_button)

    def click_continue(self):
        self.logger.info("Clicking continue button")
        self.click(self._continue_button)

    def is_error_message_displayed(self):
        self.logger.info("Checking if error message is displayed")
        return self.is_element_visible(self._error_message)

    def get_error_message(self):
        self.logger.info("Retrieving error message")
        if self.is_element_present(self._error_message):
            return self.get_text(self._error_message)
        return None

    def is_success_message_displayed(self):
        self.logger.info("Checking if success message is displayed")
        return self.is_element_visible(self._success_message)

    def get_success_message(self):
        self.logger.info("Retrieving success message")
        if self.is_element_present(self._success_message):
            return self.get_text(self._success_message)
        return None

    def is_warning_message_displayed(self):
        self.logger.info("Checking if warning message is displayed")
        return self.is_element_visible(self._warning_message)

    def get_warning_message(self):
        self.logger.info("Retrieving warning message")
        if self.is_element_present(self._warning_message):
            return self.get_text(self._warning_message)
        return None

    def get_all_product_names_in_cart(self):
        """Get all product names displayed in the cart."""
        self.logger.info("Getting all product names in cart")
        try:
            name_elements = self.driver.find_elements(*self._product_name)
            names = [elem.text for elem in name_elements]
            self.logger.info(f"Retrieved {len(names)} product names")
            return names
        except Exception as e:
            self.logger.error(f"Error getting product names: {e}")
            return []

    def get_all_product_prices_in_cart(self):
        """Get all product prices displayed in the cart."""
        self.logger.info("Getting all product prices in cart")
        try:
            price_elements = self.driver.find_elements(*self._product_price)
            prices = [elem.text for elem in price_elements]
            self.logger.info(f"Retrieved {len(prices)} product prices")
            return prices
        except Exception as e:
            self.logger.error(f"Error getting product prices: {e}")
            return []

    def remove_product_from_cart(self, product_index):
        """Remove a product from the cart by index."""
        self.logger.info(f"Removing product at index {product_index}")
        try:
            # Find all remove buttons and click the one at the specified index
            items = self.driver.find_elements(*self._product_item)
            if product_index < len(items):
                # Attempt to find remove button within the product item
                remove_button = items[product_index].find_element(By.XPATH, ".//button[contains(text(), 'Remove')]")
                remove_button.click()
                self.logger.info(f"Product at index {product_index} removed")
            else:
                self.logger.error(f"Product index {product_index} out of range")
        except Exception as e:
            self.logger.error(f"Error removing product: {e}")

    def get_cart_subtotal(self):
        """Get cart subtotal (wrapper for get_subtotal)."""
        return self.get_subtotal()



    def get_cart_total(self):
        """Get cart total (wrapper for get_total)."""
        return self.get_total()

    def update_product_quantity(self, product_index, new_quantity):
        """Update product quantity in the cart."""
        self.logger.info(f"Updating product {product_index} quantity to {new_quantity}")
        try:
            qty_fields = self.driver.find_elements(*self._product_quantity)
            if product_index < len(qty_fields):
                qty_fields[product_index].clear()
                qty_fields[product_index].send_keys(str(new_quantity))
                self.logger.info(f"Quantity updated for product {product_index}")
            else:
                self.logger.error(f"Product index {product_index} out of range")
        except Exception as e:
            self.logger.error(f"Error updating quantity: {e}")

    def update_cart(self):
        """Click update cart button to apply changes."""
        self.logger.info("Clicking update cart button")
        try:
            # Look for update button in the cart
            update_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Update')]")
            update_button.click()
            self.logger.info("Update cart button clicked")
        except Exception as e:
            self.logger.error(f"Error updating cart: {e}")


