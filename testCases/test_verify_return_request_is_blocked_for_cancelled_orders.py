import pytest
from flows.productReturnsFlow import ProductReturnsFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyReturnRequestIsBlockedForCancelledOrders:
    """Test: Verify return request is blocked for cancelled orders."""
    
    def test_verify_return_request_is_blocked_for_cancelled_orders(self, driver, returns_page):
        """
        Verify that return requests are blocked/disabled for cancelled orders.
        
        This test validates that:
        - Returns page loads successfully
        - Cancelled orders are detected if they exist
        - Return button is disabled for cancelled orders
        - Block message is displayed to indicate why returns are blocked
        - System prevents return requests on cancelled orders
        - Appropriate messaging informs users about the restriction
        
        Args:
            driver: Selenium WebDriver instance from pytest fixture
            returns_page: Returns page context fixture
        
        Assert:
            - result dictionary is not None
            - test_passed is True
            - return_blocked is True
            - block_message_shown is True
            - test_failure_reason is None
        """
        # Arrange
        product_returns_flow = ProductReturnsFlow(driver)
        
        # Act
        result = product_returns_flow.verify_return_request_is_blocked_for_cancelled_orders()
        
        # Assert
        assert result is not None
        assert result.get('test_passed') is True
        assert result.get('return_blocked') is True
        assert result.get('block_message_shown') is True
        assert result.get('test_failure_reason') is None
