import pytest
from flows.productDisplayFlow import ProductDisplayFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyProductCategoryAndBreadcrumbAreCorrect:
    """
    Test suite for verifying product category and breadcrumb navigation.
    
    Tests that the product category is correctly displayed and reflected
    in the breadcrumb navigation path on the product page.
    """

    def test_verify_product_category_and_breadcrumb_are_correct(self, driver, product_page):
        """
        Test: Verify product category and breadcrumb are correct.
        
        Verifies that:
        - Product page loads successfully
        - Product category is available
        - Breadcrumb navigation is visible
        - Breadcrumb path is correctly set
        - Product category matches the breadcrumb hierarchy
        
        Args:
            driver: Selenium WebDriver fixture
            product_page: Fixture providing product page context
        
        Asserts:
            - Test result is not None
            - Test passes successfully
            - Product category is available
            - Breadcrumb is visible
            - Breadcrumb path is available
            - Category is present in breadcrumb path
            - Test failure reason is None when category and breadcrumb are correct
        """
        # Arrange
        product_display_flow = ProductDisplayFlow(driver)
        
        # Act
        result = product_display_flow.verify_product_category_and_breadcrumb_are_correct()
        
        # Assert
        assert result is not None, "Product category and breadcrumb validation result should not be None"
        assert result.get('test_passed') is True, \
            f"Product category and breadcrumb validation failed: {result.get('test_failure_reason')}"
        assert result.get('product_category') is not None, \
            "Product category should be available"
        assert result.get('breadcrumb_visible') is True, \
            "Breadcrumb navigation should be visible"
        assert result.get('breadcrumb_path') is not None, \
            "Breadcrumb path should be available"
        assert result.get('category_in_breadcrumb') is True, \
            "Product category should be present in breadcrumb path"
        assert result.get('test_failure_reason') is None, \
            "Test failure reason should be None when category and breadcrumb are correct"
