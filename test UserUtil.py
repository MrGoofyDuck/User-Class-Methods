from userutil import UserUtil


user_id = UserUtil.generate_user_id()
print(f"Generated User ID: {user_id}")

password = UserUtil.generate_password()
print(f"Generated Password: {password}")

is_strong = UserUtil.is_strong_password(password)
print(f"Is password strong? {is_strong}")

email = UserUtil.generate_email("John", "Doe", "example.com")
print(f"Generated Email: {email}")

is_valid_email = UserUtil.validate_email(email)
print(f"Is email valid? {is_valid_email}")

invalid_email = "john.doe@example"
is_valid_invalid = UserUtil.validate_email(invalid_email)
print(f"Is invalid email valid? {is_valid_invalid}")
