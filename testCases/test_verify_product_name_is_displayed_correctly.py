import pytest
from flows.productDisplayFlow import ProductDisplayFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyProductNameIsDisplayedCorrectly:
    """
    Test suite for verifying product name display on Product Display page.
    
    Tests that the product name is displayed correctly with proper visibility
    and non-empty content.
    """

    def test_verify_product_name_is_displayed_correctly(self, driver, product_page):
        """
        Test: Verify product name is displayed correctly.
        
        Verifies that:
        - Product page loads successfully
        - Product name is visible on the page
        - Product name is not empty
        - Product name text is properly rendered
        
        Args:
            driver: Selenium WebDriver fixture
            product_page: Fixture providing product page context
        
        Asserts:
            - Test result is not None
            - Test passes successfully
            - Product name is available and not None
            - Product name is visible
            - Product name is not empty
            - Test failure reason is None when name displays correctly
        """
        # Arrange
        product_display_flow = ProductDisplayFlow(driver)
        
        # Act
        result = product_display_flow.verify_product_name_is_displayed_correctly()
        
        # Assert
        assert result is not None, "Product name validation result should not be None"
        assert result.get('test_passed') is True, \
            f"Product name validation failed: {result.get('test_failure_reason')}"
        assert result.get('product_name') is not None, \
            "Product name should be available"
        assert result.get('name_visible') is True, \
            "Product name should be visible on the page"
        assert result.get('name_not_empty') is True, \
            "Product name should not be empty"
        assert result.get('test_failure_reason') is None, \
            "Test failure reason should be None when product name displays correctly"
