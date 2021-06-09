import re
import json

class User():
    def __init__(self, username, imeil, password, name, surname, sex, birthday):
        self.username = username 
        self.imeil = imeil 
        self.password = password 
        self.name = name
        self.surname = surname 
        self.sex = sex #re
        self.birthday = birthday #re
    def add_to_file(self):
        data = {
            'username' : self.username,
            'imeil' : self.imeil,
            'password' : self.password,
            'name' : self.name,
            'surname' : self.surname,
            'sex' : self.sex,
            'birthday' : self.birthday,
            'wishlist' : [],
            'readinglist' : [],
            'readedlist' : []
        }
        with open("users.json", "r") as file:
            file_data = json.load(file)
        with open("users.json", "w") as file:
            file_data['users'].append(data)
            json.dump(file_data, file)

def check_if_username_is_taken(username):
    with open("users.json", "r+") as file:
            file_data = json.load(file)
            users = file_data['users']
            for user in users:
                if username == user["username"]:
                    return False
                #[a-zA-Z0-9._] - alowed symbols , min -  8 symbols, max - 20 symbols , example - petidamm2006, ivan_georgiev, dimitur.petrov;
                if not re.match(r'^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$', username):
                    return False
    return True


def check_if_imeil_is_taken(imeil):
    with open("users.json", "r+") as file:
            file_data = json.load(file)
            users = file_data['users']
            for user in users:
                if imeil == user["imeil"]:
                    return False
                if not re.match(r'^[a-z0-9]+[._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', imeil): 
                    return False  
    return True

def check_if_username_is_registered(username):
    with open("users.json", "r+") as file:
            file_data = json.load(file)
            users = file_data['users']
            for user in users:
                if username == user["username"]:
                    return True
    return False

def check_if_imeil_is_registered(imeil):
    with open("users.json", "r+") as file:
            file_data = json.load(file)
            users = file_data['users']
            for user in users:
                if imeil == user["imeil"]:
                    return True         
    return False

def check_if_password_is_correct(password):
    # Min eight - 8, Max - 12, at least one uppercase letter, one lowercase letter and one number, example - Peturcho123;
    if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,12}$', password):
            return True
    return False

def check_if_sex_is_correct(sex):
    if sex == 'male' or sex == 'female' or sex == 'none':
        return True 
    return False

def check_if_birthday_is_correct(birthday):
    #dd/mm/yyyy or dd.mm.yyyy or dd-mm-yyyy  
    if re.match(r'^(?:0[1-9]|[12]\d|3[01])([\/.-])(?:0[1-9]|1[012])\1(19\d\d|20[01][0-9])$', birthday):  
        return True
    return False
