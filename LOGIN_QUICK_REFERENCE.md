# User Login - Quick Reference Guide

## 📋 Business Flow (What gets executed)

```
LoginFlow.login_user(email, password)
├─ Step 1: Click "LOG IN" link on home page
├─ Step 2: Wait for login page to load
├─ Step 3: Enter email address
├─ Step 4: Enter password
└─ Step 5: Click login button
```

## 🎯 Page Object Methods (LoginPage - Atomic Actions)

### Page State
```python
login_page.is_page_loaded()  # Returns: bool
```

### Input Actions
```python
login_page.enter_email("user@example.com")
login_page.enter_password("password123")
login_page.clear_email()
login_page.clear_password()
login_page.submit_login_form()  # Clicks login button
```

### Checkbox Control
```python
login_page.check_remember_me()      # Check if not already checked
login_page.uncheck_remember_me()    # Uncheck if currently checked
login_page.is_remember_me_checked() # Returns: bool
```

### Navigation
```python
login_page.click_forgot_password()  # Navigate to password reset
```

### Observable Outcomes (Error/Success State)
```python
login_page.get_error_message()              # Returns: str or None
login_page.get_email_error()                # Returns: str or None
login_page.get_password_error()             # Returns: str or None
login_page.get_all_validation_errors()      # Returns: dict
login_page.is_any_validation_error_displayed()  # Returns: bool
login_page.is_any_error_displayed()         # Returns: bool
login_page.is_logout_link_visible()         # Returns: bool (success indicator)
```

## 🚀 Flow Methods (LoginFlow - Business Workflows)

### Core Login Variants
```python
# Standard login (clicks link from home page)
flow.login_user(email, password)

# Login with "Remember me" enabled
flow.login_user_with_remember_me(email, password)

# Login with "Remember me" disabled
flow.login_user_without_remember_me(email, password)

# Login when already on login page (no link click)
flow.login_from_login_page(email, password)
```

### Page Loading
```python
flow.wait_for_login_page_to_load()  # Raises Exception if page fails to load
```

### Observable Outcomes (Test Assertions)
```python
error = flow.get_login_error_message()  # Returns: str or None
errors = flow.get_validation_errors()   # Returns: dict {field: error}
has_errors = flow.is_any_error_displayed()  # Returns: bool
flow.initiate_password_reset()          # Navigate to password reset
```

## 💻 Pytest Integration Example

```python
import pytest
from flows.loginFlow import LoginFlow

class TestUserLogin:
    
    def test_successful_login(self, driver):
        """Test successful login with valid credentials"""
        login_flow = LoginFlow(driver)
        
        # Execute login workflow
        login_flow.login_user("testuser@nopcommerce.com", "validpassword")
        
        # Verify success via observable outcomes
        assert not login_flow.is_any_error_displayed(), "Unexpected error displayed"
        assert login_flow.login_page.is_logout_link_visible(), "Not logged in"
    
    def test_invalid_credentials_error(self, driver):
        """Test login failure with invalid credentials"""
        login_flow = LoginFlow(driver)
        
        login_flow.login_user("testuser@nopcommerce.com", "wrongpassword")
        
        # Verify error state
        error = login_flow.get_login_error_message()
        assert error is not None, "Expected error message"
        assert "invalid" in error.lower(), f"Unexpected error: {error}"
    
    def test_missing_email_validation(self, driver):
        """Test validation error for missing email"""
        login_flow = LoginFlow(driver)
        
        login_flow.login_page.click_login_link()
        login_flow.wait_for_login_page_to_load()
        login_flow.login_page.enter_password("somepassword")
        login_flow.login_page.submit_login_form()
        
        # Check for email validation error
        errors = login_flow.get_validation_errors()
        assert "email" in errors, "Expected email validation error"
    
    def test_remember_me_option(self, driver):
        """Test login with remember me option"""
        login_flow = LoginFlow(driver)
        
        login_flow.login_user_with_remember_me("user@example.com", "password")
        
        # Verify checkbox was checked before submission
        # (In real test, you'd check cookie after page reload)
        assert not login_flow.is_any_error_displayed()
    
    def test_password_reset_navigation(self, driver):
        """Test forgot password link navigation"""
        login_flow = LoginFlow(driver)
        
        login_flow.wait_for_login_page_to_load()
        login_flow.initiate_password_reset()
        
        # Test layer verifies page transition (not flow responsibility)
        # Example: assert "reset" in driver.current_url.lower()
```

## 🔍 Element Locators (Cross-Browser Safe)

| Element | Strategy | Selector |
|---------|----------|----------|
| Email Input | ID | "Email" |
| Password Input | ID | "Password" |
| Login Button | XPath | "//button[contains(text(), 'Log in')]" |
| Remember Me | ID | "RememberMe" |
| Forgot Password Link | XPath | "//a[contains(text(), 'Forgot password?')]" |
| Error Message | Class | "error" |
| Validation Error | Class | "field-validation-error" |
| Page Title | XPath | "//h1[text()='Welcome, Please Sign In!']" |
| Logout Link (Success Indicator) | XPath | "//a[contains(@href, '/logout')]" |

## 📚 Architecture Principles

### ✅ What Pages DO
- Define stable, cross-browser locators
- Perform atomic UI actions (click, type, read text)
- Check element visibility/presence
- Return observable UI state (text, visibility, error messages)

### ✅ What Flows DO
- Orchestrate business workflows using page methods
- Accept input parameters (email, password, etc.)
- Return observable outcomes for test verification
- Handle page loading and navigation

### ❌ What Pages DON'T DO
- Make business decisions
- Contain assertions
- Mix multiple actions in one method
- Hardcode test data
- Include browser selection logic

### ❌ What Flows DON'T DO
- Contain raw element locators
- Perform assertions
- Include browser-specific logic
- Verify expected outcomes

## 🛠️ Locator Update Strategy

If login page HTML changes, update locators in `pages/loginPage.py` only:

```python
# Old locator fails? Update just this line:
_email_input = (By.ID, "Email")  # Change the selector here

# No changes needed in flows - they use page methods only
# Tests continue to work - they use flow methods only
```

## 📌 Important Notes

1. **No Assertions in Code** - Tests add assertions when calling flows
2. **No Hardcoded Data** - Pass email/password as parameters
3. **No Browser Logic** - Pages work with any Selenium WebDriver
4. **Reusable** - Use same flow methods across multiple test scenarios
5. **Observable Outcomes** - Flows return state; tests verify state

## 🔗 File Locations

- **Page Object**: [pages/loginPage.py](pages/loginPage.py)
- **Business Flow**: [flows/loginFlow.py](flows/loginFlow.py)
- **Base Utilities**: [utilities/basePage.py](utilities/basePage.py)
- **Home Page** (for login link): [pages/homePage.py](pages/homePage.py)

---

**Last Updated**: January 13, 2026  
**Status**: Production-Ready ✅
