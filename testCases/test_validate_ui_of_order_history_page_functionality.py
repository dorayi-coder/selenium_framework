import pytest
from flows.orderHistoryFlow import OrderHistoryFlow


@pytest.mark.ui
@pytest.mark.regression
class TestValidateUIOfOrderHistoryPageFunctionality:
    """
    Test suite for validating Order History page UI functionality.
    
    Tests the visual elements and layout of the Order History page
    to ensure proper rendering and accessibility.
    """

    def test_validate_ui_of_order_history_page_functionality(self, driver, authenticated_user):
        """
        Test: Validate UI of Order History page functionality.
        
        Verifies that:
        - Order History page loads successfully
        - UI elements are visible and properly rendered
        - Page displays either order table or no-orders message
        - Pagination appears when applicable
        
        Args:
            driver: Selenium WebDriver fixture
            authenticated_user: Authenticated user fixture for accessing Order History
        
        Asserts:
            - Page loads successfully
            - UI elements are visible
            - Test result indicates UI is valid
        """
        # Arrange
        order_history_flow = OrderHistoryFlow(driver)
        
        # Act
        result = order_history_flow.validate_ui_of_order_history_page_functionality()
        
        # Assert
        assert result is not None, "UI validation result should not be None"
        assert result.get('test_passed') is True, \
            f"Order History UI validation failed: {result.get('test_failure_reason')}"
        assert result.get('page_loaded') is True, \
            "Order History page should load successfully"
        assert result.get('ui_valid') is True, \
            "Order History UI elements should be valid"
        assert result.get('page_title') is not None, \
            "Page title should be available"
        assert result.get('order_table_visible') or \
               'ui_valid' in result and result['ui_valid'], \
            "Order History should display either order table or valid empty state"
