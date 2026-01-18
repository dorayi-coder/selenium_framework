"""
Newsletter Feature Test Data
Provides all constants and test data for Newsletter feature testing
"""


class NewsletterTestData:
    """Newsletter test data constants"""

    # Valid Email Test Data
    VALID_EMAIL_FOR_SUBSCRIPTION = "user@example.com"
    VALID_EMAIL_SECONDARY = "subscriber@example.com"
    VALID_EMAIL_INTERNATIONAL = "user@example.co.uk"
    VALID_EMAIL_WITH_NUMBERS = "user123@example.com"
    VALID_EMAIL_WITH_DOTS = "first.last@example.com"

    VALID_EMAILS_LIST = [
        "user1@example.com",
        "user2@example.com",
        "user3@example.com",
        "user4@example.com",
        "user5@example.com"
    ]

    # Invalid Email Test Data
    INVALID_EMAIL_NO_AT_SYMBOL = "userexample.com"
    INVALID_EMAIL_NO_DOMAIN = "user@"
    INVALID_EMAIL_NO_LOCAL = "@example.com"
    INVALID_EMAIL_SPACES = "user @example.com"
    INVALID_EMAIL_SPECIAL_CHARS = "user#@example.com"

    INVALID_EMAILS_LIST = [
        "invalid.email",
        "user@",
        "@example.com",
        "user @example.com",
        "user#@example.com"
    ]

    # Newsletter Categories
    CATEGORY_PROMOTIONS = "Promotions"
    CATEGORY_PRODUCT_UPDATES = "Product Updates"
    CATEGORY_COMPANY_NEWS = "Company News"
    CATEGORY_TIPS_TRICKS = "Tips & Tricks"
    CATEGORY_SPECIAL_OFFERS = "Special Offers"
    CATEGORY_EXCLUSIVE_DEALS = "Exclusive Deals"
    CATEGORY_NEW_ARRIVALS = "New Arrivals"
    CATEGORY_SALES = "Sales"

    NEWSLETTER_CATEGORIES = [
        CATEGORY_PROMOTIONS,
        CATEGORY_PRODUCT_UPDATES,
        CATEGORY_COMPANY_NEWS,
        CATEGORY_TIPS_TRICKS,
        CATEGORY_SPECIAL_OFFERS,
        CATEGORY_EXCLUSIVE_DEALS,
        CATEGORY_NEW_ARRIVALS,
        CATEGORY_SALES
    ]

    SINGLE_CATEGORY_SELECTION = [CATEGORY_PROMOTIONS]
    MULTIPLE_CATEGORIES_SELECTION = [
        CATEGORY_PROMOTIONS,
        CATEGORY_PRODUCT_UPDATES,
        CATEGORY_SPECIAL_OFFERS
    ]
    ALL_CATEGORIES_SELECTION = NEWSLETTER_CATEGORIES

    # Newsletter Frequency Options
    FREQUENCY_DAILY = "Daily"
    FREQUENCY_WEEKLY = "Weekly"
    FREQUENCY_MONTHLY = "Monthly"
    FREQUENCY_QUARTERLY = "Quarterly"
    FREQUENCY_YEARLY = "Yearly"
    FREQUENCY_IMMEDIATE = "Immediate"

    FREQUENCY_OPTIONS = [
        FREQUENCY_DAILY,
        FREQUENCY_WEEKLY,
        FREQUENCY_MONTHLY,
        FREQUENCY_QUARTERLY,
        FREQUENCY_YEARLY,
        FREQUENCY_IMMEDIATE
    ]

    DEFAULT_FREQUENCY = FREQUENCY_WEEKLY
    PREFERRED_FREQUENCY = FREQUENCY_MONTHLY

    # Email Preference Types
    PREFERENCE_PROMOTIONAL = "Promotional Emails"
    PREFERENCE_NOTIFICATIONS = "Notification Emails"
    PREFERENCE_DIGEST = "Digest Emails"
    PREFERENCE_PERSONALIZED_OFFERS = "Personalized Offers"

    PREFERENCE_OPTIONS = [
        PREFERENCE_PROMOTIONAL,
        PREFERENCE_NOTIFICATIONS,
        PREFERENCE_DIGEST,
        PREFERENCE_PERSONALIZED_OFFERS
    ]

    # Preference Configurations
    ALL_PREFERENCES_ENABLED = {
        'promotional': True,
        'notifications': True,
        'digest': True,
        'personalized_offers': True
    }

    ALL_PREFERENCES_DISABLED = {
        'promotional': False,
        'notifications': False,
        'digest': False,
        'personalized_offers': False
    }

    MIXED_PREFERENCES_1 = {
        'promotional': True,
        'notifications': False,
        'digest': True,
        'personalized_offers': False
    }

    MIXED_PREFERENCES_2 = {
        'promotional': False,
        'notifications': True,
        'digest': False,
        'personalized_offers': True
    }

    ONLY_PROMOTIONS = {
        'promotional': True,
        'notifications': False,
        'digest': False,
        'personalized_offers': False
    }

    ONLY_NOTIFICATIONS = {
        'promotional': False,
        'notifications': True,
        'digest': False,
        'personalized_offers': False
    }

    # Subscription Status Messages
    STATUS_SUBSCRIBED = "You are subscribed to our newsletter"
    STATUS_UNSUBSCRIBED = "You have unsubscribed from our newsletter"
    STATUS_PENDING_VERIFICATION = "Please verify your email address"
    STATUS_SUBSCRIPTION_UPDATED = "Your subscription has been updated"
    STATUS_PREFERENCES_UPDATED = "Your preferences have been saved"

    # Success Messages
    SUCCESS_SUBSCRIPTION = "Successfully subscribed to newsletter"
    SUCCESS_UNSUBSCRIPTION = "Successfully unsubscribed from newsletter"
    SUCCESS_EMAIL_UPDATE = "Email address updated successfully"
    SUCCESS_PREFERENCES_SAVED = "Preferences saved successfully"
    SUCCESS_PREFERENCES_UPDATED = "Newsletter preferences updated"
    SUCCESS_EMAIL_VERIFIED = "Email verified successfully"
    SUCCESS_CATEGORY_SELECTED = "Category selected successfully"

    # Error Messages
    ERROR_INVALID_EMAIL = "Please enter a valid email address"
    ERROR_EMAIL_ALREADY_SUBSCRIBED = "This email is already subscribed"
    ERROR_EMAIL_NOT_FOUND = "Email address not found"
    ERROR_SAVE_PREFERENCES = "Failed to save preferences"
    ERROR_UPDATE_EMAIL = "Failed to update email address"
    ERROR_SUBSCRIPTION_FAILED = "Subscription failed"
    ERROR_UNSUBSCRIPTION_FAILED = "Unsubscription failed"

    # Warning Messages
    WARNING_NO_CATEGORIES_SELECTED = "Please select at least one category"
    WARNING_EMAIL_NOT_VERIFIED = "Your email has not been verified"
    WARNING_UNSAVED_CHANGES = "You have unsaved changes"
    WARNING_DUPLICATE_SUBSCRIPTION = "This email is already in our system"

    # Activity Types
    ACTIVITY_SUBSCRIBED = "Subscribed"
    ACTIVITY_UNSUBSCRIBED = "Unsubscribed"
    ACTIVITY_EMAIL_UPDATED = "Email Updated"
    ACTIVITY_PREFERENCES_CHANGED = "Preferences Changed"
    ACTIVITY_EMAIL_VERIFIED = "Email Verified"
    ACTIVITY_CATEGORY_SELECTED = "Category Selected"
    ACTIVITY_FREQUENCY_CHANGED = "Frequency Changed"

    ACTIVITY_TYPES = [
        ACTIVITY_SUBSCRIBED,
        ACTIVITY_UNSUBSCRIBED,
        ACTIVITY_EMAIL_UPDATED,
        ACTIVITY_PREFERENCES_CHANGED,
        ACTIVITY_EMAIL_VERIFIED,
        ACTIVITY_CATEGORY_SELECTED,
        ACTIVITY_FREQUENCY_CHANGED
    ]

    # Subscription Scenario Data
    COMPLETE_SUBSCRIPTION_CONFIG = {
        'email': VALID_EMAIL_FOR_SUBSCRIPTION,
        'categories': MULTIPLE_CATEGORIES_SELECTION,
        'frequency': FREQUENCY_WEEKLY,
        'preferences': MIXED_PREFERENCES_1
    }

    MINIMAL_SUBSCRIPTION_CONFIG = {
        'email': VALID_EMAIL_FOR_SUBSCRIPTION,
        'categories': SINGLE_CATEGORY_SELECTION,
        'frequency': FREQUENCY_MONTHLY,
        'preferences': ONLY_PROMOTIONS
    }

    MAXIMUM_ENGAGEMENT_CONFIG = {
        'email': VALID_EMAIL_FOR_SUBSCRIPTION,
        'categories': ALL_CATEGORIES_SELECTION,
        'frequency': FREQUENCY_DAILY,
        'preferences': ALL_PREFERENCES_ENABLED
    }

    MINIMAL_ENGAGEMENT_CONFIG = {
        'email': VALID_EMAIL_FOR_SUBSCRIPTION,
        'categories': SINGLE_CATEGORY_SELECTION,
        'frequency': FREQUENCY_QUARTERLY,
        'preferences': ONLY_PROMOTIONS
    }

    # Email Update Scenarios
    VALID_EMAIL_UPDATE_PAIRS = [
        ('old@example.com', 'new@example.com'),
        ('user1@example.com', 'user2@example.com'),
        ('subscriber@example.com', 'customer@example.com')
    ]

    # Subscription History Test Data
    EXPECTED_ACTIVITY_COUNT_NEW_USER = 1  # Initial subscription
    EXPECTED_ACTIVITY_COUNT_ACTIVE_USER = 5  # Multiple interactions
    EXPECTED_ACTIVITY_COUNT_INACTIVE_USER = 2  # Minimal interactions

    # Pagination Test Data
    RECORDS_PER_PAGE = 10
    TOTAL_ACTIVITY_RECORDS_LARGE = 50
    TOTAL_ACTIVITY_RECORDS_MEDIUM = 25
    TOTAL_ACTIVITY_RECORDS_SMALL = 5

    EXPECTED_TOTAL_PAGES_LARGE = 5
    EXPECTED_TOTAL_PAGES_MEDIUM = 3
    EXPECTED_TOTAL_PAGES_SMALL = 1

    # Frequency Change Scenarios
    FREQUENCY_CHANGE_SCENARIOS = [
        {'from': FREQUENCY_DAILY, 'to': FREQUENCY_WEEKLY},
        {'from': FREQUENCY_WEEKLY, 'to': FREQUENCY_MONTHLY},
        {'from': FREQUENCY_MONTHLY, 'to': FREQUENCY_QUARTERLY},
        {'from': FREQUENCY_QUARTERLY, 'to': FREQUENCY_YEARLY}
    ]

    # Category Selection Scenarios
    CATEGORY_SELECTION_SCENARIO_1 = [
        CATEGORY_PROMOTIONS,
        CATEGORY_PRODUCT_UPDATES
    ]

    CATEGORY_SELECTION_SCENARIO_2 = [
        CATEGORY_SPECIAL_OFFERS,
        CATEGORY_EXCLUSIVE_DEALS,
        CATEGORY_NEW_ARRIVALS
    ]

    CATEGORY_SELECTION_SCENARIO_3 = [
        CATEGORY_COMPANY_NEWS,
        CATEGORY_TIPS_TRICKS,
        CATEGORY_SALES
    ]

    # Preference Toggle Scenarios
    PREFERENCE_TOGGLE_SCENARIO_1 = {
        'promotional': {'enable': True},
        'notifications': {'enable': False},
        'digest': {'enable': True},
        'personalized_offers': {'enable': False}
    }

    PREFERENCE_TOGGLE_SCENARIO_2 = {
        'promotional': {'enable': False},
        'notifications': {'enable': True},
        'digest': {'enable': False},
        'personalized_offers': {'enable': True}
    }

    PREFERENCE_TOGGLE_SCENARIO_3 = {
        'promotional': {'enable': True},
        'notifications': {'enable': True},
        'digest': {'enable': True},
        'personalized_offers': {'enable': True}
    }

    # Bulk Email Test Data
    BULK_EMAILS_FOR_TESTING = [
        "bulk1@example.com",
        "bulk2@example.com",
        "bulk3@example.com",
        "bulk4@example.com",
        "bulk5@example.com"
    ]

    # Performance Test Data
    LARGE_CATEGORY_DATASET = [f"Category_{i}" for i in range(1, 51)]
    LARGE_EMAIL_DATASET_SIZE = 1000
    LARGE_ACTIVITY_DATASET_SIZE = 500

    # Mock Activity Records
    MOCK_ACTIVITY_RECORD_SUBSCRIPTION = {
        'type': ACTIVITY_SUBSCRIBED,
        'date': '2024-01-15',
        'details': 'Email added to newsletter list'
    }

    MOCK_ACTIVITY_RECORD_EMAIL_UPDATE = {
        'type': ACTIVITY_EMAIL_UPDATED,
        'date': '2024-01-20',
        'details': 'Email changed from old@example.com to new@example.com'
    }

    MOCK_ACTIVITY_RECORD_PREFERENCE_CHANGE = {
        'type': ACTIVITY_PREFERENCES_CHANGED,
        'date': '2024-01-25',
        'details': 'Notification preferences updated'
    }

    # Email Verification
    VERIFICATION_LINK_PATTERN = "https://example.com/verify?token="
    VERIFICATION_TOKEN_LENGTH = 32
    VERIFICATION_TIMEOUT_MINUTES = 24 * 60  # 24 hours

    # Time-based Test Data
    RECENT_SUBSCRIPTION_DATE = "2024-01-20"
    OLD_SUBSCRIPTION_DATE = "2023-01-20"

    # Account Status
    ACCOUNT_STATUS_ACTIVE = "Active"
    ACCOUNT_STATUS_INACTIVE = "Inactive"
    ACCOUNT_STATUS_SUSPENDED = "Suspended"
    ACCOUNT_STATUS_UNVERIFIED = "Unverified"

    # Newsletter Edition Types
    EDITION_WEEKLY_DIGEST = "Weekly Digest"
    EDITION_DAILY_BRIEF = "Daily Brief"
    EDITION_MONTHLY_SUMMARY = "Monthly Summary"
    EDITION_SPECIAL_ANNOUNCEMENT = "Special Announcement"

    # Test Email Subjects
    EMAIL_SUBJECT_WELCOME = "Welcome to Our Newsletter"
    EMAIL_SUBJECT_CONFIRMATION = "Confirm Your Subscription"
    EMAIL_SUBJECT_WEEKLY_DIGEST = "Your Weekly Digest"
    EMAIL_SUBJECT_PROMOTIONAL = "Special Promotion for You"
    EMAIL_SUBJECT_UNSUBSCRIBE_CONFIRMATION = "Unsubscribe Confirmation"

    # Default Test Values
    DEFAULT_CATEGORY = CATEGORY_PROMOTIONS
    DEFAULT_FREQUENCY = FREQUENCY_WEEKLY
    DEFAULT_EMAIL = VALID_EMAIL_FOR_SUBSCRIPTION

    # Boundary Test Data
    MINIMUM_EMAIL_LENGTH = 5  # a@b.c
    MAXIMUM_EMAIL_LENGTH = 254
    EMAIL_WITH_MINIMUM_LENGTH = "a@b.c"
    EMAIL_WITH_MAXIMUM_LENGTH = "a" * 240 + "@example.com"

    # Special Characters in Email
    EMAIL_WITH_PLUS = "user+tag@example.com"
    EMAIL_WITH_HYPHEN = "user-name@example.com"
    EMAIL_WITH_UNDERSCORE = "user_name@example.com"
    EMAIL_WITH_NUMBERS = "user123@example.com"
