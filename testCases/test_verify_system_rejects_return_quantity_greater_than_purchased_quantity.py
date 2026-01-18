import pytest
from flows.productReturnsFlow import ProductReturnsFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifySystemRejectsReturnQuantityGreaterThanPurchasedQuantity:
    """Test: Verify system rejects return quantity greater than purchased quantity."""
    
    def test_verify_system_rejects_return_quantity_greater_than_purchased_quantity(self, driver, return_request_page):
        """
        Verify that the system rejects return quantity when it exceeds purchased quantity.
        
        This test validates that:
        - Return request page loads successfully
        - Purchased quantity can be retrieved
        - Invalid quantity (greater than purchased) is detected
        - Error is displayed when quantity exceeds purchased amount
        - System properly rejects the invalid quantity
        - Validation prevents over-returns
        
        Args:
            driver: Selenium WebDriver instance from pytest fixture
            return_request_page: Return request page context fixture
        
        Assert:
            - result dictionary is not None
            - test_passed is True
            - purchased_quantity is not None
            - entered_quantity is not None
            - error_displayed is True
            - quantity_rejected is True
            - test_failure_reason is None
        """
        # Arrange
        product_returns_flow = ProductReturnsFlow(driver)
        
        # Act
        result = product_returns_flow.verify_system_rejects_return_quantity_greater_than_purchased_quantity()
        
        # Assert
        assert result is not None
        assert result.get('test_passed') is True
        assert result.get('purchased_quantity') is not None
        assert result.get('entered_quantity') is not None
        assert result.get('error_displayed') is True
        assert result.get('quantity_rejected') is True
        assert result.get('test_failure_reason') is None
