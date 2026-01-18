import pytest
from flows.productDisplayFlow import ProductDisplayFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyProductPageRemainsAccessibleForHistoricalOrders:
    """Test: Verify product page remains accessible for historical orders."""
    
    def test_verify_product_page_remains_accessible_for_historical_orders(self, driver, product_page):
        """
        Verify that the product page remains accessible when viewing products from historical orders.
        
        This test validates that:
        - Product page loads successfully
        - Product name is available and can be retrieved
        - No access errors are displayed
        - Product data is available for historical products
        - Page remains accessible even for older/historical orders
        - All access conditions are met without restrictions
        
        Args:
            driver: Selenium WebDriver instance from pytest fixture
            product_page: Product page context fixture
        
        Assert:
            - result dictionary is not None
            - test_passed is True
            - product_name is not None
            - page_accessible is True
            - has_access_error is False
            - product_data_available is True
            - test_failure_reason is None
        """
        # Arrange
        product_display_flow = ProductDisplayFlow(driver)
        
        # Act
        result = product_display_flow.verify_product_page_remains_accessible_for_historical_orders()
        
        # Assert
        assert result is not None
        assert result.get('test_passed') is True
        assert result.get('product_name') is not None
        assert result.get('page_accessible') is True
        assert result.get('has_access_error') is False
        assert result.get('product_data_available') is True
        assert result.get('test_failure_reason') is None
