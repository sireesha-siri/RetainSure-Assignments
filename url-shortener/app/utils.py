# TODO: Implement utility functions here
# Consider functions for:
# - Generating short codes
# - Validating URLs
# - Any other helper functions you need

import random
import string
import re

def generate_short_code(length=6):
    # Generate a random 6-character alphanumeric string (e.g. 'abc123')
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def is_valid_url(url):
    # Basic regular expression to validate HTTP/HTTPS URLs
    regex = re.compile(
        r'^(http|https):\/\/'                   # http:// or https://
        r'(\w+\.)?[\w\-]+\.\w{2,}'              # domain
        r'([\w\-\._~:/?#\[\]@!$&\'()*+,;=]*)*$',# optional path/query/fragment
        re.IGNORECASE
    )
    return re.match(regex, url) is not None
