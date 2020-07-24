from re import search

class Validator:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def validate_username_not_password(self):
        if not search(self.password, self.username):
            return True
        else:
            print("password and username are not similar")
            return False

    def password_not_common(self):
        with open("common_passwords.txt", "r") as c:
            if self.password not in c.read():
                return True
            else:
                return False
    
    def minimum_length(self, min_length):
        if self.password >= min_length:
            return True
        else:
            return False

    def contains_alphanumeric_and_symbols(self):
        contains_num_and_letter = search("[A-Za-z0-9]+", self.password)
        contains_special_character = search("[!@#$%^&*]+", self.password)
        if contains_num_and_letter and contains_special_character:
            return True
        else:
            return False
        
    def confirm_password(self, password2):
        if self.password == password2:
            return True
        else:
            return False
