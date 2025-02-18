from datetime import datetime

class User:
    def __init__(self, user_id, name, surname, birthday:datetime, email, password):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.email = email 
        self.password = password

    def get_details(self):
        return ({self.user_id, 
                 self.name,
                 self.surname,
                 self.email,
                 self.birthday})
    
    def get_age(self, today = None):
        today = datetime.today().year
        
        return today - self.birthday.year 
    
