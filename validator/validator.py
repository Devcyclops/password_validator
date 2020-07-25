from re import search

class Validator:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def username_in_password(self):
        return search(self.username, self.password)

    def password_is_common(self):
        with open("common_passwords.txt", "r") as c:
            return self.password in c.read()
    
    def is_minimum_length(self, min_length):
        return self.password >= min_length

    def contains_alphanumeric_and_symbols(self):
        contains_num_and_letter = search("[A-Za-z0-9]+", self.password)
        contains_special_character = search("[!@#$%^&*]+", self.password)
        return contains_num_and_letter and contains_special_character
        
    def confirm_password(self, password2):
        return self.password == password2
