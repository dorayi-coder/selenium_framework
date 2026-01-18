"""Test data for Transactions feature tests."""

VALID_TRANSACTIONS = [
    {
        "id": "txn_001",
        "type": "payment",
        "amount": 99.99,
        "currency": "USD",
        "status": "completed",
        "timestamp": "2025-12-23T10:30:00Z",
        "description": "Order payment",
    },
    {
        "id": "txn_002",
        "type": "refund",
        "amount": 50.00,
        "currency": "USD",
        "status": "completed",
        "timestamp": "2025-12-23T11:00:00Z",
        "description": "Partial refund",
    },
    {
        "id": "txn_003",
        "type": "transfer",
        "amount": 150.00,
        "currency": "USD",
        "status": "completed",
        "timestamp": "2025-12-23T12:00:00Z",
        "description": "Account transfer",
    },
]

TRANSACTION_TYPES = ["payment", "refund", "transfer", "withdrawal", "deposit"]

TRANSACTION_STATUSES = [
    "pending",
    "completed",
    "failed",
    "cancelled",
    "processing",
    "on_hold",
]

PAYMENT_METHODS = [
    {"name": "Credit Card", "type": "card", "is_active": True},
    {"name": "Debit Card", "type": "card", "is_active": True},
    {"name": "Bank Transfer", "type": "bank", "is_active": True},
    {"name": "PayPal", "type": "wallet", "is_active": False},
    {"name": "Apple Pay", "type": "digital", "is_active": True},
]

VALID_AMOUNTS = [
    {"amount": 0.01, "currency": "USD", "description": "Minimum amount"},
    {"amount": 100.00, "currency": "USD", "description": "Standard amount"},
    {"amount": 1000.00, "currency": "USD", "description": "Large amount"},
    {"amount": 9999.99, "currency": "USD", "description": "Maximum amount"},
]

INVALID_AMOUNTS = [
    {"amount": 0.00, "error": "Amount must be greater than zero"},
    {"amount": -50.00, "error": "Amount cannot be negative"},
    {"amount": 10000.00, "error": "Amount exceeds maximum limit"},
    {"amount": 0.001, "error": "Invalid decimal precision"},
]

UNSUPPORTED_CURRENCIES = [
    "XYZ",
    "TEST",
    "FAKE",
    "000",
]

SUPPORTED_CURRENCIES = [
    "USD",
    "EUR",
    "GBP",
    "JPY",
    "CAD",
    "AUD",
]

FAILED_TRANSACTIONS = [
    {
        "id": "failed_txn_001",
        "reason": "Insufficient funds",
        "recovery_possible": True,
    },
    {
        "id": "failed_txn_002",
        "reason": "Invalid card",
        "recovery_possible": True,
    },
    {
        "id": "failed_txn_003",
        "reason": "Transaction timeout",
        "recovery_possible": True,
    },
    {
        "id": "failed_txn_004",
        "reason": "Fraud detected",
        "recovery_possible": False,
    },
]

DUPLICATE_TRANSACTION_ATTEMPTS = [
    {
        "amount": 75.50,
        "description": "Duplicate payment attempt 1",
    },
    {
        "amount": 75.50,
        "description": "Duplicate payment attempt 2",
    },
]

CONCURRENT_TRANSACTIONS = [
    {"id": "concurrent_001", "amount": 50.00},
    {"id": "concurrent_002", "amount": 75.00},
    {"id": "concurrent_003", "amount": 25.00},
]

TRANSACTION_LIMITS = {
    "daily_limit_usd": 5000,
    "monthly_limit_usd": 50000,
    "per_transaction_min_usd": 0.01,
    "per_transaction_max_usd": 9999.99,
}

PENDING_TRANSACTIONS = [
    {
        "id": "pending_001",
        "amount": 100.00,
        "status": "pending",
        "age_minutes": 5,
    },
    {
        "id": "pending_002",
        "amount": 200.00,
        "status": "pending",
        "age_minutes": 30,
    },
    {
        "id": "pending_003",
        "amount": 150.00,
        "status": "pending",
        "age_minutes": 120,
    },
]

TRANSACTION_SEARCH_CRITERIA = [
    {"type": "date_range", "start_date": "2025-12-01", "end_date": "2025-12-31"},
    {"type": "amount_range", "min_amount": 50.00, "max_amount": 500.00},
    {"type": "status_filter", "status": "completed"},
    {"type": "transaction_type", "transaction_type": "payment"},
]

REFUND_SCENARIOS = [
    {"original_txn_id": "txn_001", "refund_amount": 99.99, "refund_type": "full"},
    {"original_txn_id": "txn_002", "refund_amount": 50.00, "refund_type": "partial"},
    {"original_txn_id": "txn_003", "refund_amount": 75.00, "refund_type": "partial"},
]

TRANSACTION_RECONCILIATION_DATA = {
    "expected_total": 250.00,
    "expected_count": 3,
    "date_range": "2025-12-23",
}

MALFORMED_TRANSACTION_DATA = [
    {"amount": "invalid_string", "error": "Amount must be numeric"},
    {"amount": None, "error": "Amount is required"},
    {"currency": "", "error": "Currency is required"},
    {"type": "unknown_type", "error": "Invalid transaction type"},
]

HIGH_VALUE_TRANSACTION_THRESHOLDS = {
    "high_value_usd": 1000,
    "requires_approval": True,
    "requires_verification": True,
}

TRANSACTION_RETRY_POLICY = {
    "max_retries": 3,
    "retry_delay_seconds": 5,
    "backoff_multiplier": 2,
}

BULK_TRANSACTION_UPLOAD = {
    "max_records": 1000,
    "accepted_formats": ["csv", "xlsx", "json"],
    "max_file_size_mb": 10,
}

TRANSACTION_AUDIT_LOG = {
    "retention_days": 2555,
    "fields_tracked": [
        "transaction_id",
        "user_id",
        "action",
        "timestamp",
        "ip_address",
    ],
}

TRANSACTION_FEES = [
    {"transaction_type": "payment", "percentage": 0.0, "fixed": 0.00},
    {"transaction_type": "transfer", "percentage": 0.5, "fixed": 0.00},
    {"transaction_type": "withdrawal", "percentage": 0.0, "fixed": 1.50},
]
