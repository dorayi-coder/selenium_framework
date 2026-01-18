"""
Affiliate Feature Test Data
Provides all constants and test data for Affiliate feature testing
"""


class AffiliateTestData:
    """Affiliate test data constants"""

    # Referral Link Data
    VALID_REFERRAL_LINK = "https://nopcommerce.com/ref/ABC123DEF456"
    REFERRAL_CODE = "ABC123DEF456"
    AFFILIATE_LINK_WITH_CODE = "https://nopcommerce.com/?affiliatecode=ABC123DEF456"
    SECONDARY_REFERRAL_LINK = "https://nopcommerce.com/ref/XYZ789PQR012"
    SECONDARY_REFERRAL_CODE = "XYZ789PQR012"

    # Commission Types
    COMMISSION_TYPES = [
        "Sale Commission",
        "Sign-up Bonus",
        "Tiered Commission",
        "Referral Bonus",
        "Product Commission"
    ]

    # Commission Statuses
    COMMISSION_STATUSES = [
        "Pending",
        "Approved",
        "Rejected",
        "Completed",
        "Processing",
        "On Hold"
    ]

    # Payout Methods
    PAYOUT_METHODS = [
        "Bank Transfer",
        "PayPal",
        "Wire Transfer",
        "Check",
        "Cryptocurrency"
    ]

    PAYOUT_METHOD_BANK_TRANSFER = "Bank Transfer"
    PAYOUT_METHOD_PAYPAL = "PayPal"
    PAYOUT_METHOD_WIRE_TRANSFER = "Wire Transfer"
    PAYOUT_METHOD_CHECK = "Check"
    PAYOUT_METHOD_CRYPTOCURRENCY = "Cryptocurrency"

    # Bank Details for Testing
    VALID_BANK_DETAILS = {
        "bank_name": "Wells Fargo",
        "account_holder": "John Doe",
        "account_number": "1234567890",
        "routing_number": "121000248",
        "swift_code": "WFFAUS6W"
    }

    ALTERNATIVE_BANK_DETAILS = {
        "bank_name": "Bank of America",
        "account_holder": "Jane Smith",
        "account_number": "9876543210",
        "routing_number": "026009593",
        "swift_code": "BOFAUS3N"
    }

    INTERNATIONAL_BANK_DETAILS = {
        "bank_name": "HSBC Bank UK",
        "account_holder": "Alex Johnson",
        "account_number": "12345678",
        "routing_number": "230003051",
        "swift_code": "HSBCGB2L"
    }

    # Commission Filter Scenarios
    FILTER_BY_STATUS_PENDING = "Pending"
    FILTER_BY_STATUS_COMPLETED = "Completed"
    FILTER_BY_STATUS_REJECTED = "Rejected"

    FILTER_BY_TYPE_SALE = "Sale Commission"
    FILTER_BY_TYPE_SIGNUP = "Sign-up Bonus"

    # Date Filters
    DATE_FILTER_LAST_30_DAYS = "Last 30 Days"
    DATE_FILTER_LAST_90_DAYS = "Last 90 Days"
    DATE_FILTER_LAST_6_MONTHS = "Last 6 Months"
    DATE_FILTER_LAST_YEAR = "Last Year"
    DATE_FILTER_CUSTOM = "Custom Date Range"

    # Sort Options
    SORT_BY_DATE_DESC = "Date (Newest)"
    SORT_BY_DATE_ASC = "Date (Oldest)"
    SORT_BY_AMOUNT_DESC = "Amount (Highest)"
    SORT_BY_AMOUNT_ASC = "Amount (Lowest)"
    SORT_BY_STATUS = "Status"
    SORT_BY_TYPE = "Type"

    # Commission Amount Data
    VALID_COMMISSION_AMOUNTS = [
        "$10.00",
        "$25.50",
        "$100.00",
        "$500.00",
        "$1,000.00",
        "$5,000.00"
    ]

    COMMISSION_AMOUNT_THRESHOLD = 100.0  # Dollar amount threshold
    COMMISSION_AMOUNT_FOR_PAYOUT_ELIGIBLE = 50.0

    # Dashboard Statistics for Testing
    EXPECTED_ZERO_REFERRALS = 0
    EXPECTED_ZERO_COMMISSIONS = 0.0
    EXPECTED_ZERO_PAYOUTS = 0.0

    EXPECTED_HIGH_REFERRAL_COUNT = 50
    EXPECTED_HIGH_COMMISSION_AMOUNT = 5000.0
    EXPECTED_HIGH_PAYOUT_AMOUNT = 10000.0

    # Tab Names
    TAB_COMMISSION_HISTORY = "Commission History"
    TAB_REFERRALS = "Referrals"
    TAB_PAYOUTS = "Payouts"
    TAB_SETTINGS = "Settings"

    # Message Types
    SUCCESS_MESSAGE_PAYOUT_REQUESTED = "Payout request submitted successfully"
    SUCCESS_MESSAGE_BANK_DETAILS_UPDATED = "Bank account details updated successfully"
    SUCCESS_MESSAGE_LINK_COPIED = "Referral link copied to clipboard"
    SUCCESS_MESSAGE_NEW_LINK_GENERATED = "New referral link generated successfully"

    ERROR_MESSAGE_INVALID_BANK_DETAILS = "Invalid bank details provided"
    ERROR_MESSAGE_PAYOUT_AMOUNT_TOO_LOW = "Payout amount below minimum threshold"
    ERROR_MESSAGE_DUPLICATE_PAYOUT_REQUEST = "Payout request already pending"

    # Search Terms
    SEARCH_TERM_BY_REFERRAL_NAME = "John Doe"
    SEARCH_TERM_BY_EMAIL = "john@example.com"
    SEARCH_TERM_BY_COMMISSION_ID = "COMM-12345"
    SEARCH_TERM_BY_TRANSACTION_ID = "TXN-67890"

    # Referral Data
    VALID_REFERRAL_NAMES = [
        "Alice Cooper",
        "Bob Wilson",
        "Charlie Brown",
        "David Johnson",
        "Emma Davis"
    ]

    VALID_REFERRAL_EMAILS = [
        "alice@example.com",
        "bob@example.com",
        "charlie@example.com",
        "david@example.com",
        "emma@example.com"
    ]

    # Payout Status
    PAYOUT_STATUS_PENDING = "Pending"
    PAYOUT_STATUS_PROCESSING = "Processing"
    PAYOUT_STATUS_COMPLETED = "Completed"
    PAYOUT_STATUS_FAILED = "Failed"

    PAYOUT_STATUSES = [
        PAYOUT_STATUS_PENDING,
        PAYOUT_STATUS_PROCESSING,
        PAYOUT_STATUS_COMPLETED,
        PAYOUT_STATUS_FAILED
    ]

    # Minimum Thresholds
    MINIMUM_PAYOUT_AMOUNT = 50.0
    MINIMUM_COMMISSION_FOR_APPROVAL = 0.0
    MAXIMUM_PAYOUT_REQUEST_PER_MONTH = 10

    # Pagination Data
    RECORDS_PER_PAGE = 10
    TOTAL_PAGES_FOR_LARGE_DATASET = 5
    FIRST_PAGE_NUMBER = 1
    LAST_PAGE_NUMBER = 5

    # Invalid/Edge Case Data
    INVALID_BANK_ACCOUNT_NUMBER = "123"  # Too short
    INVALID_ROUTING_NUMBER = "12345"  # Invalid length
    INVALID_SWIFT_CODE = "INVALID"  # Wrong format

    EMPTY_BANK_ACCOUNT_HOLDER = ""
    EMPTY_BANK_NAME = ""

    # Performance Test Data
    LARGE_COMMISSION_DATASET_SIZE = 1000
    LARGE_REFERRAL_DATASET_SIZE = 500
    BULK_SEARCH_TERMS = [
        "commission",
        "referral",
        "payout",
        "bank",
        "transfer"
    ]

    # Commission Scenarios
    HIGH_VALUE_COMMISSION = {
        "id": "COMM-1000",
        "type": "Sale Commission",
        "amount": "$5,000.00",
        "status": "Completed",
        "date": "2024-01-15"
    }

    LOW_VALUE_COMMISSION = {
        "id": "COMM-1001",
        "type": "Sign-up Bonus",
        "amount": "$10.00",
        "status": "Pending",
        "date": "2024-01-20"
    }

    REJECTED_COMMISSION = {
        "id": "COMM-1002",
        "type": "Referral Bonus",
        "amount": "$100.00",
        "status": "Rejected",
        "date": "2024-01-18"
    }

    # Payout Request Scenarios
    PAYOUT_REQUEST_DATA = {
        "method": "Bank Transfer",
        "amount": "$500.00",
        "bank_name": "Wells Fargo",
        "account_holder": "John Doe",
        "account_number": "1234567890",
        "routing_number": "121000248"
    }

    # Referral Performance Tiers
    TIER_BRONZE = "Bronze"  # 1-10 referrals
    TIER_SILVER = "Silver"  # 11-50 referrals
    TIER_GOLD = "Gold"  # 51-100 referrals
    TIER_PLATINUM = "Platinum"  # 100+ referrals

    TIER_COMMISSION_MULTIPLIERS = {
        TIER_BRONZE: 1.0,
        TIER_SILVER: 1.25,
        TIER_GOLD: 1.5,
        TIER_PLATINUM: 2.0
    }

    # API Response Data (for mock testing)
    MOCK_COMMISSION_RESPONSE = {
        "id": "COMM-12345",
        "type": "Sale Commission",
        "amount": 250.00,
        "currency": "USD",
        "status": "Completed",
        "referral_id": "REF-001",
        "transaction_date": "2024-01-15",
        "processing_date": "2024-01-17",
        "notes": "Commission for successful sale"
    }

    MOCK_REFERRAL_RESPONSE = {
        "id": "REF-001",
        "name": "John Doe",
        "email": "john@example.com",
        "date_referred": "2024-01-10",
        "status": "Active",
        "total_sales": 1000.00,
        "total_commission_earned": 250.00
    }

    MOCK_PAYOUT_RESPONSE = {
        "id": "PAYOUT-001",
        "amount": 500.00,
        "currency": "USD",
        "method": "Bank Transfer",
        "status": "Completed",
        "requested_date": "2024-01-20",
        "processed_date": "2024-01-25",
        "transaction_reference": "TXN-2024-001"
    }

    # Notification Messages
    NOTIFICATION_NEW_REFERRAL = "You have a new referral"
    NOTIFICATION_COMMISSION_EARNED = "Commission earned from referral sale"
    NOTIFICATION_PAYOUT_PROCESSED = "Your payout has been processed"
    NOTIFICATION_PAYOUT_FAILED = "Payout processing failed"

    # Account Status
    ACCOUNT_STATUS_ACTIVE = "Active"
    ACCOUNT_STATUS_SUSPENDED = "Suspended"
    ACCOUNT_STATUS_INACTIVE = "Inactive"
    ACCOUNT_STATUS_PENDING_VERIFICATION = "Pending Verification"

    # Affiliate Registration Data
    AFFILIATE_REGISTRATION_COMPANY = "Test Company"
    AFFILIATE_REGISTRATION_FIRST_NAME = "John"
    AFFILIATE_REGISTRATION_LAST_NAME = "Doe"
    AFFILIATE_REGISTRATION_EMAIL = "affiliate@example.com"
    AFFILIATE_REGISTRATION_PHONE = "+1234567890"
    AFFILIATE_REGISTRATION_ADDRESS = "123 Main St"
    AFFILIATE_REGISTRATION_CITY = "Test City"
    AFFILIATE_REGISTRATION_STATE = "State"
    AFFILIATE_REGISTRATION_ZIPCODE = "12345"
    AFFILIATE_REGISTRATION_COUNTRY = "United States"

    # Affiliate Registration Mandatory Fields Only
    AFFILIATE_MANDATORY_FIRST_NAME = "Jane"
    AFFILIATE_MANDATORY_LAST_NAME = "Smith"
    AFFILIATE_MANDATORY_EMAIL = "jane.affiliate@example.com"
    AFFILIATE_MANDATORY_COMPANY = "Mandatory Company"
