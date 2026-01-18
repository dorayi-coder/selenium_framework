import pytest
from flows.productCompareFlow import ProductCompareFlow


@pytest.mark.ui
@pytest.mark.regression
class TestValidateProductComparePageWhenNoProductsAreAddedForComparison:
    """
    Test suite for validating Product Compare page empty state.
    
    Tests that the Product Compare page displays the correct empty state
    when no products are added for comparison.
    """

    def test_validate_product_compare_page_when_no_products_are_added_for_comparison(self, driver):
        """
        Test: Validate Product Compare page when no products are added for comparison.
        
        Verifies that:
        - Product Compare page loads successfully
        - No products message is displayed when comparison is empty
        - Comparison table is not visible when empty
        - Empty state is displayed correctly
        - Page shows appropriate message to user
        
        Args:
            driver: Selenium WebDriver fixture
        
        Asserts:
            - Test result is not None
            - Test passes successfully
            - No products message is displayed
            - Comparison table is not visible
            - Test failure reason is None when test passes
        """
        # Arrange
        product_compare_flow = ProductCompareFlow(driver)
        
        # Act
        result = product_compare_flow.validate_product_compare_page_when_no_products_are_added_for_comparison()
        
        # Assert
        assert result is not None, "Product Compare page validation result should not be None"
        assert result.get('test_passed') is True, \
            f"Product Compare page validation failed: {result.get('test_failure_reason')}"
        assert result.get('no_products_message_displayed') is True, \
            "No products message should be displayed when comparison is empty"
        assert result.get('comparison_table_visible') is False, \
            "Comparison table should not be visible when empty"
        assert result.get('test_failure_reason') is None, \
            "Test failure reason should be None when empty state is correctly displayed"
