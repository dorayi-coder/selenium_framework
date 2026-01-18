import pytest
from flows.productCompareFlow import ProductCompareFlow


@pytest.mark.ui
@pytest.mark.regression
class TestValidateAddingProductForComparisonFromSearchResultsListView:
    """
    Test suite for validating product addition to comparison from Search Results.
    
    Tests that products can be successfully added to the comparison list
    from the search results list view page.
    """

    def test_validate_adding_product_for_comparison_from_search_results_list_view(self, driver, search_results_page_with_products):
        """
        Test: Validate adding product for comparison from List View of Search Results page.
        
        Verifies that:
        - Products can be added to comparison from search results list view
        - Success message is displayed after adding product
        - Product count increases after adding product
        - Product appears in the comparison list
        
        Args:
            driver: Selenium WebDriver fixture
            search_results_page_with_products: Fixture providing search results page with available products
        
        Asserts:
            - Test result is not None
            - Test passes successfully
            - Product count is at least 1
            - Success message is visible
            - Test failure reason is None when test passes
        """
        # Arrange
        product_compare_flow = ProductCompareFlow(driver)
        
        # Act
        result = product_compare_flow.validate_adding_product_for_comparison_from_search_results_list_view()
        
        # Assert
        assert result is not None, "Product comparison validation result should not be None"
        assert result.get('test_passed') is True, \
            f"Product comparison validation failed: {result.get('test_failure_reason')}"
        assert result.get('product_count') is not None, \
            "Product count should be available in result"
        assert result.get('product_count') >= 1, \
            "Product count should be at least 1 after adding product"
        assert result.get('success_message_visible') is True, \
            "Success message should be visible after adding product to comparison"
        assert result.get('test_failure_reason') is None, \
            "Test failure reason should be None when product is successfully added"
