import pytest
from flows.searchFlow import SearchFlow


@pytest.mark.ui
@pytest.mark.regression
class TestValidateSearchWhenBackendResponseDelayed:
    """Test: Validate search behavior when backend response is delayed."""
    
    def test_validate_search_when_backend_response_delayed(self, driver, search_results_page_with_products):
        """
        Validate search behavior when backend response is delayed.
        
        This test verifies:
        1. Search page loads and is ready
        2. Search is submitted for the product
        3. Application waits for results to display
        4. Results eventually display within timeout period
        5. Response delay is tracked (whether > 2 seconds)
        6. Page remains responsive during wait
        7. Product results or no-results message is captured
        8. First product name is available if results exist
        9. Overall validation passes
        10. All timing and response data is collected
        
        Args:
            driver: Selenium WebDriver fixture
            search_results_page_with_products: Fixture providing search context with products
        """
        # Arrange
        search_flow = SearchFlow(driver)
        product_name = "laptop"
        wait_timeout = 15
        
        # Act
        result = search_flow.validate_search_when_backend_response_delayed(product_name, wait_timeout)
        
        # Assert
        assert result is not None
        assert result.get('validation_passed') is True
        assert result.get('search_keyword') is not None
        assert result.get('search_keyword') == product_name
        assert result.get('search_executed') is True
        assert result.get('results_eventually_displayed') is True
        assert result.get('page_responsive') is True
        assert result.get('response_delayed') in [True, False]
        assert isinstance(result.get('result_count'), int)
        assert result.get('result_count') >= 0
        assert result.get('has_results') in [True, False]
        assert result.get('first_product_name') is None or isinstance(result.get('first_product_name'), str)
        assert result.get('no_results_message') is None or isinstance(result.get('no_results_message'), str)
        assert result.get('page_url') is not None
