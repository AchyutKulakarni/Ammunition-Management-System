import re

def validate_caliber(caliber):
    # Example: Caliber like 9mm, .45ACP, etc. Basic check allowing alphanumerics and dots
    pattern = r"^[\w\.]+$"
    return bool(re.match(pattern, caliber))

def validate_manufacturer(manufacturer):
    # Allow letters, spaces, dots, and hyphens
    pattern = r"^[a-zA-Z\s.\-]+$"
    return bool(re.match(pattern, manufacturer))

def validate_date(date_str):
    # Dates in YYYY-MM-DD format
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    return bool(re.match(pattern, date_str))
