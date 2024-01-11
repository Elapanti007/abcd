import re

def extract_gstin(text):
    pattern = r'\b\d{2}[A-Z]{5}\d{4}[A-Z]{1}\d{1}[Z]{1}[A-Z\d]{1}\b'
    matches = re.findall(pattern, text)
    return matches[0] if matches else None
