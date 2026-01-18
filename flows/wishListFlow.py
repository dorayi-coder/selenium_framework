from pages.wishListPage import WishListPage
from pages.searchPage import SearchPage
from utilities.customLogger import LoggerFactory


class WishListFlow:
    logger = LoggerFactory.get_logger(__name__)

    def __init__(self, driver):
        self.driver = driver
        self.wishlist_page = WishListPage(driver)
        self.search_page = SearchPage(driver)

    def wait_for_wishlist_page_to_load(self):
        self.logger.info("Waiting for WishList page to load")
        self.wishlist_page.handle_cloudflare_if_present()
        if not self.wishlist_page.is_page_loaded():
            self.logger.error("WishList page failed to load")
            raise Exception("WishList page failed to load")
        self.logger.info("WishList page loaded successfully")

    def verify_wishlist_is_empty(self):
        self.logger.info("Verifying wishlist is empty")
        self.wait_for_wishlist_page_to_load()
        is_empty = self.wishlist_page.is_wishlist_empty()
        if is_empty:
            self.logger.info("Wishlist is empty as expected")
        else:
            self.logger.warning("Wishlist is not empty")
        return is_empty

    def verify_wishlist_has_items(self):
        self.logger.info("Verifying wishlist has items")
        self.wait_for_wishlist_page_to_load()
        count = self.wishlist_page.get_wishlist_item_count()
        has_items = count > 0
        if has_items:
            self.logger.info(f"Wishlist has {count} items")
        else:
            self.logger.warning("Wishlist has no items")
        return has_items

    def get_wishlist_item_count(self):
        self.logger.info("Getting wishlist item count")
        self.wait_for_wishlist_page_to_load()
        count = self.wishlist_page.get_wishlist_item_count()
        self.logger.info(f"Wishlist item count: {count}")
        return count

    def get_all_products_in_wishlist(self):
        self.logger.info("Retrieving all products in wishlist")
        self.wait_for_wishlist_page_to_load()
        products = self.wishlist_page.get_all_product_names()
        self.logger.info(f"Retrieved {len(products)} products from wishlist")
        return products

    def get_all_products_with_prices(self):
        self.logger.info("Retrieving all products with prices from wishlist")
        self.wait_for_wishlist_page_to_load()
        names = self.wishlist_page.get_all_product_names()
        prices = self.wishlist_page.get_all_product_prices()
        products_with_prices = list(zip(names, prices))
        self.logger.info(f"Retrieved {len(products_with_prices)} products with prices")
        return products_with_prices

    def get_all_products_with_details(self):
        self.logger.info("Retrieving all products with detailed information")
        self.wait_for_wishlist_page_to_load()
        names = self.wishlist_page.get_all_product_names()
        prices = self.wishlist_page.get_all_product_prices()
        skus = self.wishlist_page.get_all_product_skus()
        products_details = []
        for i, name in enumerate(names):
            details = {
                'name': name,
                'price': prices[i] if i < len(prices) else None,
                'sku': skus[i] if i < len(skus) else None
            }
            products_details.append(details)
        self.logger.info(f"Retrieved {len(products_details)} products with details")
        return products_details

    def verify_product_in_wishlist(self, product_name):
        self.logger.info(f"Verifying product '{product_name}' is in wishlist")
        self.wait_for_wishlist_page_to_load()
        is_present = self.wishlist_page.is_product_in_wishlist(product_name)
        if is_present:
            self.logger.info(f"Product '{product_name}' found in wishlist")
        else:
            self.logger.warning(f"Product '{product_name}' not found in wishlist")
        return is_present

    def remove_product_from_wishlist(self, product_name):
        self.logger.info(f"Removing product '{product_name}' from wishlist")
        self.wait_for_wishlist_page_to_load()
        success = self.wishlist_page.remove_product_by_name(product_name)
        if success:
            self.logger.info(f"Successfully removed '{product_name}' from wishlist")
        else:
            self.logger.error(f"Failed to remove '{product_name}' from wishlist")
        return success

    def add_product_to_cart_from_wishlist(self, product_name):
        self.logger.info(f"Adding product '{product_name}' to cart from wishlist")
        self.wait_for_wishlist_page_to_load()
        success = self.wishlist_page.add_product_to_cart_by_name(product_name)
        if success:
            self.logger.info(f"Successfully added '{product_name}' to cart from wishlist")
        else:
            self.logger.error(f"Failed to add '{product_name}' to cart from wishlist")
        return success

    def check_product_stock_status(self, product_name):
        self.logger.info(f"Checking stock status for product '{product_name}'")
        self.wait_for_wishlist_page_to_load()
        status = self.wishlist_page.get_product_stock_status_by_name(product_name)
        self.logger.info(f"Stock status for '{product_name}': {status}")
        return status

    def verify_product_in_stock(self, product_name):
        self.logger.info(f"Verifying product '{product_name}' is in stock")
        self.wait_for_wishlist_page_to_load()
        in_stock = self.wishlist_page.is_product_in_stock_by_name(product_name)
        if in_stock:
            self.logger.info(f"Product '{product_name}' is in stock")
        else:
            self.logger.warning(f"Product '{product_name}' is out of stock")
        return in_stock

    def add_all_products_to_cart(self):
        self.logger.info("Adding all wishlist items to cart")
        self.wait_for_wishlist_page_to_load()
        self.wishlist_page.select_all_items()
        success = self.wishlist_page.add_selected_items_to_cart()
        if success:
            self.logger.info("Successfully added all items to cart")
        else:
            self.logger.error("Failed to add all items to cart")
        return success

    def get_product_price_from_wishlist(self, product_name):
        self.logger.info(f"Getting price for product '{product_name}' from wishlist")
        self.wait_for_wishlist_page_to_load()
        price = self.wishlist_page.get_product_price_by_name(product_name)
        if price:
            self.logger.info(f"Price for '{product_name}': {price}")
        else:
            self.logger.warning(f"Could not retrieve price for '{product_name}'")
        return price

    def share_wishlist_with_others(self):
        self.logger.info("Sharing wishlist")
        self.wait_for_wishlist_page_to_load()
        success = self.wishlist_page.share_wishlist()
        if success:
            self.logger.info("Wishlist share dialog opened successfully")
            wishlist_url = self.wishlist_page.get_wishlist_url()
            return {'success': True, 'url': wishlist_url}
        else:
            self.logger.error("Failed to open wishlist share dialog")
            return {'success': False, 'url': None}

    def email_wishlist_to_friend(self, friend_email=None):
        self.logger.info(f"Emailing wishlist to friend: {friend_email}")
        self.wait_for_wishlist_page_to_load()
        success = self.wishlist_page.email_wishlist_to_friend()
        if success:
            self.logger.info("Email wishlist dialog opened successfully")
            return True
        else:
            self.logger.error("Failed to open email wishlist dialog")
            return False

    def remove_multiple_products_from_wishlist(self, product_names):
        self.logger.info(f"Removing multiple products from wishlist: {product_names}")
        self.wait_for_wishlist_page_to_load()
        results = {}
        for product_name in product_names:
            success = self.wishlist_page.remove_product_by_name(product_name)
            results[product_name] = success
            self.logger.info(f"Product '{product_name}' removal: {success}")
        return results

    def verify_product_not_in_wishlist(self, product_name):
        self.logger.info(f"Verifying product '{product_name}' is not in wishlist")
        self.wait_for_wishlist_page_to_load()
        is_present = self.wishlist_page.is_product_in_wishlist(product_name)
        not_present = not is_present
        if not_present:
            self.logger.info(f"Product '{product_name}' is not in wishlist as expected")
        else:
            self.logger.warning(f"Product '{product_name}' is still in wishlist")
        return not_present

    def get_wishlist_summary(self):
        self.logger.info("Getting wishlist summary")
        self.wait_for_wishlist_page_to_load()
        count = self.wishlist_page.get_wishlist_item_count()
        products = self.wishlist_page.get_all_product_names()
        prices = self.wishlist_page.get_all_product_prices()
        summary = {
            'item_count': count,
            'products': products,
            'prices': prices,
            'total_products': len(products)
        }
        self.logger.info(f"Wishlist summary: {count} items")
        return summary

    # ===== Flow Test Methods =====
    def validate_adding_product_to_wishlist_from_search_result_page(self, product_name):
        """
        Validate adding a product to WishList page from the search Result page.
        
        Executes workflow to search for product, add to wishlist from search results,
        and verify product appears in wishlist.
        
        Args:
            product_name (str): Product name to search and add to wishlist
            
        Returns:
            dict: Test result with search, add, and verification outcomes
        """
        try:
            self.logger.info(f"TEST: Validate adding product to WishList from search results")
            self.logger.info(f"Parameters: product='{product_name}'")
            
            # Search for product
            search_outcome = self.search_page.perform_product_search(product_name)
            search_executed = bool(search_outcome.get('search_successful'))
            
            if not search_executed:
                return self._build_wishlist_result(product_name, False, "Search failed")
            
            self.logger.debug("Product search successful")
            
            # Get all products in search results
            all_products = self.search_page.get_all_product_names()
            product_found_in_results = any(
                product_name.lower() in product.lower() for product in all_products
            )
            
            if not product_found_in_results:
                return self._build_wishlist_result(product_name, False, "Product not in search results")
            
            self.logger.debug(f"Product found in search results")
            
            # Try to add product to wishlist from search results
            add_to_wishlist_executed = False
            try:
                # Find and click add to wishlist button for the product in search results
                self.search_page.add_product_to_wishlist_from_results(product_name)
                add_to_wishlist_executed = True
                self.logger.debug("Add to wishlist executed from search results")
            except Exception as e:
                self.logger.error(f"Failed to add product to wishlist from search: {str(e)}")
            
            if not add_to_wishlist_executed:
                return self._build_wishlist_result(product_name, False, "Add to wishlist failed")
            
            # Navigate to wishlist page
            try:
                self.wishlist_page.navigate_to_wishlist()
                self.logger.debug("Navigated to wishlist page")
            except:
                self.logger.error("Failed to navigate to wishlist page")
                return self._build_wishlist_result(product_name, False, "Wishlist navigation failed")
            
            # Verify wishlist page loaded
            if not self.wishlist_page.is_page_loaded():
                return self._build_wishlist_result(product_name, False, "Wishlist page load failed")
            
            self.logger.debug("Wishlist page loaded")
            
            # Verify product is in wishlist
            products_in_wishlist = self.wishlist_page.get_all_product_names()
            product_found_in_wishlist = any(
                product_name.lower() in product.lower() for product in products_in_wishlist
            )
            
            wishlist_item_count = self.wishlist_page.get_wishlist_item_count()
            
            # Test result
            test_passed = (
                search_executed and
                product_found_in_results and
                add_to_wishlist_executed and
                product_found_in_wishlist
            )
            
            test_failure_reason = None
            if not test_passed:
                if not search_executed:
                    test_failure_reason = "Product search failed"
                elif not product_found_in_results:
                    test_failure_reason = "Product not found in search results"
                elif not add_to_wishlist_executed:
                    test_failure_reason = "Failed to add product to wishlist from search"
                elif not product_found_in_wishlist:
                    test_failure_reason = "Product not found in wishlist after add"
                else:
                    test_failure_reason = "Test failed at unknown validation point"
            
            if test_passed:
                self.logger.info("✓ TEST PASSED: Product successfully added to wishlist from search results")
            else:
                self.logger.error(f"✗ TEST FAILED: {test_failure_reason}")
            
            return {
                'test_case_title': "Validate adding a product to WishList page from the search Result page",
                'product_name': product_name,
                'search_executed': search_executed,
                'product_found_in_search_results': product_found_in_results,
                'add_to_wishlist_from_search_executed': add_to_wishlist_executed,
                'wishlist_page_loaded': True,
                'product_found_in_wishlist': product_found_in_wishlist,
                'wishlist_item_count': wishlist_item_count,
                'products_in_wishlist': products_in_wishlist,
                'test_passed': test_passed,
                'test_failure_reason': test_failure_reason
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_wishlist_result(product_name, False, str(e))

    def _build_wishlist_result(self, product_name, test_passed, failure_reason):
        """Build wishlist test result dictionary."""
        return {
            'test_case_title': "Validate adding a product to WishList page from the search Result page",
            'product_name': product_name,
            'search_executed': False,
            'product_found_in_search_results': False,
            'add_to_wishlist_from_search_executed': False,
            'wishlist_page_loaded': False,
            'product_found_in_wishlist': False,
            'wishlist_item_count': 0,
            'products_in_wishlist': [],
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }

    def validate_wishlist_page_title_url_and_heading(self):
        """
        Validate Page Title, Page URL and Page Heading of WishList Page.
        
        Verifies that wishlist page loads with correct title, URL, and heading.
        
        Returns:
            dict: Test result with page validation details
        """
        try:
            self.logger.info(f"TEST: Validate WishList page title, URL and heading")
            
            # Wait for wishlist page to load
            if not self.wishlist_page.is_page_loaded():
                return self._build_page_validation_result(False, "Wishlist page failed to load")
            
            # Get page title
            page_title = self.driver.title
            title_valid = page_title and "wishlist" in page_title.lower()
            
            # Get page URL
            page_url = self.driver.current_url
            url_valid = page_url and "wishlist" in page_url.lower()
            
            # Get page heading
            try:
                page_heading = self.wishlist_page.get_page_heading()
                heading_valid = page_heading and len(page_heading) > 0
            except:
                page_heading = None
                heading_valid = False
            
            self.logger.info(f"Page Title: {page_title}")
            self.logger.info(f"Page URL: {page_url}")
            self.logger.info(f"Page Heading: {page_heading}")
            
            # Test result
            test_passed = title_valid and url_valid and heading_valid
            
            test_failure_reason = None
            if not test_passed:
                reasons = []
                if not title_valid:
                    reasons.append("Page title is invalid or doesn't contain 'wishlist'")
                if not url_valid:
                    reasons.append("Page URL is invalid or doesn't contain 'wishlist'")
                if not heading_valid:
                    reasons.append("Page heading is missing or invalid")
                test_failure_reason = "; ".join(reasons)
            
            if test_passed:
                self.logger.info("✓ TEST PASSED: WishList page title, URL, and heading are valid")
            else:
                self.logger.error(f"✗ TEST FAILED: {test_failure_reason}")
            
            return {
                'test_case_title': "Validate the Page Title, Page URL and Page Heading of 'Wish List' Page",
                'page_title': page_title,
                'page_title_valid': title_valid,
                'page_url': page_url,
                'page_url_valid': url_valid,
                'page_heading': page_heading,
                'page_heading_valid': heading_valid,
                'page_loaded': True,
                'test_passed': test_passed,
                'test_failure_reason': test_failure_reason
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_page_validation_result(False, str(e))

    def _build_page_validation_result(self, test_passed, failure_reason):
        """Build page validation test result dictionary."""
        return {
            'test_case_title': "Validate the Page Title, Page URL and Page Heading of 'Wish List' Page",
            'page_title': None,
            'page_title_valid': False,
            'page_url': None,
            'page_url_valid': False,
            'page_heading': None,
            'page_heading_valid': False,
            'page_loaded': False,
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }

    def verify_product_is_added_to_wishlist_successfully(self, product_name):
        """
        Verify product is added to wishlist successfully.
        
        Adds a product to wishlist and verifies it exists in wishlist.
        
        Args:
            product_name (str): Product name to add to wishlist
            
        Returns:
            dict: Test result with add and verification outcomes
        """
        try:
            self.logger.info(f"TEST: Verify product is added to wishlist successfully")
            self.logger.info(f"Parameters: product='{product_name}'")
            
            # Get initial wishlist count
            initial_count = self.get_wishlist_item_count()
            self.logger.debug(f"Initial wishlist count: {initial_count}")
            
            # Add product to wishlist
            add_success = False
            try:
                self.wishlist_page.add_product_to_wishlist(product_name)
                add_success = True
                self.logger.debug("Product add to wishlist executed")
            except Exception as e:
                self.logger.error(f"Failed to add product to wishlist: {str(e)}")
            
            if not add_success:
                return self._build_add_wishlist_result(product_name, False, "Add to wishlist failed")
            
            # Get updated wishlist count
            updated_count = self.get_wishlist_item_count()
            count_increased = updated_count > initial_count
            
            self.logger.debug(f"Updated wishlist count: {updated_count}")
            
            # Verify product in wishlist
            products_in_wishlist = self.wishlist_page.get_all_product_names()
            product_found = any(
                product_name.lower() in product.lower() for product in products_in_wishlist
            )
            
            # Test result
            test_passed = add_success and product_found and count_increased
            
            test_failure_reason = None
            if not test_passed:
                if not add_success:
                    test_failure_reason = "Failed to add product to wishlist"
                elif not product_found:
                    test_failure_reason = "Product not found in wishlist after add"
                elif not count_increased:
                    test_failure_reason = "Wishlist count did not increase after add"
                else:
                    test_failure_reason = "Test failed at unknown validation point"
            
            if test_passed:
                self.logger.info("✓ TEST PASSED: Product successfully added to wishlist")
            else:
                self.logger.error(f"✗ TEST FAILED: {test_failure_reason}")
            
            return {
                'test_case_title': "Verify Product is added to wishlist successfully",
                'product_name': product_name,
                'add_to_wishlist_executed': add_success,
                'initial_wishlist_count': initial_count,
                'updated_wishlist_count': updated_count,
                'wishlist_count_increased': count_increased,
                'product_found_in_wishlist': product_found,
                'products_in_wishlist': products_in_wishlist,
                'test_passed': test_passed,
                'test_failure_reason': test_failure_reason
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_add_wishlist_result(product_name, False, str(e))

    def _build_add_wishlist_result(self, product_name, test_passed, failure_reason):
        """Build add to wishlist test result dictionary."""
        return {
            'test_case_title': "Verify Product is added to wishlist successfully",
            'product_name': product_name,
            'add_to_wishlist_executed': False,
            'initial_wishlist_count': 0,
            'updated_wishlist_count': 0,
            'wishlist_count_increased': False,
            'product_found_in_wishlist': False,
            'products_in_wishlist': [],
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }

    def verify_wish_list_reflects_updated_product_price(self, product_name):
        """
        Verify Wish List reflects updated product price.
        
        Gets product price from wishlist and verifies it is displayed correctly.
        
        Args:
            product_name (str): Product name to check price
            
        Returns:
            dict: Test result with price validation
        """
        try:
            self.logger.info(f"TEST: Verify Wish List reflects updated product price")
            self.logger.info(f"Parameters: product='{product_name}'")
            
            # Verify wishlist page loaded
            if not self.wishlist_page.is_page_loaded():
                return self._build_price_result(product_name, False, "Wishlist page load failed")
            
            # Get product price from wishlist
            try:
                product_price = self.wishlist_page.get_product_price(product_name)
                price_found = product_price is not None and product_price > 0
                self.logger.debug(f"Product price in wishlist: {product_price}")
            except Exception as e:
                self.logger.error(f"Failed to get product price: {str(e)}")
                return self._build_price_result(product_name, False, "Failed to retrieve price")
            
            if not price_found:
                return self._build_price_result(product_name, False, "Product price is invalid or zero")
            
            # Verify product exists in wishlist
            products = self.wishlist_page.get_all_product_names()
            product_found = any(
                product_name.lower() in product.lower() for product in products
            )
            
            if not product_found:
                return self._build_price_result(product_name, False, "Product not found in wishlist")
            
            # Get all prices to verify price display
            all_prices = self.wishlist_page.get_all_product_prices()
            prices_displayed = len(all_prices) > 0
            
            # Test result
            test_passed = price_found and product_found and prices_displayed
            
            test_failure_reason = None
            if not test_passed:
                if not price_found:
                    test_failure_reason = "Product price not found or invalid"
                elif not product_found:
                    test_failure_reason = "Product not found in wishlist"
                elif not prices_displayed:
                    test_failure_reason = "Prices not displayed in wishlist"
                else:
                    test_failure_reason = "Test failed at unknown validation point"
            
            if test_passed:
                self.logger.info("✓ TEST PASSED: Wish List reflects updated product price")
            else:
                self.logger.error(f"✗ TEST FAILED: {test_failure_reason}")
            
            return {
                'test_case_title': "Verify Wish List reflects updated product price",
                'product_name': product_name,
                'product_found_in_wishlist': product_found,
                'product_price': product_price,
                'price_valid': price_found,
                'all_prices_displayed': all_prices,
                'total_products_with_prices': len(all_prices),
                'prices_display_working': prices_displayed,
                'test_passed': test_passed,
                'test_failure_reason': test_failure_reason
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_price_result(product_name, False, str(e))

    def _build_price_result(self, product_name, test_passed, failure_reason):
        """Build price validation test result dictionary."""
        return {
            'test_case_title': "Verify Wish List reflects updated product price",
            'product_name': product_name,
            'product_found_in_wishlist': False,
            'product_price': None,
            'price_valid': False,
            'all_prices_displayed': [],
            'total_products_with_prices': 0,
            'prices_display_working': False,
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }

    def verify_wish_list_updates_immediately_after_product_removal(self, product_name):
        """
        Verify Wish List updates immediately after product removal.
        
        Removes a product from wishlist and verifies the list updates immediately.
        
        Args:
            product_name (str): Product name to remove from wishlist
            
        Returns:
            dict: Test result with removal and update validation
        """
        try:
            self.logger.info(f"TEST: Verify Wish List updates immediately after product removal")
            self.logger.info(f"Parameters: product='{product_name}'")
            
            # Verify wishlist page loaded
            if not self.wishlist_page.is_page_loaded():
                return self._build_removal_result(product_name, False, "Wishlist page load failed")
            
            # Get initial wishlist count
            initial_count = self.get_wishlist_item_count()
            self.logger.debug(f"Initial wishlist count: {initial_count}")
            
            # Verify product exists in wishlist
            products_before = self.wishlist_page.get_all_product_names()
            product_exists = any(
                product_name.lower() in product.lower() for product in products_before
            )
            
            if not product_exists:
                return self._build_removal_result(product_name, False, "Product not found in wishlist")
            
            # Remove product from wishlist
            remove_success = False
            try:
                self.wishlist_page.remove_product_from_wishlist(product_name)
                remove_success = True
                self.logger.debug("Product removed from wishlist")
            except Exception as e:
                self.logger.error(f"Failed to remove product: {str(e)}")
            
            if not remove_success:
                return self._build_removal_result(product_name, False, "Product removal failed")
            
            # Get updated wishlist count
            updated_count = self.get_wishlist_item_count()
            count_decreased = updated_count < initial_count
            
            self.logger.debug(f"Updated wishlist count: {updated_count}")
            
            # Verify product removed from wishlist
            products_after = self.wishlist_page.get_all_product_names()
            product_removed = not any(
                product_name.lower() in product.lower() for product in products_after
            )
            
            # Test result
            test_passed = remove_success and product_removed and count_decreased
            
            test_failure_reason = None
            if not test_passed:
                if not remove_success:
                    test_failure_reason = "Failed to remove product from wishlist"
                elif not product_removed:
                    test_failure_reason = "Product still exists in wishlist after removal"
                elif not count_decreased:
                    test_failure_reason = "Wishlist count did not decrease after removal"
                else:
                    test_failure_reason = "Test failed at unknown validation point"
            
            if test_passed:
                self.logger.info("✓ TEST PASSED: Wish List updated immediately after product removal")
            else:
                self.logger.error(f"✗ TEST FAILED: {test_failure_reason}")
            
            return {
                'test_case_title': "Verify Wish List updates immediately after product removal",
                'product_name': product_name,
                'product_existed_before': product_exists,
                'remove_executed': remove_success,
                'initial_wishlist_count': initial_count,
                'updated_wishlist_count': updated_count,
                'wishlist_count_decreased': count_decreased,
                'product_removed_from_list': product_removed,
                'products_before_removal': products_before,
                'products_after_removal': products_after,
                'test_passed': test_passed,
                'test_failure_reason': test_failure_reason
            }
            
        except Exception as e:
            self.logger.error(f"Test execution failed: {str(e)}")
            return self._build_removal_result(product_name, False, str(e))

    def _build_removal_result(self, product_name, test_passed, failure_reason):
        """Build product removal test result dictionary."""
        return {
            'test_case_title': "Verify Wish List updates immediately after product removal",
            'product_name': product_name,
            'product_existed_before': False,
            'remove_executed': False,
            'initial_wishlist_count': 0,
            'updated_wishlist_count': 0,
            'wishlist_count_decreased': False,
            'product_removed_from_list': False,
            'products_before_removal': [],
            'products_after_removal': [],
            'test_passed': test_passed,
            'test_failure_reason': failure_reason
        }
