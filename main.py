import re

Tracking_REGEX = re.compile(r'[\d{1}]+[Z]+[\d{16}]+')
Order_REGEX = re.compile(r'ORD-\d{5}')
Email_REGEX = re.compile(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+.+\.[a-zA-Z]+')
SKU_REGEX = re.compile(r'[A-Z]{3}-[A-Z]{3}-\d{3}')

patterns = [SKU_REGEX, Order_REGEX, Tracking_REGEX]
with open("raw_system_logs.txt", "r") as file:
    for line in file:
       privacy_line = Email_REGEX.sub('[REDACTED-EMAIL]', line)
       for pattern in patterns:
            match = pattern.search(privacy_line)
            if match:
                print(match.group())