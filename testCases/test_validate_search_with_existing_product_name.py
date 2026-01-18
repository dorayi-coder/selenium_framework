import pytest
from flows.searchFlow import SearchFlow


@pytest.mark.ui
@pytest.mark.regression
class TestValidateSearchWithExistingProductName:
    """Test: Validate search with existing product name."""
    
    def test_validate_search_with_existing_product_name(self, driver, search_results_page_with_products):
        """
        Validate that searching for an existing product name returns relevant results.
        
        This test validates that:
        - Search is successfully executed for the product
        - Search results are displayed on the page
        - At least one product is found matching the search
        - The searched product appears in the results
        - Result count is greater than zero
        - First product is retrievable from results
        - All products list is populated
        - Overall validation passes
        
        Args:
            driver: Selenium WebDriver instance from pytest fixture
            search_results_page_with_products: Search context with products fixture
        
        Assert:
            - result dictionary is not None
            - validation_passed is True
            - search_successful is True
            - results_displayed is True
            - result_count is greater than 0
            - searched_product_found is True
            - product_name is not None
            - first_product is not None
            - all_products is not empty
        """
        # Arrange
        search_flow = SearchFlow(driver)
        product_name = "laptop"  # Using a common product name that should exist
        
        # Act
        result = search_flow.validate_search_with_existing_product_name(product_name)
        
        # Assert
        assert result is not None
        assert result.get('validation_passed') is True
        assert result.get('search_successful') is True
        assert result.get('results_displayed') is True
        assert result.get('result_count') > 0
        assert result.get('searched_product_found') is True
        assert result.get('product_name') is not None
        assert result.get('first_product') is not None
        assert result.get('all_products') is not None
        assert len(result.get('all_products', [])) > 0
