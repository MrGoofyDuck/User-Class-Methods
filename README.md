# User Management System

This project implements a user management system using object-oriented principles in Python. It includes classes for managing user data, performing user-related operations, and providing utility functions.  The system emphasizes proper use of instance variables, class attributes/methods, and static methods.  Comprehensive unit tests are included to ensure the correctness of the code.

## Project Structure


## Classes

### 1. `User`

Represents a user with the following attributes:

*   `user_id` (int): Unique identifier.
*   `name` (str): First name.
*   `surname` (str): Last name.
*   `email` (str): Email address.
*   `password` (str): User password.
*   `birthday` (datetime): Birthday.

**Methods:**

*   `__init__(self, user_id, name, surname, birthday)`: Initializes a new User object.
*   `get_details(self)`: Returns a formatted string containing user details.
*   `get_age(self)`: Computes and returns the user's age.

### 2. `UserService`

Manages a collection of `User` objects.

**Class Attribute:**

*   `users` (dict): A dictionary storing `User` objects, keyed by `user_id`.

**Class Methods:**

*   `add_user(cls, user)`: Adds a `User` object to the `users` dictionary.
*   `find_user(cls, user_id)`: Searches for a user by `user_id`.
*   `delete_user(cls, user_id)`: Removes a user by `user_id`.
*   `update_user(cls, user_id, user_update)`: Updates user attributes. `user_update` should be a dictionary containing the attributes to update.
*   `get_number(cls)`: Returns the number of users.

### 3. `UserUtil`

Provides utility functions for user management.

**Static Methods:**

*   `generate_user_id()`: Generates a unique 9-digit user ID (first two digits are the current year).
*   `generate_password()`: Generates a strong password (min 8 characters, at least one uppercase, lowercase, digit, and special character).
*   `is_strong_password(password)`: Checks password strength.
*   `generate_email(name, surname, domain)`: Generates an email address.
*   `validate_email(email)`: Validates email format.

## How to Run

1.  Clone the repository:

    ```bash
    git clone [https://github.com/YOUR_USERNAME/user_management.git](https://www.google.com/search?q=https://github.com/YOUR_USERNAME/user_management.git)  # Replace with your repository URL
    cd user_management
    ```

2.  Run the unit tests:

    ```bash
    python -m unittest test_user.py
    python -m unittest test_user_service.py
    python -m unittest test_user_util.py
    ```

3.  (Optional) You can create a main script to demonstrate the usage of the classes and methods.

## Sample Usage and Output

```python
# Example Usage (Illustrative)
from user import User
from user_service import UserService
from user_util import UserUtil
import datetime

user1 = User(UserUtil.generate_user_id(), "John", "Doe", datetime.date(1990, 5, 15))
UserService.add_user(user1)

print(user1.get_details())
print(f"Age: {user1.get_age()}")

print(f"Number of users: {UserService.get_number()}")

user2 = UserService.find_user(user1.user_id)
if user2:
    print("User found!")

UserService.delete_user(user1.user_id)
print(f"Number of users after deletion: {UserService.get_number()}")

print(f"Generated Password: {UserUtil.generate_password()}")
print(f"Generated Email: {UserUtil.generate_email('jane', 'smith', 'example.com')}")

# Sample Output (Will vary based on random generation)
# User ID: 247895432
# Name: John
# Surname: Doe
# Email: None
# Birthday: 1990-05-15
# Age: 33
# Number of users: 1
# User found!
# Number of users after deletion: 0
# Generated Password:  P@$$wOrd123  # Example
# Generated Email: [email address removed]
