import pytest
from flows.recurringPaymentsFlow import RecurringPaymentsFlow


@pytest.mark.ui
@pytest.mark.regression
class TestVerifyRecurringPaymentsPageIsAccessibleOnlyToAuthenticatedUsers:
    """Test: Verify Recurring Payments page is accessible only to authenticated users."""
    
    def test_verify_recurring_payments_page_is_accessible_only_to_authenticated_users(self, driver, authenticated_user):
        """
        Verify that the Recurring Payments page is accessible only to authenticated/logged-in users.
        
        This test validates that:
        - Recurring Payments page loads successfully
        - User must be authenticated to access the page
        - Access control is properly enforced
        - Authenticated users can access the page
        - Page access restrictions are in place for non-authenticated users
        - Either login requirement or authentication state is verified
        
        Args:
            driver: Selenium WebDriver instance from pytest fixture
            authenticated_user: Authenticated user context fixture
        
        Assert:
            - result dictionary is not None
            - test_passed is True
            - is_user_authenticated is True
            - test_failure_reason is None
        """
        # Arrange
        recurring_payments_flow = RecurringPaymentsFlow(driver)
        
        # Act
        result = recurring_payments_flow.verify_recurring_payments_page_is_accessible_only_to_authenticated_users()
        
        # Assert
        assert result is not None
        assert result.get('test_passed') is True
        assert result.get('is_user_authenticated') is True
        assert result.get('test_failure_reason') is None
