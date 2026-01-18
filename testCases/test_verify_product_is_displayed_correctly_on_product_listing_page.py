import pytest
from flows.productDisplayFlow import ProductDisplayFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyProductIsDisplayedCorrectlyOnProductListingPage:
    """
    Test suite for verifying product display on Product Listing page.
    
    Tests that product information is displayed correctly with all essential
    elements visible on the product listing page.
    """

    def test_verify_product_is_displayed_correctly_on_product_listing_page(self, driver, product_listing_page):
        """
        Test: Verify product is displayed correctly on Product Listing page.
        
        Verifies that:
        - Product page loads successfully
        - Product name is displayed
        - Product price is displayed
        - Product image is visible
        - All product elements are properly visible and accessible
        
        Args:
            driver: Selenium WebDriver fixture
            product_listing_page: Fixture providing product listing page context
        
        Asserts:
            - Test result is not None
            - Test passes successfully
            - Product name is available
            - Product is visible
            - Product image is visible
            - Product price is available
            - All elements are visible together
            - Test failure reason is None when product displays correctly
        """
        # Arrange
        product_display_flow = ProductDisplayFlow(driver)
        
        # Act
        result = product_display_flow.verify_product_is_displayed_correctly_on_product_listing_page()
        
        # Assert
        assert result is not None, "Product display validation result should not be None"
        assert result.get('test_passed') is True, \
            f"Product display validation failed: {result.get('test_failure_reason')}"
        assert result.get('product_name') is not None, \
            "Product name should be available"
        assert result.get('product_visible') is True, \
            "Product should be visible on listing page"
        assert result.get('product_image_visible') is True, \
            "Product image should be visible"
        assert result.get('product_price') is not None, \
            "Product price should be available"
        assert result.get('test_failure_reason') is None, \
            "Test failure reason should be None when all product elements are visible"
