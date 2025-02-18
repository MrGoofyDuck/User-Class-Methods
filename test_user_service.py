from serve import Userservice
from user import User
from datetime import datetime

if __name__ == "__main__":

    user1 = User(1, "Alice", 'Doe', datetime(1990, 12, 15), "john.doe@example.com", "password123")
    user2 = User(2, "Bob", 'Doe', datetime(1998, 1, 3), "john.doe@example.com", "password123")

    Userservice.add_user(user1)
    Userservice.add_user(user2)

    print(Userservice.users)

    #print(Userservice.find_user(1))

    #update_info = User(1, "Alice", 'Doe', datetime(1990, 12, 15), "john.doe@example.com", "password123")
    #Userservice.update_user(1, update_info)
    #print(Userservice.find_user(1))

    #Userservice.delete_user(2)
    #print(Userservice.users)

    #print(Userservice.user_number())