import pytest
from flows.productDisplayFlow import ProductDisplayFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyProductPageDoesNotDisplayStaleOrCachedData:
    """Test: Verify product page does not display stale or cached data."""
    
    def test_verify_product_page_does_not_display_stale_or_cached_data(self, driver, product_page):
        """
        Verify that the product page displays fresh data and not stale or cached information.
        
        This test validates that:
        - Product name is available and current
        - Product price is available and current
        - Page shows fresh data, not stale/cached
        - Last modified timestamp does not indicate cached data
        - Data is current and not outdated
        - All freshness conditions are met
        
        Args:
            driver: Selenium WebDriver instance from pytest fixture
            product_page: Product page context fixture
        
        Assert:
            - result dictionary is not None
            - test_passed is True
            - product_name is not None
            - product_price is not None
            - page_fresh is True
            - data_current is True
            - test_failure_reason is None
        """
        # Arrange
        product_display_flow = ProductDisplayFlow(driver)
        
        # Act
        result = product_display_flow.verify_product_page_does_not_display_stale_or_cached_data()
        
        # Assert
        assert result is not None
        assert result.get('test_passed') is True
        assert result.get('product_name') is not None
        assert result.get('product_price') is not None
        assert result.get('page_fresh') is True
        assert result.get('data_current') is True
        assert result.get('test_failure_reason') is None
