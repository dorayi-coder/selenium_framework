"""Test data for Recurring Payments feature tests."""

VALID_SUBSCRIPTIONS = [
    {
        "id": "sub_001",
        "plan": "Premium Monthly",
        "amount": 29.99,
        "currency": "USD",
        "frequency": "monthly",
        "status": "active",
        "start_date": "2025-01-01",
        "next_payment_date": "2026-01-23",
        "payment_method": "Credit Card",
        "description": "Premium plan subscription",
    },
    {
        "id": "sub_002",
        "plan": "Pro Annual",
        "amount": 299.99,
        "currency": "USD",
        "frequency": "yearly",
        "status": "active",
        "start_date": "2024-12-23",
        "next_payment_date": "2025-12-23",
        "payment_method": "PayPal",
        "description": "Professional plan annual subscription",
    },
    {
        "id": "sub_003",
        "plan": "Basic Weekly",
        "amount": 5.99,
        "currency": "USD",
        "frequency": "weekly",
        "status": "paused",
        "start_date": "2025-11-01",
        "next_payment_date": "2026-01-30",
        "payment_method": "Debit Card",
        "description": "Basic weekly plan",
    },
]

SUBSCRIPTION_STATUSES = ["active", "paused", "cancelled", "expired", "pending", "failed"]

SUBSCRIPTION_FREQUENCIES = ["weekly", "bi-weekly", "monthly", "quarterly", "yearly"]

SUBSCRIPTION_PLANS = [
    {"name": "Basic", "amount": 9.99, "frequency": "monthly"},
    {"name": "Premium", "amount": 29.99, "frequency": "monthly"},
    {"name": "Pro", "amount": 99.99, "frequency": "monthly"},
    {"name": "Enterprise", "amount": 299.99, "frequency": "yearly"},
]

VALID_AMOUNTS = [
    {"amount": 0.99, "currency": "USD", "description": "Minimum subscription amount"},
    {"amount": 29.99, "currency": "USD", "description": "Standard monthly amount"},
    {"amount": 299.99, "currency": "USD", "description": "Annual subscription amount"},
    {"amount": 5000.00, "currency": "USD", "description": "Maximum amount"},
]

INVALID_AMOUNTS = [
    {"amount": 0.00, "error": "Amount must be greater than zero"},
    {"amount": -9.99, "error": "Amount cannot be negative"},
    {"amount": 10000.00, "error": "Amount exceeds maximum limit"},
    {"amount": 0.001, "error": "Invalid decimal precision"},
]

PAYMENT_METHODS_FOR_SUBSCRIPTIONS = [
    {"name": "Credit Card", "type": "card", "is_active": True},
    {"name": "Debit Card", "type": "card", "is_active": True},
    {"name": "Bank Account", "type": "bank", "is_active": True},
    {"name": "PayPal", "type": "wallet", "is_active": True},
    {"name": "Apple Pay", "type": "digital", "is_active": True},
]

SUPPORTED_CURRENCIES_FOR_SUBSCRIPTIONS = [
    "USD",
    "EUR",
    "GBP",
    "JPY",
    "CAD",
    "AUD",
]

FAILED_PAYMENT_REASONS = [
    {
        "subscription_id": "sub_failed_001",
        "reason": "Insufficient funds",
        "recovery_possible": True,
    },
    {
        "subscription_id": "sub_failed_002",
        "reason": "Expired card",
        "recovery_possible": True,
    },
    {
        "subscription_id": "sub_failed_003",
        "reason": "Address mismatch",
        "recovery_possible": True,
    },
    {
        "subscription_id": "sub_failed_004",
        "reason": "Fraud detected",
        "recovery_possible": False,
    },
]

SUBSCRIPTION_EDIT_SCENARIOS = [
    {
        "subscription_id": "sub_edit_001",
        "edit_field": "plan",
        "from_value": "Basic",
        "to_value": "Premium",
    },
    {
        "subscription_id": "sub_edit_002",
        "edit_field": "payment_method",
        "from_value": "Credit Card",
        "to_value": "PayPal",
    },
    {
        "subscription_id": "sub_edit_003",
        "edit_field": "billing_date",
        "from_value": "1st of month",
        "to_value": "15th of month",
    },
]

SUBSCRIPTION_PAUSE_RESUME_SCENARIOS = [
    {
        "subscription_id": "sub_pause_001",
        "reason": "Temporary pause",
        "pause_duration": 30,
    },
    {
        "subscription_id": "sub_pause_002",
        "reason": "Financial constraints",
        "pause_duration": 60,
    },
]

SUBSCRIPTION_CANCELLATION_REASONS = [
    "Not using the service",
    "Too expensive",
    "Found better alternative",
    "Service not as expected",
    "Financial constraints",
    "Found better pricing elsewhere",
]

SUBSCRIPTION_RENEWAL_SCENARIOS = [
    {
        "subscription_id": "sub_renew_001",
        "renew_date": "2025-12-23",
        "expected_status": "active",
    },
    {
        "subscription_id": "sub_renew_002",
        "renew_date": "2025-12-30",
        "expected_status": "active",
    },
]

UPGRADE_DOWNGRADE_PATHS = [
    {"from_plan": "Basic", "to_plan": "Premium", "action": "upgrade"},
    {"from_plan": "Premium", "to_plan": "Pro", "action": "upgrade"},
    {"from_plan": "Pro", "to_plan": "Premium", "action": "downgrade"},
    {"from_plan": "Premium", "to_plan": "Basic", "action": "downgrade"},
]

BILLING_CYCLE_TESTS = [
    {"frequency": "weekly", "expected_cycles_per_year": 52},
    {"frequency": "bi-weekly", "expected_cycles_per_year": 26},
    {"frequency": "monthly", "expected_cycles_per_year": 12},
    {"frequency": "quarterly", "expected_cycles_per_year": 4},
    {"frequency": "yearly", "expected_cycles_per_year": 1},
]

PRORATION_SCENARIOS = [
    {
        "scenario": "upgrade_mid_cycle",
        "previous_amount": 29.99,
        "new_amount": 99.99,
        "proration_expected": True,
    },
    {
        "scenario": "downgrade_mid_cycle",
        "previous_amount": 99.99,
        "new_amount": 29.99,
        "proration_expected": True,
    },
    {
        "scenario": "plan_change_same_day",
        "previous_amount": 29.99,
        "new_amount": 49.99,
        "proration_expected": False,
    },
]

NOTIFICATION_SCENARIOS = [
    {"type": "payment_success", "should_send": True},
    {"type": "payment_failed", "should_send": True},
    {"type": "renewal_reminder", "should_send": True},
    {"type": "subscription_expiring", "should_send": True},
    {"type": "plan_change_confirmation", "should_send": True},
    {"type": "cancellation_confirmation", "should_send": True},
]

GRACE_PERIOD_TESTS = [
    {"failed_payment_date": "2025-12-23", "grace_period_days": 3},
    {"failed_payment_date": "2025-12-20", "grace_period_days": 7},
]

SUBSCRIPTION_RETENTION_TESTS = [
    {"offer": "discount_upgrade", "discount_percent": 20},
    {"offer": "free_month", "free_months": 1},
    {"offer": "loyalty_bonus", "bonus_credit": 50},
]

INVALID_SUBSCRIPTION_IDS = [
    "nonexistent_sub_123",
    "invalid_id_xyz",
    "0",
    "-1",
    "999999999",
]

INVALID_PLAN_NAMES = [
    "",
    " " * 50,
    "<script>alert('xss')</script>",
    "../../etc/passwd",
    "plan|with|pipes",
]

CONCURRENT_SUBSCRIPTION_LIMITS = {
    "max_active_subscriptions_per_account": 10,
    "max_subscriptions_per_payment_method": 5,
}

SUBSCRIPTION_TIMELINE_SCENARIOS = [
    {
        "action": "create",
        "expected_status": "pending",
        "next_action": "confirm_payment",
    },
    {
        "action": "confirm_payment",
        "expected_status": "active",
        "next_action": "first_renewal",
    },
    {
        "action": "first_renewal",
        "expected_status": "active",
        "next_action": "pause",
    },
    {
        "action": "pause",
        "expected_status": "paused",
        "next_action": "resume",
    },
]
