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
            if not self.password in c.read():
                return True
            else:
                return False
    
    def minimum_password_length(self):
        


        

if __name__ == "__main__":
    run()



