from user import User
from datetime import datetime


user1 = User(1, "John", "Doe", datetime(1990, 12, 15),"john.doe@example.com", "password123" )

print(user1.get_details())
print (user1.get_age())