import re

def extract_phone_numbers(text):
    pattern = r'\+91[-\s]?\d{3}[-\s]?\d{3}[-\s]?\d{4}|\d{3}[-\s]?\d{3}[-\s]?\d{4}|\d{10}'
    return re.findall(pattern, text)

text = """
Contact us at 9876543210 or +91-9876543210.
For international queries, call +91 987 654 3210.
Invalid numbers: 12345, 98765abc321, 555-55-5555.
"""

print(extract_phone_numbers(text))
