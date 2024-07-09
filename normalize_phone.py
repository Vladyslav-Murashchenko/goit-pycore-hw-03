import re

def add_default_country_code(match: re.Match[str]):
    if (match.group(1) == ''):
        return '+38' + match.group(2)

    return '+' + match.group(1) + match.group(2)

def normalize_phone(phone_number: str) -> str:
    phone_number = re.sub(r'\D', '', phone_number)
    phone_number = re.sub(r'^(\d*)(\d{10})$', add_default_country_code, phone_number)
    return phone_number
