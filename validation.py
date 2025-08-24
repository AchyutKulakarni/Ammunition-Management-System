import re

def validate_caliber(caliber):
    pattern = r"^[\w\.]+$"
    return bool(re.match(pattern, caliber))

def validate_manufacturer(manufacturer):
    pattern = r"^[a-zA-Z\s.\-]+$"
    return bool(re.match(pattern, manufacturer))

def validate_date(date_str):
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    return bool(re.match(pattern, date_str))
