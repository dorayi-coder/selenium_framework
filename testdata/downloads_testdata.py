"""Test data for Downloads feature tests."""

VALID_DOWNLOADABLE_FILES = [
    {
        "id": "file_001",
        "name": "product_manual.pdf",
        "format": "pdf",
        "size_mb": 2.5,
        "version": "1.0",
    },
    {
        "id": "file_002",
        "name": "software_guide.zip",
        "format": "zip",
        "size_mb": 15.3,
        "version": "2.1",
    },
    {
        "id": "file_003",
        "name": "license_agreement.docx",
        "format": "docx",
        "size_mb": 0.5,
        "version": "1.2",
    },
]

DOWNLOAD_FORMATS = ["pdf", "zip", "docx", "xlsx", "txt", "mp4"]

RESTRICTED_FILES = [
    {
        "id": "restricted_001",
        "name": "confidential_data.pdf",
        "error": "Access denied",
    },
    {
        "id": "restricted_002",
        "name": "admin_only.zip",
        "error": "Insufficient permissions",
    },
]

EXPIRED_DOWNLOAD_LINKS = [
    {
        "id": "expired_001",
        "name": "old_file.pdf",
        "error": "Download link expired",
    },
    {
        "id": "expired_002",
        "name": "outdated_guide.zip",
        "error": "This download is no longer available",
    },
]

LARGE_FILES = [
    {"name": "large_file_100mb.zip", "size_mb": 100},
    {"name": "large_file_500mb.zip", "size_mb": 500},
    {"name": "large_file_1gb.zip", "size_mb": 1024},
]

MALFORMED_FILE_NAMES = [
    {"name": "", "error": "Invalid file name"},
    {"name": " " * 50, "error": "Invalid file name"},
    {"name": "<script>alert('xss')</script>.pdf", "error": "Invalid file name"},
    {"name": "../../etc/passwd", "error": "Invalid file name"},
    {"name": "file|with|pipes.pdf", "error": "Invalid file name"},
]

DOWNLOAD_SPEED_REQUIREMENTS = {
    "min_speed_mbps": 0.1,
    "timeout_seconds": 300,
    "retry_attempts": 3,
}

CONCURRENT_DOWNLOAD_LIMITS = {
    "max_concurrent_downloads": 5,
    "max_downloads_per_day": 50,
    "max_total_size_per_day_mb": 1000,
}

INVALID_FILE_IDS = [
    "nonexistent_file_123",
    "invalid_id_xyz",
    "0",
    "-1",
    "999999999",
]

DOWNLOAD_EXTENSIONS_ALLOWED = [
    ".pdf",
    ".zip",
    ".docx",
    ".xlsx",
    ".txt",
    ".jpg",
    ".png",
    ".mp4",
]

DOWNLOAD_EXTENSIONS_BLOCKED = [
    ".exe",
    ".bat",
    ".cmd",
    ".scr",
    ".vbs",
    ".app",
]

EXPECTED_DOWNLOAD_HEADERS = {
    "content-disposition": "attachment",
    "content-type": "application/octet-stream",
}

DOWNLOAD_HISTORY_RETENTION_DAYS = 90
MAX_DOWNLOAD_HISTORY_RECORDS = 1000

PAUSE_RESUME_FILE_SIZES = [
    {"name": "resumable_small.zip", "size_mb": 5},
    {"name": "resumable_medium.zip", "size_mb": 50},
    {"name": "resumable_large.zip", "size_mb": 200},
]
