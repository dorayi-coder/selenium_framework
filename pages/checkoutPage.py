from selenium.webdriver.common.by import By
from utilities.basePage import BasePage
from utilities.customLogger import LoggerFactory


class CheckoutPage(BasePage):
    logger = LoggerFactory.get_logger(__name__)

        
    _checkout_page_title = (By.XPATH, "//h1[contains(text(), 'Checkout')]")
    _checkout_progress = (By.CLASS_NAME, "checkout-progress")
    _billing_address_section = (By.ID, "billing-address-section")
    _existing_address_option = (By.XPATH, "//input[@value='existing']")
    _new_address_option = (By.XPATH, "//input[@value='new']")
    _address_dropdown = (By.ID, "address-select")
    _first_name_input = (By.ID, "BillingNewAddress_FirstName")
    _last_name_input = (By.ID, "BillingNewAddress_LastName")
    _email_input = (By.ID, "BillingNewAddress_Email")
    _phone_input = (By.ID, "BillingNewAddress_PhoneNumber")
    _country_dropdown = (By.ID, "BillingNewAddress_CountryId")
    _state_dropdown = (By.ID, "BillingNewAddress_StateProvinceId")
    _city_input = (By.ID, "BillingNewAddress_City")
    _address1_input = (By.ID, "BillingNewAddress_Address1")
    _address2_input = (By.ID, "BillingNewAddress_Address2")
    _postal_code_input = (By.ID, "BillingNewAddress_ZipPostalCode")
    _company_input = (By.ID, "BillingNewAddress_Company")
    _continue_billing_button = (By.XPATH, "//button[contains(text(), 'Continue')][@name='save-billing']")
    _billing_form = (By.ID, "billing-form")
    _shipping_address_same_checkbox = (By.ID, "ShippingAddressSameAsBillingAddress")
    _shipping_address_section = (By.ID, "shipping-address-section")
    _shipping_first_name_input = (By.ID, "ShippingNewAddress_FirstName")
    _shipping_last_name_input = (By.ID, "ShippingNewAddress_LastName")
    _shipping_email_input = (By.ID, "ShippingNewAddress_Email")
    _shipping_phone_input = (By.ID, "ShippingNewAddress_PhoneNumber")
    _shipping_country_dropdown = (By.ID, "ShippingNewAddress_CountryId")
    _shipping_state_dropdown = (By.ID, "ShippingNewAddress_StateProvinceId")
    _shipping_city_input = (By.ID, "ShippingNewAddress_City")
    _shipping_address1_input = (By.ID, "ShippingNewAddress_Address1")
    _shipping_address2_input = (By.ID, "ShippingNewAddress_Address2")
    _shipping_postal_code_input = (By.ID, "ShippingNewAddress_ZipPostalCode")
    _shipping_company_input = (By.ID, "ShippingNewAddress_Company")
    _continue_shipping_button = (By.XPATH, "//button[contains(text(), 'Continue')][@name='save-shipping']")
    _shipping_method_section = (By.ID, "shipping-method-section")
    _shipping_method_radio = (By.NAME, "shippingoption")
    _continue_shipping_method_button = (By.XPATH, "//button[contains(text(), 'Continue')][@name='save-shipping-method']")
    _payment_method_section = (By.ID, "payment-method-section")
    _payment_method_radio = (By.NAME, "paymentmethod")
    _payment_information_section = (By.ID, "payment-information-section")
    _continue_payment_button = (By.XPATH, "//button[contains(text(), 'Continue')][@name='save-payment-method']")
    _confirm_order_button = (By.XPATH, "//button[contains(text(), 'Confirm')]")
    _order_review_section = (By.ID, "order-review")
    _error_message = (By.CLASS_NAME, "error-message")
    _validation_error = (By.CLASS_NAME, "field-validation-error")
    _back_button = (By.XPATH, "//button[contains(text(), 'Back')]")
    _cart_summary = (By.CLASS_NAME, "cart-summary")
    _order_total = (By.CLASS_NAME, "order-total")

    def is_page_loaded(self):
        self.logger.info("Checking if Checkout page is loaded")
        return self.is_element_visible(self._checkout_page_title)



    def select_existing_billing_address(self):
        self.logger.info("Selecting existing billing address")
        try:
            self.click(self._existing_address_option)
            self.logger.info("Existing billing address option selected")
            return True
        except:
            self.logger.error("Failed to select existing billing address")
            return False

    def select_new_billing_address(self):
        self.logger.info("Selecting new billing address")
        try:
            self.click(self._new_address_option)
            self.logger.info("New billing address option selected")
            return True
        except:
            self.logger.error("Failed to select new billing address")
            return False

    def select_billing_address_from_dropdown(self, address_id):
        self.logger.info(f"Selecting billing address from dropdown: {address_id}")
        try:
            self.select_dropdown(self._address_dropdown, address_id)
            self.logger.info(f"Billing address selected: {address_id}")
            return True
        except:
            self.logger.error(f"Failed to select billing address: {address_id}")
            return False

    def enter_billing_first_name(self, first_name):
        self.logger.info(f"Entering billing first name: {first_name}")
        self.type(self._first_name_input, first_name)

    def enter_billing_last_name(self, last_name):
        self.logger.info(f"Entering billing last name: {last_name}")
        self.type(self._last_name_input, last_name)

    def enter_billing_email(self, email):
        self.logger.info(f"Entering billing email: {email}")
        self.type(self._email_input, email)

    def enter_billing_phone(self, phone):
        self.logger.info(f"Entering billing phone: {phone}")
        self.type(self._phone_input, phone)

    def enter_billing_company(self, company):
        self.logger.info(f"Entering billing company: {company}")
        self.type(self._company_input, company)

    def select_billing_country(self, country_name):
        self.logger.info(f"Selecting billing country: {country_name}")
        self.select_dropdown(self._country_dropdown, country_name)

    def select_billing_state(self, state_name):
        self.logger.info(f"Selecting billing state: {state_name}")
        self.select_dropdown(self._state_dropdown, state_name)

    def enter_billing_city(self, city):
        self.logger.info(f"Entering billing city: {city}")
        self.type(self._city_input, city)

    def enter_billing_address1(self, address):
        self.logger.info(f"Entering billing address line 1: {address}")
        self.type(self._address1_input, address)

    def enter_billing_address2(self, address):
        self.logger.info(f"Entering billing address line 2: {address}")
        self.type(self._address2_input, address)

    def enter_billing_postal_code(self, postal_code):
        self.logger.info(f"Entering billing postal code: {postal_code}")
        self.type(self._postal_code_input, postal_code)

    def continue_from_billing_address(self):
        self.logger.info("Continuing from billing address section")
        self.click(self._continue_billing_button)

    def check_shipping_same_as_billing(self):
        self.logger.info("Checking shipping address same as billing")
        if not self.is_checkbox_selected(self._shipping_address_same_checkbox):
            self.click(self._shipping_address_same_checkbox)
            self.logger.info("Shipping address same as billing checkbox checked")

    def uncheck_shipping_same_as_billing(self):
        self.logger.info("Unchecking shipping address same as billing")
        if self.is_checkbox_selected(self._shipping_address_same_checkbox):
            self.click(self._shipping_address_same_checkbox)
            self.logger.info("Shipping address same as billing checkbox unchecked")

    def enter_shipping_first_name(self, first_name):
        self.logger.info(f"Entering shipping first name: {first_name}")
        self.type(self._shipping_first_name_input, first_name)

    def enter_shipping_last_name(self, last_name):
        self.logger.info(f"Entering shipping last name: {last_name}")
        self.type(self._shipping_last_name_input, last_name)

    def enter_shipping_email(self, email):
        self.logger.info(f"Entering shipping email: {email}")
        self.type(self._shipping_email_input, email)

    def enter_shipping_phone(self, phone):
        self.logger.info(f"Entering shipping phone: {phone}")
        self.type(self._shipping_phone_input, phone)

    def enter_shipping_company(self, company):
        self.logger.info(f"Entering shipping company: {company}")
        self.type(self._shipping_company_input, company)

    def select_shipping_country(self, country_name):
        self.logger.info(f"Selecting shipping country: {country_name}")
        self.select_dropdown(self._shipping_country_dropdown, country_name)

    def select_shipping_state(self, state_name):
        self.logger.info(f"Selecting shipping state: {state_name}")
        self.select_dropdown(self._shipping_state_dropdown, state_name)

    def enter_shipping_city(self, city):
        self.logger.info(f"Entering shipping city: {city}")
        self.type(self._shipping_city_input, city)

    def enter_shipping_address1(self, address):
        self.logger.info(f"Entering shipping address line 1: {address}")
        self.type(self._shipping_address1_input, address)

    def enter_shipping_address2(self, address):
        self.logger.info(f"Entering shipping address line 2: {address}")
        self.type(self._shipping_address2_input, address)

    def enter_shipping_postal_code(self, postal_code):
        self.logger.info(f"Entering shipping postal code: {postal_code}")
        self.type(self._shipping_postal_code_input, postal_code)

    def continue_from_shipping_address(self):
        self.logger.info("Continuing from shipping address section")
        self.click(self._continue_shipping_button)

    def select_shipping_method(self, method_value):
        self.logger.info(f"Selecting shipping method: {method_value}")
        shipping_methods = self.driver.find_elements(*self._shipping_method_radio)
        for method in shipping_methods:
            try:
                if method.get_attribute("value") == method_value:
                    method.click()
                    self.logger.info(f"Shipping method selected: {method_value}")
                    return True
            except:
                self.logger.warning(f"Failed to select shipping method: {method_value}")
        self.logger.error(f"Shipping method not found: {method_value}")
        return False

    def continue_from_shipping_method(self):
        self.logger.info("Continuing from shipping method section")
        self.click(self._continue_shipping_method_button)

    def select_payment_method(self, method_value):
        self.logger.info(f"Selecting payment method: {method_value}")
        payment_methods = self.driver.find_elements(*self._payment_method_radio)
        for method in payment_methods:
            try:
                if method.get_attribute("value") == method_value:
                    method.click()
                    self.logger.info(f"Payment method selected: {method_value}")
                    return True
            except:
                self.logger.warning(f"Failed to select payment method: {method_value}")
        self.logger.error(f"Payment method not found: {method_value}")
        return False

    def continue_from_payment_method(self):
        self.logger.info("Continuing from payment method section")
        self.click(self._continue_payment_button)

    def get_order_total(self):
        self.logger.info("Getting order total")
        try:
            total = self.get_text(self._order_total)
            self.logger.info(f"Order total: {total}")
            return total
        except:
            self.logger.error("Failed to get order total")
            return None

    def confirm_order(self):
        self.logger.info("Confirming order")
        self.click(self._confirm_order_button)

    def is_error_message_displayed(self):
        self.logger.info("Checking if error message is displayed")
        return self.is_element_visible(self._error_message)

    def get_error_message(self):
        self.logger.info("Getting error message")
        try:
            error = self.get_text(self._error_message)
            self.logger.warning(f"Error message: {error}")
            return error
        except:
            self.logger.warning("Failed to get error message")
            return None

    def click_back_button(self):
        self.logger.info("Clicking back button")
        self.click(self._back_button)

    def is_order_review_visible(self):
        self.logger.info("Checking if order review section is visible")
        return self.is_element_visible(self._order_review_section)

    def get_cart_summary(self):
        self.logger.info("Getting cart summary")
        try:
            summary = self.get_text(self._cart_summary)
            self.logger.info(f"Cart summary retrieved")
            return summary
        except:
            self.logger.error("Failed to get cart summary")
            return None
