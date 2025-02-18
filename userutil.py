import random
from datetime import datetime
import string
import re

class UserUtil:

    @staticmethod
    def generate_user_id():
        """Generates a unique 9-digit user ID."""
        current_year = str(datetime.now().year)[2:]  # Get last two digits of the year
        random_digits = ''.join(random.choices(string.digits, k=7))
        return current_year + random_digits

    @staticmethod
    def generate_password():
        """Generates a strong password."""
        while True:  # Ensure the password meets criteria
            password_length = random.randint(8, 16) # Password length between 8 and 16
            password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
            if UserUtil.is_strong_password(password):
                return password

    @staticmethod
    def is_strong_password(password):
         """Checks if a password meets strength criteria."""
         if len(password) < 8:
             return False
         if not any(c.isupper() for c in password):
             return False
         if not any(c.islower() for c in password):
             return False
         if not any(c.isdigit() for c in password):
             return False
         if not any(c in string.punctuation for c in password):
             return False
         return True


    @staticmethod
    def generate_email(name, surname, domain):
        """Generates an email address."""
        return f"{name.lower()}.{surname.lower()}@{domain}"

    @staticmethod
    def validate_email(email):
        """Validates an email address format."""
        pattern = r"^[a-zA-Z]+(?:\.[a-zA-Z]+)*@[a-zA-Z]+(?:\.[a-zA-Z]+)+$"  # More robust regex
        return bool(re.fullmatch(pattern, email))

