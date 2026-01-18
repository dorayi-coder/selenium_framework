import pytest
from flows.orderHistoryFlow import OrderHistoryFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyOrderHistoryPaginationWorksCorrectlyWhenManyOrdersExist:
    """
    Test suite for verifying Order History pagination functionality.
    
    Tests that pagination controls function properly when multiple pages
    of orders exist in the Order History page.
    """

    def test_verify_order_history_pagination_works_correctly_when_many_orders_exist(self, driver, authenticated_user):
        """
        Test: Verify Order History pagination works correctly when many orders exist.
        
        Verifies that:
        - Order History page loads successfully
        - Pagination controls are visible when applicable
        - Navigation between pages works correctly
        - Next and previous page buttons function as expected
        - Single page scenario is handled gracefully
        
        Args:
            driver: Selenium WebDriver fixture
            authenticated_user: Authenticated user fixture for accessing Order History
        
        Asserts:
            - Test result is not None
            - Test passes successfully
            - Pagination visibility matches expected state
            - Pagination controls work correctly (if visible)
            - Test failure reason is None when test passes
        """
        # Arrange
        order_history_flow = OrderHistoryFlow(driver)
        
        # Act
        result = order_history_flow.verify_order_history_pagination_works_correctly_when_many_orders_exist()
        
        # Assert
        assert result is not None, "Pagination validation result should not be None"
        assert result.get('test_passed') is True, \
            f"Order History pagination validation failed: {result.get('test_failure_reason')}"
        assert result.get('pagination_visible') is not None, \
            "Pagination visibility status should be available"
        assert result.get('pagination_works') is not None, \
            "Pagination functionality status should be available"
        
        # If pagination is visible, verify navigation works
        if result.get('pagination_visible'):
            assert result.get('pagination_works') is True, \
                "Pagination controls should work when visible"
        
        assert result.get('test_failure_reason') is None, \
            "Test failure reason should be None when test passes"
