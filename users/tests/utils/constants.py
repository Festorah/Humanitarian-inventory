from typing import Any, Dict

VALID_PASSWORD = "SecurePass123!"

TEST_DATA: Dict[str, Any] = {
    "VALID_REGISTRATION": {
        "email": "test@example.com",
        "password": VALID_PASSWORD,
        "password2": VALID_PASSWORD,
    },
    "INVALID_REGISTRATION": {
        "WEAK_PASSWORD": {
            "email": "test@example.com",
            "password": "weak",
            "password2": "weak",
        },
        "MISMATCHED_PASSWORDS": {
            "email": "test@example.com",
            "password": VALID_PASSWORD,
            "password2": "DifferentPass123!",
        },
    },
}
