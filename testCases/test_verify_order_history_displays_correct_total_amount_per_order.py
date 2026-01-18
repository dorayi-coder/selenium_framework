import pytest
from flows.orderHistoryFlow import OrderHistoryFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyOrderHistoryDisplaysCorrectTotalAmountPerOrder:
    """
    Test suite for verifying Order History displays correct total amounts.
    
    Tests that order totals are displayed correctly and accurately for each order
    in the Order History page.
    """

    def test_verify_order_history_displays_correct_total_amount_per_order(self, driver, authenticated_user):
        """
        Test: Verify Order History displays correct total amount per order.
        
        Verifies that:
        - Order History page loads successfully
        - Each order displays a valid total amount
        - Order totals are properly formatted and accessible
        - Empty order state is handled correctly when no orders exist
        
        Args:
            driver: Selenium WebDriver fixture
            authenticated_user: Authenticated user fixture for accessing Order History
        
        Asserts:
            - Test result is not None
            - Test passes successfully
            - Order totals are valid and properly displayed
            - Orders count and totals count are consistent
        """
        # Arrange
        order_history_flow = OrderHistoryFlow(driver)
        
        # Act
        result = order_history_flow.verify_order_history_displays_correct_total_amount_per_order()
        
        # Assert
        assert result is not None, "Total amount validation result should not be None"
        assert result.get('test_passed') is True, \
            f"Order History total amount validation failed: {result.get('test_failure_reason')}"
        assert result.get('orders_count') is not None, \
            "Orders count should be available in result"
        assert result.get('totals_count') is not None, \
            "Totals count should be available in result"
        assert result.get('totals_valid') is True, \
            "Order totals should be valid"
        assert result.get('orders_count') == result.get('totals_count') or \
               result.get('orders_count') == 0, \
            "Total amount count should match orders count or be zero for empty state"
