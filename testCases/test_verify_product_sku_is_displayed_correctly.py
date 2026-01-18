import pytest
from flows.productDisplayFlow import ProductDisplayFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyProductSkuIsDisplayedCorrectly:
    """
    Test suite for verifying product SKU display on Product Display page.
    
    Tests that the product SKU is displayed correctly with proper visibility
    and non-empty content.
    """

    def test_verify_product_sku_is_displayed_correctly(self, driver, product_page):
        """
        Test: Verify product SKU is displayed correctly.
        
        Verifies that:
        - Product page loads successfully
        - Product SKU is visible on the page
        - Product SKU is not empty
        - Product SKU text is properly rendered
        
        Args:
            driver: Selenium WebDriver fixture
            product_page: Fixture providing product page context
        
        Asserts:
            - Test result is not None
            - Test passes successfully
            - Product SKU is available and not None
            - Product SKU is visible
            - Product SKU is not empty
            - Test failure reason is None when SKU displays correctly
        """
        # Arrange
        product_display_flow = ProductDisplayFlow(driver)
        
        # Act
        result = product_display_flow.verify_product_sku_is_displayed_correctly()
        
        # Assert
        assert result is not None, "Product SKU validation result should not be None"
        assert result.get('test_passed') is True, \
            f"Product SKU validation failed: {result.get('test_failure_reason')}"
        assert result.get('product_sku') is not None, \
            "Product SKU should be available"
        assert result.get('sku_visible') is True, \
            "Product SKU should be visible on the page"
        assert result.get('sku_not_empty') is True, \
            "Product SKU should not be empty"
        assert result.get('test_failure_reason') is None, \
            "Test failure reason should be None when product SKU displays correctly"
