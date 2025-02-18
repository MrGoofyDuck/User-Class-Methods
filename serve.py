from user import User

class Userservice:

    users = {}

    
    @classmethod
    def add_user(cls, user):
        cls.users[user.user_id] = user

    @classmethod
    def find_user(cls, user_id):
        return cls.users.get(user_id, None)
    
    @classmethod
    def delete_user(cls, user_id):
        if user_id in cls.users:
            del cls.users[user_id]

    @classmethod
    def update_user(cls, user_id, user_update):
        if user_id in cls.users:
            user = cls.users[user_id]
            user.name = user_update.name if hasattr(user_update, "name") else user.name
            user.get_age = user_update.get_age if hasattr(user_update, "age") else user.get_age

    @classmethod
    def user_number(cls):
        return len(cls.users)
    
    

