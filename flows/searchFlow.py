from pages.searchPage import SearchPage
from pages.homePage import HomePage
from utilities.customLogger import LoggerFactory


class SearchFlow:
   
    logger = LoggerFactory.get_logger(__name__)

    def __init__(self, driver):
        """
        Initialize the search flow with page objects.
        
        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.home_page = HomePage(driver)
        self.search_page = SearchPage(driver)

    # ===== Core Search Workflow =====
    def search_product_by_keyword(self, keyword):
        """
        Execute the product search workflow.
        
        Assumes the search page is already loaded.
        
        Workflow:
        1. Enter the product name/keyword into the search field
        2. Click the search button
        3. Wait for results to load
        
        Args:
            keyword (str): The product name or search term
            
        Note:
            Does not perform assertions. Caller verifies search results 
            via get_search_results() or is_search_successful()
        """
        self.logger.info(f"Searching for product with keyword: {keyword}")
        self.search_page.wait_for_page_to_load()
        self.search_page.search_for_product(keyword)
        self.logger.info(f"Search submitted for keyword: {keyword}")

    # ===== Complete Search Workflow (with Navigation) =====
    def perform_product_search(self, keyword):
        """
        Execute the COMPLETE product search workflow from start to finish.
        
        Workflow:
        1. Open the application home page (https://demo.nopcommerce.com/)
        2. Enter product name into the search field
        3. Click the search button
        4. Return observable UI outcomes (results list, empty state, messages)
        
        Args:
            keyword (str): The product name or search term to search for
            
        Returns:
            dict: Observable UI outcome containing:
                - 'keyword': str of the searched keyword
                - 'has_results': bool indicating if results are displayed
                - 'result_count': int number of products found
                - 'is_empty': bool indicating if search returned no results
                - 'no_results_message': str message if no results
                - 'error_message': str message if error occurred
                - 'page_url': str of final page URL
                
        Note:
            Does not perform assertions. Caller determines test success 
            by examining returned data structure.
        """
        self.logger.info(f"Starting complete product search for keyword: {keyword}")
        
        # Perform the search
        self.search_product_by_keyword(keyword)
        
        # Capture observable outcomes
        outcome = self._capture_search_outcome(keyword)
        
        self.logger.info(f"Product search completed. Results: {outcome['result_count']} items found")
        return outcome

    def _capture_search_outcome(self, keyword):
        """
        Capture the current observable state of the search results page.
        Helper method to collect all relevant UI state data.
        
        Args:
            keyword (str): The searched keyword
            
        Returns:
            dict: Complete search outcome data
        """
        has_results = self.search_page.are_search_results_displayed()
        result_count = self.search_page.get_number_of_results() if has_results else 0
        is_empty = self.search_page.are_results_empty()
        
        no_results_msg = None
        if self.search_page.is_no_results_message_displayed():
            no_results_msg = self.search_page.get_no_results_message()
        
        error_msg = None
        if self.search_page.is_any_error_displayed():
            error_msg = self.search_page.get_error_message()
        
        return {
            'keyword': keyword,
            'has_results': has_results,
            'result_count': result_count,
            'is_empty': is_empty,
            'no_results_message': no_results_msg,
            'error_message': error_msg,
            'page_url': self.driver.current_url
        }

    # ===== Observable Search State Methods (for test verification) =====
    def verify_search_results_displayed(self):
        """
        Check if search results container is currently displayed.
        
        Returns:
            bool: True if results container visible, False otherwise
        """
        self.logger.info("Verifying search results are displayed")
        results_displayed = self.search_page.are_search_results_displayed()
        if results_displayed:
            self.logger.info("Search results successfully displayed")
            return True
        else:
            self.logger.warning("Search results not displayed")
            return False

    def verify_search_results_not_empty(self):
        """
        Check if search results are not empty (at least one product found).
        
        Returns:
            bool: True if results not empty, False if empty
        """
        self.logger.info("Verifying search results are not empty")
        result_count = self.get_search_result_count()
        if result_count > 0:
            self.logger.info("Search results are not empty")
            return True
        else:
            self.logger.warning("Search results are empty")
            return False

    def verify_search_results_empty(self):
        """
        Check if search returned no results (empty state).
        
        Returns:
            bool: True if results are empty, False if results found
        """
        self.logger.info("Verifying search results are empty")
        return self.search_page.are_results_empty()

    # ===== Search Result Count =====
    def get_search_result_count(self):
        """
        Get the count of product items in current search results.
        
        Returns:
            int: Number of products found, 0 if none
        """
        self.logger.info("Getting count of search results")
        result_count = self.search_page.get_number_of_results()
        self.logger.info(f"Search result count: {result_count}")
        return result_count

    # ===== Product Data Retrieval =====
    def get_first_product_from_results(self):
        """
        Retrieve the name of the first product in search results.
        
        Returns:
            str: First product name, or None if no results
        """
        self.logger.info("Retrieving first product from search results")
        product_name = self.search_page.get_first_product_name()
        if product_name:
            self.logger.info(f"First product retrieved: {product_name}")
            return product_name
        else:
            self.logger.warning("No first product found")
            return None

    def get_all_products_from_results(self):
        """
        Retrieve all product names from the current search results page.
        
        Returns:
            list: List of product name strings, empty list if no results
        """
        self.logger.info("Retrieving all products from search results")
        product_names = self.search_page.get_all_product_names()
        self.logger.info(f"Retrieved {len(product_names)} products")
        return product_names

    def get_all_product_prices_from_results(self):
        """
        Retrieve all product prices from the current search results page.
        
        Returns:
            list: List of price strings, empty list if no results
        """
        self.logger.info("Retrieving all product prices from search results")
        product_prices = self.search_page.get_all_product_prices()
        self.logger.info(f"Retrieved {len(product_prices)} product prices")
        return product_prices

    # ===== No Results State Methods =====
    def verify_no_results_message(self):
        """
        Check if the "No products found" message is displayed.
        Indicates that search returned no results.
        
        Returns:
            bool: True if no results message visible, False otherwise
        """
        self.logger.info("Verifying no results message is displayed")
        no_results = self.search_page.is_no_results_message_displayed()
        if no_results:
            self.logger.info("No results message displayed successfully")
            return True
        else:
            self.logger.warning("No results message not displayed")
            return False

    def get_no_results_message(self):
        """
        Retrieve the "No products found" message text.
        
        Returns:
            str: Message text, or None if not displayed
        """
        self.logger.info("Retrieving no results message")
        return self.search_page.get_no_results_message()

    # ===== Error State Methods =====
    def verify_search_has_error(self):
        """
        Check if any error is displayed on the search page.
        
        Returns:
            bool: True if error visible, False otherwise
        """
        self.logger.info("Verifying search has error")
        has_error = self.search_page.is_any_error_displayed()
        if has_error:
            self.logger.warning("Search error detected")
            return True
        else:
            self.logger.info("No search error detected")
            return False

    def get_search_error_message(self):
        """
        Retrieve any error message from the search page.
        
        Returns:
            str: Error message text, or None if no error
        """
        self.logger.info("Retrieving search error message")
        error_message = self.search_page.get_error_message()
        if error_message:
            self.logger.warning(f"Search error: {error_message}")
            return error_message
        return None

    # ===== Advanced Search Navigation =====
    def navigate_to_advanced_search(self):
        """
        Navigate to the advanced search page.
        Does not verify successful navigation; caller handles verification.
        """
        self.logger.info("Navigating to advanced search")
        self.search_page.wait_for_page_to_load()
        self.search_page.click_advanced_search()
        self.logger.info("Advanced search navigation initiated")

    # ===== Pagination Navigation =====
    def navigate_to_next_search_results_page(self):
        """
        Navigate to the next page of search results if pagination available.
        Logs warning if pagination not available.
        """
        self.logger.info("Navigating to next search results page")
        if self.search_page.is_pagination_available():
            self.search_page.click_next_page()
            self.logger.info("Navigation to next page initiated")
        else:
            self.logger.warning("Pagination not available")

    def navigate_to_previous_search_results_page(self):
        """
        Navigate to the previous page of search results if pagination available.
        Logs warning if pagination not available.
        """
        self.logger.info("Navigating to previous search results page")
        if self.search_page.is_pagination_available():
            self.search_page.click_previous_page()
            self.logger.info("Navigation to previous page initiated")
        else:
            self.logger.warning("Pagination not available")

    # ===== Multiple Search & Combined Operations =====
    def perform_multiple_searches(self, keywords):
        """
        Perform multiple searches sequentially with different keywords.
        Useful for testing search functionality across various terms.
        
        Args:
            keywords (list): List of product names/search terms to search for
            
        Returns:
            dict: Dictionary mapping each keyword to its result count
        """
        self.logger.info(f"Performing multiple searches for keywords: {keywords}")
        search_results = {}
        for keyword in keywords:
            self.logger.info(f"Searching for keyword: {keyword}")
            self.search_product_by_keyword(keyword)
            result_count = self.get_search_result_count()
            search_results[keyword] = result_count
            self.logger.info(f"Search results for '{keyword}': {result_count}")
        return search_results

    def search_and_get_products(self, keyword):
        """
        Search for a product and retrieve all matching product names.
        Combined operation for convenience.
        
        Args:
            keyword (str): The product name or search term
            
        Returns:
            list: List of product name strings, empty if no results
        """
        self.logger.info(f"Searching and retrieving products for keyword: {keyword}")
        self.search_product_by_keyword(keyword)
        if self.verify_search_results_displayed():
            products = self.get_all_products_from_results()
            self.logger.info(f"Retrieved {len(products)} products for keyword: {keyword}")
            return products
        else:
            self.logger.warning(f"No results displayed for keyword: {keyword}")
            return []

    def search_and_get_product_prices(self, keyword):
        """
        Search for a product and retrieve all matching product prices.
        Combined operation for convenience.
        
        Args:
            keyword (str): The product name or search term
            
        Returns:
            list: List of price strings, empty if no results
        """
        self.logger.info(f"Searching and retrieving product prices for keyword: {keyword}")
        self.search_product_by_keyword(keyword)
        if self.verify_search_results_displayed():
            prices = self.get_all_product_prices_from_results()
            self.logger.info(f"Retrieved {len(prices)} product prices for keyword: {keyword}")
            return prices
        else:
            self.logger.warning(f"No results displayed for keyword: {keyword}")
            return []

    # ===== Validation Methods =====
    def validate_search_with_existing_product_name(self, product_name):
        """
        Validate searching with an existing product name.
        
        Executes a search for a known product and validates that:
        1. Search results are displayed
        2. At least one product is found
        3. The searched product appears in results
        
        Observable outcomes are returned for caller validation.
        
        Args:
            product_name (str): An existing product name to search for
            
        Returns:
            dict: Validation outcome containing:
                - 'product_name': str of the searched product
                - 'search_successful': bool indicating if results found
                - 'results_displayed': bool indicating if results container visible
                - 'result_count': int number of products found
                - 'first_product': str name of first product in results
                - 'all_products': list of all product names found
                - 'searched_product_found': bool indicating if product appears in results
                - 'validation_passed': bool indicating overall validation success
                - 'page_url': str of final page URL
                
        Note:
            Does not perform assertions. Caller determines validation success 
            by examining 'validation_passed' flag and other returned fields.
        """
        self.logger.info(f"Validating search with existing product name: {product_name}")
        
        # Execute search
        self.search_product_by_keyword(product_name)
        
        # Capture results
        results_displayed = self.search_page.are_search_results_displayed()
        result_count = self.search_page.get_number_of_results() if results_displayed else 0
        first_product = self.search_page.get_first_product_name() if result_count > 0 else None
        all_products = self.search_page.get_all_product_names() if results_displayed else []
        
        # Validate: check if searched product appears in results
        searched_product_found = any(product_name.lower() in product.lower() for product in all_products)
        
        # Determine overall validation success
        validation_passed = (
            results_displayed and 
            result_count > 0 and 
            searched_product_found
        )
        
        self.logger.info(
            f"Search validation for '{product_name}': "
            f"Results={results_displayed}, Count={result_count}, Found={searched_product_found}, Passed={validation_passed}"
        )
        
        return {
            'product_name': product_name,
            'search_successful': result_count > 0,
            'results_displayed': results_displayed,
            'result_count': result_count,
            'first_product': first_product,
            'all_products': all_products,
            'searched_product_found': searched_product_found,
            'validation_passed': validation_passed,
            'page_url': self.driver.current_url
        }

    def validate_search_using_search_criteria_field(self, search_criteria):
        """
        Validate searching functionality using the search criteria field.
        
        Executes a complete validation workflow for the search criteria field:
        1. Verify search input field is visible and accessible
        2. Enter search criteria into the field
        3. Verify input is properly accepted
        4. Click search button
        5. Verify search results are displayed
        
        Observable outcomes are returned for caller validation.
        
        Args:
            search_criteria (str): The search criteria/term to test
            
        Returns:
            dict: Validation outcome containing:
                - 'search_criteria': str of the search term tested
                - 'input_field_visible': bool indicating field is visible
                - 'input_field_accepts_input': bool indicating input was accepted
                - 'input_field_value': str actual value in field after entry
                - 'search_button_visible': bool indicating button is visible
                - 'search_submitted': bool indicating search was submitted successfully
                - 'results_displayed': bool indicating results are visible after search
                - 'result_count': int number of products found
                - 'has_results': bool indicating if results exist
                - 'validation_passed': bool indicating overall validation success
                - 'page_url': str of final page URL
                
        Note:
            Does not perform assertions. Caller determines validation success 
            by examining 'validation_passed' flag and detailed outcome fields.
        """
        self.logger.info(f"Validating search using search criteria field: {search_criteria}")
        
        # Ensure page is loaded
        self.search_page.wait_for_page_to_load()
        
        # Validate search criteria input at page level
        criteria_validation = self.search_page.validate_search_criteria_input(search_criteria)
        
        # Capture additional results data after search
        result_count = 0
        has_results = False
        
        if criteria_validation['results_displayed']:
            result_count = self.search_page.get_number_of_results()
            has_results = result_count > 0
        
        # Determine overall validation success
        validation_passed = (
            criteria_validation['validation_passed'] and 
            criteria_validation['results_displayed']
        )
        
        self.logger.info(
            f"Search criteria validation for '{search_criteria}': "
            f"Input={criteria_validation['input_field_accepts_input']}, "
            f"Submitted={criteria_validation['search_submitted']}, "
            f"Results={criteria_validation['results_displayed']}, "
            f"Count={result_count}, Passed={validation_passed}"
        )
        
        return {
            'search_criteria': search_criteria,
            'input_field_visible': criteria_validation['input_field_visible'],
            'input_field_accepts_input': criteria_validation['input_field_accepts_input'],
            'input_field_value': criteria_validation['input_field_value'],
            'search_button_visible': criteria_validation['search_button_visible'],
            'search_submitted': criteria_validation['search_submitted'],
            'results_displayed': criteria_validation['results_displayed'],
            'result_count': result_count,
            'has_results': has_results,
            'validation_passed': validation_passed,
            'page_url': self.driver.current_url
        }

    def validate_search_result_relevance_multiple_categories(self, product_name):
        """
        Validates search result relevance when a product exists in multiple categories.
        Searches for product and verifies relevance through position and related products.
        
        This workflow:
        1. Ensures search page is loaded
        2. Performs search for the product
        3. Validates search result relevance through page-level method
        4. Captures all product data for relevance analysis
        5. Calculates relevance score based on product position
        
        Args:
            product_name (str): Name of the product to search for and validate relevance
            
        Returns:
            dict: Observable outcome containing:
                - 'search_keyword': Product name searched
                - 'page_loaded': Boolean indicating page loaded successfully
                - 'search_executed': Boolean indicating search was submitted
                - 'results_displayed': Boolean indicating results are visible
                - 'product_found_in_results': Boolean indicating product appears in results
                - 'result_count': Total number of products in search results
                - 'matching_products': List of product names matching the search
                - 'all_product_names': List of all product names in results
                - 'all_product_prices': List of all product prices in results
                - 'relevance_data': Dict with product position, score, and category data
                - 'relevance_score': String indicating relevance (High/Medium/Low/Not Found)
                - 'validation_passed': Boolean indicating overall validation success
                - 'page_url': Current page URL after search
        """
        try:
            self.logger.info(f"Starting search result relevance validation for: {product_name}")
            
            # Ensure page is loaded
            page_loaded = self.search_page.is_page_loaded()
            if not page_loaded:
                self.logger.warning("Search page not fully loaded")
                return {
                    'search_keyword': product_name,
                    'page_loaded': False,
                    'search_executed': False,
                    'results_displayed': False,
                    'product_found_in_results': False,
                    'result_count': 0,
                    'matching_products': [],
                    'all_product_names': [],
                    'all_product_prices': [],
                    'relevance_data': {},
                    'relevance_score': 'Unknown',
                    'validation_passed': False,
                    'page_url': self.driver.current_url
                }
            
            # Execute search
            self.logger.debug(f"Searching for product: {product_name}")
            search_outcome = self.perform_product_search(product_name)
            
            if not search_outcome['search_successful']:
                self.logger.warning(f"Product search failed for: {product_name}")
                return {
                    'search_keyword': product_name,
                    'page_loaded': page_loaded,
                    'search_executed': False,
                    'results_displayed': False,
                    'product_found_in_results': False,
                    'result_count': 0,
                    'matching_products': [],
                    'all_product_names': [],
                    'all_product_prices': [],
                    'relevance_data': {},
                    'relevance_score': 'Unknown',
                    'validation_passed': False,
                    'page_url': self.driver.current_url
                }
            
            # Validate result relevance through page method
            self.logger.debug("Validating search result relevance")
            relevance_validation = self.search_page.validate_search_result_relevance_multiple_categories(product_name)
            
            # Extract relevance score from validation data
            relevance_score = relevance_validation.get('relevance_data', {}).get('relevance_score', 'Unknown')
            
            # Build comprehensive outcome
            outcome = {
                'search_keyword': product_name,
                'page_loaded': page_loaded,
                'search_executed': relevance_validation['search_executed'],
                'results_displayed': relevance_validation['results_displayed'],
                'product_found_in_results': relevance_validation['product_found_in_results'],
                'result_count': relevance_validation['result_count'],
                'matching_products': relevance_validation['matching_products'],
                'all_product_names': relevance_validation['all_product_names'],
                'all_product_prices': relevance_validation['all_product_prices'],
                'relevance_data': relevance_validation['relevance_data'],
                'relevance_score': relevance_score,
                'validation_passed': relevance_validation['validation_passed'],
                'page_url': self.driver.current_url
            }
            
            self.logger.info(f"Search relevance validation completed. Product found: {outcome['product_found_in_results']}, Relevance score: {relevance_score}")
            return outcome
            
        except Exception as e:
            self.logger.error(f"Error during search relevance validation: {str(e)}")
            return {
                'search_keyword': product_name,
                'page_loaded': False,
                'search_executed': False,
                'results_displayed': False,
                'product_found_in_results': False,
                'result_count': 0,
                'matching_products': [],
                'all_product_names': [],
                'all_product_prices': [],
                'relevance_data': {},
                'relevance_score': 'Unknown',
                'validation_passed': False,
                'page_url': self.driver.current_url
            }

    def validate_search_with_whitespace_only(self, whitespace_string=None):
        """
        Validates search behavior when the search term contains only whitespace characters.

        This method performs a search using a whitespace-only string (default three spaces)
        and returns an observable outcome describing how the application handled the input.

        Args:
            whitespace_string (str|None): Optional whitespace string to submit. If None, uses three spaces.

        Returns:
            dict: Observable outcome containing:
                - 'whitespace_string': The whitespace string submitted
                - 'trimmed_to_empty': Bool whether the app/page trimmed the input to empty
                - 'search_executed': Bool indicating whether the search was submitted
                - 'results_displayed': Bool indicating whether results container is visible
                - 'has_results': Bool indicating whether any product results were found
                - 'result_count': Integer count of results (0 if none or not visible)
                - 'no_results_message': Text of any no-results message (or None)
                - 'validation_passed': Bool indicating overall validation success (no crash and graceful handling)
                - 'page_url': Current page URL after search
        """
        try:
            self.logger.info("Validating search with whitespace-only input")
            ws = whitespace_string if whitespace_string is not None else '   '

            # Ensure search page ready
            page_loaded = self.search_page.is_page_loaded()
            if not page_loaded:
                self.logger.warning("Search page not loaded before whitespace test")
                return {
                    'whitespace_string': ws,
                    'trimmed_to_empty': False,
                    'search_executed': False,
                    'results_displayed': False,
                    'has_results': False,
                    'result_count': 0,
                    'no_results_message': None,
                    'validation_passed': False,
                    'page_url': self.driver.current_url
                }

            # Use existing flow to perform the search; perform_product_search is responsible for submission
            search_outcome = self.perform_product_search(ws)

            # If the flow reports failure to execute search, treat as not executed
            search_executed = bool(search_outcome.get('search_successful'))

            # Inspect page-level state for results and messages
            results_displayed = self.search_page.are_search_results_displayed()
            has_results = False
            result_count = 0
            no_results_message = None

            if results_displayed:
                # Use page helpers to collect results
                all_names = self.search_page.get_all_product_names() or []
                result_count = len(all_names)
                has_results = result_count > 0
                if not has_results:
                    no_results_message = self.search_page.get_no_results_message() if hasattr(self.search_page, 'get_no_results_message') else None
            else:
                # No results container visible; attempt to read any no-results messaging
                no_results_message = self.search_page.get_no_results_message() if hasattr(self.search_page, 'get_no_results_message') else None

            # Determine if the application trimmed whitespace to empty (heuristic: search_executed true but result_count==0)
            trimmed_to_empty = search_executed and (result_count == 0)

            validation_passed = True
            # Fail the validation only if search execution crashed or page not responsive
            if not search_executed and page_loaded:
                validation_passed = False

            outcome = {
                'whitespace_string': ws,
                'trimmed_to_empty': trimmed_to_empty,
                'search_executed': search_executed,
                'results_displayed': results_displayed,
                'has_results': has_results,
                'result_count': result_count,
                'no_results_message': no_results_message,
                'validation_passed': validation_passed,
                'page_url': self.driver.current_url
            }

            self.logger.info(f"Whitespace search validation completed: executed={search_executed}, results={result_count}")
            return outcome

        except Exception as e:
            self.logger.error(f"Error validating whitespace-only search: {str(e)}")
            return {
                'whitespace_string': whitespace_string if whitespace_string is not None else '   ',
                'trimmed_to_empty': False,
                'search_executed': False,
                'results_displayed': False,
                'has_results': False,
                'result_count': 0,
                'no_results_message': None,
                'validation_passed': False,
                'page_url': self.driver.current_url
            }

    def validate_search_with_repeated_characters(self, character='a', repetition_count=7):
        """
        Validates search behavior when the search term contains only repeated characters.

        This method performs a search using a string of repeated characters (default seven 'a's)
        and returns an observable outcome describing how the application handled the input.

        Args:
            character (str): Single character to repeat. Defaults to 'a'.
            repetition_count (int): Number of times to repeat the character. Defaults to 7.

        Returns:
            dict: Observable outcome containing:
                - 'repeated_string': The repeated character string submitted
                - 'search_executed': Bool indicating whether the search was submitted
                - 'results_displayed': Bool indicating whether results container is visible
                - 'has_results': Bool indicating whether any product results were found
                - 'result_count': Integer count of results returned
                - 'first_product_name': Name of first product if results exist, else None
                - 'no_results_message': Text of any no-results message (or None)
                - 'search_handled_gracefully': Bool indicating no crashes or errors
                - 'validation_passed': Bool indicating overall validation success
                - 'page_url': Current page URL after search
        """
        try:
            self.logger.info(f"Validating search with repeated characters: '{character}' x {repetition_count}")
            repeated_string = character * repetition_count

            # Ensure search page ready
            page_loaded = self.search_page.is_page_loaded()
            if not page_loaded:
                self.logger.warning("Search page not loaded before repeated character test")
                return {
                    'repeated_string': repeated_string,
                    'search_executed': False,
                    'results_displayed': False,
                    'has_results': False,
                    'result_count': 0,
                    'first_product_name': None,
                    'no_results_message': None,
                    'search_handled_gracefully': False,
                    'validation_passed': False,
                    'page_url': self.driver.current_url
                }

            # Execute search with repeated character string
            self.logger.debug(f"Performing search with repeated string: {repeated_string}")
            search_outcome = self.perform_product_search(repeated_string)

            # Check if search execution was successful
            search_executed = bool(search_outcome.get('search_successful'))

            # Inspect page-level state for results and messages
            results_displayed = self.search_page.are_search_results_displayed()
            has_results = False
            result_count = 0
            first_product_name = None
            no_results_message = None
            search_handled_gracefully = True

            if results_displayed:
                # Use page helpers to collect results
                all_names = self.search_page.get_all_product_names() or []
                result_count = len(all_names)
                has_results = result_count > 0
                if has_results:
                    first_product_name = all_names[0]
                else:
                    # No results; try to get the no-results message
                    no_results_message = self.search_page.get_no_results_message() if hasattr(self.search_page, 'get_no_results_message') else None
            else:
                # Results container not visible; attempt to read no-results message
                no_results_message = self.search_page.get_no_results_message() if hasattr(self.search_page, 'get_no_results_message') else None

            # Validation passes if search was submitted and handled without error
            validation_passed = search_executed and search_handled_gracefully

            outcome = {
                'repeated_string': repeated_string,
                'search_executed': search_executed,
                'results_displayed': results_displayed,
                'has_results': has_results,
                'result_count': result_count,
                'first_product_name': first_product_name,
                'no_results_message': no_results_message,
                'search_handled_gracefully': search_handled_gracefully,
                'validation_passed': validation_passed,
                'page_url': self.driver.current_url
            }

            self.logger.info(f"Repeated character search validation completed: executed={search_executed}, results={result_count}")
            return outcome

        except Exception as e:
            self.logger.error(f"Error validating repeated character search: {str(e)}")
            return {
                'repeated_string': character * repetition_count,
                'search_executed': False,
                'results_displayed': False,
                'has_results': False,
                'result_count': 0,
                'first_product_name': None,
                'no_results_message': None,
                'search_handled_gracefully': False,
                'validation_passed': False,
                'page_url': self.driver.current_url
            }

    def validate_search_when_backend_response_delayed(self, product_name, wait_timeout=15):
        """
        Validates search behavior when backend response is delayed.

        This method performs a search and monitors for delayed response, tracking:
        - Whether search submission was successful
        - Loading indicators or waiting states
        - Time waited for results to appear
        - Final results rendering and count

        Args:
            product_name (str): Product name to search for
            wait_timeout (int): Maximum seconds to wait for results. Defaults to 15.

        Returns:
            dict: Observable outcome containing:
                - 'search_keyword': Product name searched
                - 'search_executed': Bool indicating search was submitted
                - 'results_eventually_displayed': Bool indicating results loaded within timeout
                - 'result_count': Integer count of results that loaded
                - 'has_results': Bool indicating whether results contain products
                - 'first_product_name': Name of first product if results exist, else None
                - 'page_responsive': Bool indicating page remained responsive during wait
                - 'no_results_message': Text of any no-results message (or None)
                - 'response_delayed': Bool indicating whether results took time to load
                - 'validation_passed': Bool indicating overall validation success
                - 'page_url': Current page URL after search
        """
        import time
        try:
            self.logger.info(f"Validating search with delayed backend response for: {product_name}")
            start_time = time.time()

            # Ensure search page ready
            page_loaded = self.search_page.is_page_loaded()
            if not page_loaded:
                self.logger.warning("Search page not loaded before delayed response test")
                return {
                    'search_keyword': product_name,
                    'search_executed': False,
                    'results_eventually_displayed': False,
                    'result_count': 0,
                    'has_results': False,
                    'first_product_name': None,
                    'page_responsive': False,
                    'no_results_message': None,
                    'response_delayed': False,
                    'validation_passed': False,
                    'page_url': self.driver.current_url
                }

            # Submit search
            self.logger.debug(f"Submitting search for: {product_name}")
            search_outcome = self.perform_product_search(product_name)
            search_executed = bool(search_outcome.get('search_successful'))

            if not search_executed:
                self.logger.warning(f"Search submission failed for: {product_name}")
                return {
                    'search_keyword': product_name,
                    'search_executed': False,
                    'results_eventually_displayed': False,
                    'result_count': 0,
                    'has_results': False,
                    'first_product_name': None,
                    'page_responsive': True,
                    'no_results_message': None,
                    'response_delayed': False,
                    'validation_passed': False,
                    'page_url': self.driver.current_url
                }

            # Wait for results to display (perform_product_search may not wait long enough)
            self.logger.debug(f"Waiting for results to display (timeout: {wait_timeout}s)")
            results_displayed = False
            wait_start = time.time()

            # Poll for results with multiple checks
            while not results_displayed and (time.time() - wait_start) < wait_timeout:
                results_displayed = self.search_page.are_search_results_displayed()
                if not results_displayed:
                    time.sleep(0.5)  # Small delay before retry

            elapsed_time = time.time() - wait_start
            response_delayed = elapsed_time > 2.0  # Consider > 2 seconds as delayed

            # Collect result data
            result_count = 0
            has_results = False
            first_product_name = None
            no_results_message = None

            if results_displayed:
                self.logger.debug("Results displayed after waiting")
                all_names = self.search_page.get_all_product_names() or []
                result_count = len(all_names)
                has_results = result_count > 0
                if has_results:
                    first_product_name = all_names[0]
                else:
                    no_results_message = self.search_page.get_no_results_message() if hasattr(self.search_page, 'get_no_results_message') else None
            else:
                self.logger.warning(f"Results did not display within {wait_timeout}s timeout")
                no_results_message = self.search_page.get_no_results_message() if hasattr(self.search_page, 'get_no_results_message') else None

            # Assume page remained responsive if we reached here
            page_responsive = True

            validation_passed = search_executed and results_displayed

            outcome = {
                'search_keyword': product_name,
                'search_executed': search_executed,
                'results_eventually_displayed': results_displayed,
                'result_count': result_count,
                'has_results': has_results,
                'first_product_name': first_product_name,
                'page_responsive': page_responsive,
                'no_results_message': no_results_message,
                'response_delayed': response_delayed,
                'validation_passed': validation_passed,
                'page_url': self.driver.current_url
            }

            self.logger.info(f"Delayed response validation completed: executed={search_executed}, displayed={results_displayed}, elapsed={elapsed_time:.2f}s, delayed={response_delayed}")
            return outcome

        except Exception as e:
            self.logger.error(f"Error validating delayed backend response: {str(e)}")
            return {
                'search_keyword': product_name,
                'search_executed': False,
                'results_eventually_displayed': False,
                'result_count': 0,
                'has_results': False,
                'first_product_name': None,
                'page_responsive': False,
                'no_results_message': None,
                'response_delayed': False,
                'validation_passed': False,
                'page_url': self.driver.current_url
            }