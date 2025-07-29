import hashlib
import secrets
from datetime import datetime, timedelta
from typing import Optional

def generate_password_hash(password: str) -> str:
    """Generate password hash"""
    return hashlib.sha256(password.encode()).hexdigest()

def generate_random_token() -> str:
    """Generate random token"""
    return secrets.token_urlsafe(32)

def format_datetime(dt: datetime) -> str:
    """Format datetime to ISO string"""
    return dt.isoformat()

def is_valid_email(email: str) -> bool:
    """Simple email validation"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None 