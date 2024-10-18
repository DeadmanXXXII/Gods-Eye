import hashlib
import time

# Simple DGA example based on date
def generate_domain():
    current_time = time.strftime("%Y-%m-%d")
    domain = hashlib.md5(current_time.encode()).hexdigest()[:10] + ".com"
    return domain

# Example usage
print(generate_domain())
