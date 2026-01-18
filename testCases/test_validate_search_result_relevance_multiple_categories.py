import pytest
from flows.searchFlow import SearchFlow


@pytest.mark.ui
@pytest.mark.regression
class TestValidateSearchResultRelevanceMultipleCategories:
    """Test: Validate search result relevance when product exists in multiple categories."""
    
    def test_validate_search_result_relevance_multiple_categories(self, driver, search_results_page_with_products):
        """
        Validate that search results display relevant products when a product exists in multiple categories.
        
        This test verifies:
        1. Search page loads successfully
        2. Search is executed for the product
        3. Results are displayed on the page
        4. Product is found in search results
        5. Relevance data is calculated and available
        6. Relevance score is determined (High/Medium/Low/Not Found)
        7. All product data is captured (names, prices)
        8. Validation passes with correct relevance assessment
        
        Args:
            driver: Selenium WebDriver fixture
            search_results_page_with_products: Fixture providing search context with products
        """
        # Arrange
        search_flow = SearchFlow(driver)
        product_name = "laptop"
        
        # Act
        result = search_flow.validate_search_result_relevance_multiple_categories(product_name)
        
        # Assert
        assert result is not None
        assert result.get('validation_passed') is True
        assert result.get('page_loaded') is True
        assert result.get('search_executed') is True
        assert result.get('results_displayed') is True
        assert result.get('search_keyword') is not None
        assert result.get('search_keyword') == product_name
        assert result.get('product_found_in_results') is True
        assert result.get('result_count') > 0
        assert result.get('matching_products') is not None
        assert len(result.get('matching_products', [])) > 0
        assert result.get('all_product_names') is not None
        assert len(result.get('all_product_names', [])) > 0
        assert result.get('all_product_prices') is not None
        assert result.get('relevance_data') is not None
        assert result.get('relevance_score') is not None
        assert result.get('relevance_score') in ['High', 'Medium', 'Low', 'Not Found']
        assert result.get('page_url') is not None
