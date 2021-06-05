import re
import json
from book import *
from user import *

class Book():
    def __init__(self, author, title, genre, published_year, ISBN, series, num_in_series, pages, id_):
        #автор, заглавие, жарн, година на издаване, isbn, страници, поредица(да/не))
        self.title = title
        self.author = author
        self.genre = genre
        self.published_year = published_year
        self.ISBN = ISBN
        self.pages = pages
        self.series = series
        self.num_in_series = num_in_series
        self.id = id_   
    def add_to_file(self, ):
        data = {
            'author' : self.author,
            'title' : self.title,
            'genre' : self.genre,
            'published_year' : self.published_year,
            'ISBN' : self.ISBN,
            'series' : self.series,
            'num_in_series' : self.num_in_series,
            'pages' : self.pages,
            'id' : self.id,
            'rate': [],
            'comment': []
        }
        with open("books.json", "r") as file:
            file_data = json.load(file)
        with open("books.json", "w") as file:
            file_data['books'].append(data)
            json.dump(file_data, file)
    def print_book_info(self):
        print("\n-------------------------------")
        print(f"Book's title: {self.title}")
        print(f"Book's author: {self.author}")
        print(f"Book's id: {self.id}")
        print("-------------------------------\n")
        

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


def add_book():
    #author, title, genre, published_year, ISBN, series, num_in_series, pages, id_
    title = input("Enter book's title: ")
    while check_if_book_is_registered(title) == False:
        title = input("This book is already added! Enter new book title: ")
    author = input("Enter book's author: ")
    genre = input("Enter book's genre: ")
    published_year = input("Enter book's published year: ")
    while ckeck_if_published_year_is_correct(published_year) == False:
        published_year = input("Published year is not valid! Try again: ")
    ISBN = input("Enter ISBN number: ")
    while ckeck_if_ISBN_is_correct(ISBN) == False:
        print("ISBN like these: 978-123-456-789-0 , 978-1234-567890 , 9781234567890")
        ISBN = input("ISBN number is not correct! Try again: ")
    series = input("Enter True - if the book is in series or False - if book isn't in series: ")
    while ckeck_if_series_are_correct(series) == False:
        series = input("You have to enter True - if the book is in series or False - if book isn't in series: ")
    num_in_series = input("Enter book's number in series !If the book is not in series enter 0! : ")
    while check_if_num_in_series_is_correct(int(num_in_series)) == False:
        num_in_series = input("Your number is not valid! Enter book's number in series !If the book is not in series enter 0! : ")
    pages = input("Enter book's pages: ")
    while ckeck_if_pages_are_correct(int(pages)) == False:
        pages = input("Enter valid pages: ")
    # id_
    try:
        book_id = open("id.txt", 'r')
        id_ = int(book_id.readline()) + 1
        book_id.close()
        b = Book(author, title, genre, published_year, ISBN, series, num_in_series, pages, id_)
        b.add_to_file()
        book_id = open("id.txt", 'w')
        book_id.write(str(id_))
    except ValueError:
        book_id.close()
        print("The id have to be int")
    except:
        book_id.close()
        print("Error")
    else:
        print("Uspeh")

def sign_up():
    username = input("- alowed symbols , min -  8 symbols, max - 20 symbols , example - petidamm2006, ivan_georgiev...  Enter username: ")
    while check_if_username_is_taken(username) == False:
        username = input("This username is already taken ili ima greshka! Enter new username: ")
    imeil = input("Enter email: ")
    while check_if_imeil_is_taken(imeil) == False:
        imeil = input("This imeil is already taken! Enter new imeil: ")
    password = input("Enter password: ")
    while check_if_password_is_correct(password) == False:
        password = input("This password is not valid.[ Min - 8 characters, Max - 12 characters, at least one uppercase letter, one lowercase letter and one number] ! Try again: ")
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    sex = input("Enter sex: ")
    while check_if_sex_is_correct(sex) == False:
        sex = input("You can enter only male, female or none! Try again: ")
    birthday = input("Enter birthday: ")
    while check_if_birthday_is_correct(birthday) == False:
        birthday = input("You have to enter your birthday in this format : dd/mm/yyyy or dd.mm.yyyy or dd-mm-yyyy. Try again: ")
    u = User(username, imeil, password, name, surname, sex, birthday)
    u.add_to_file()
    print("Uspeh")
    return u
    
def sign_in():
    rev_counter = 3
    imeil_or_username = input("Enter 1 if you want to sign in with imeil or 2 for username: ")
    while imeil_or_username != "1" and imeil_or_username != "2":
        imeil_or_username = input("Press 1 to sign in with imeil or 2 for username: ")
    if imeil_or_username == "1":
        imeil = input("Enter email: ")
        while check_if_imeil_is_registered(imeil) == False:
            imeil = input("This imeil is invalid! Try again: ")
        password = input("Enter password: ")
        with open("users.json", "r+") as file:
            file_data = json.load(file)
            users = file_data['users']
            for user in users:
                if imeil == user["imeil"]:
                    while password != user["password"]:
                        password = input(f"Password is wrong!You have only {rev_counter} tries more! Try again: ")
                        rev_counter = rev_counter - 1 
                        if rev_counter == 0:
                            return
                    print("Uspeh")
                    return user
    elif imeil_or_username == "2":
        username = input("- alowed symbols , min -  8 symbols, max - 20 symbols , example - petidamm2006, ivan_georgiev...  Enter username: ")
        while check_if_username_is_registered(username) == False:
            username = input("This username is invalid! Try again: ")
        password = input("Enter password: ")
        with open("users.json", "r+") as file:
            file_data = json.load(file)
            users = file_data['users']
            for user in users:
                    if username == user["username"]:
                        while password != user["password"]:
                            password = input(f"Password is wrong! You have only {rev_counter} tries more!  Try again: ")
                            rev_counter = rev_counter - 1 
                            if rev_counter == 0:
                                return
                        print("Uspeh")
                        return user

def print_all_books():
    with open("books.json", "r+") as file:
            file_data = json.load(file)
            books = file_data['books']
            for book in books:
                new_book = Book(book["author"], book["title"], book["genre"], book["published_year"], book["ISBN"], book["series"], book["pages"], book["num_in_series"], book["id"])
                new_book.print_book_info()

def print_book_with_id(id_num):
    flag = 0
    with open("books.json", "r+") as file:
            file_data = json.load(file)
            books = file_data['books']
            for book in books:
                if id_num == book["id"]:
                    print("\n-------------------------------")
                    print(f"Book's title: {book['title']}")
                    print(f"Book's author: {book['author']}")
                    print(f"Book's id: {book['id']}")
                    print(f"Book's genre: {book['genre']}")
                    print(f"Book's published_year: {book['published_year']}")
                    print(f"Book's num_in_series: {book['num_in_series']}")
                    print(f"Book's pages: {book['pages']}")
                    if len(book['rate']) > 0:
                        sum_ = 0  
                        for rate in book['rate']:
                            sum_ = sum_ + (int(list(dict.values(rate))[0]))
                        print(f"Book's rated: {sum_/len(book['rate'])}")
                    else:
                        print(f"Book's rated: {book['rate']}")
                    if len(book['comment']) > 0:
                        print(f"Book's comment:\n")   
                        for comment in book['comment']:
                            print(comment)   
                    else:
                        print(f"Book's comment: {book['comment']}")
                    print("-------------------------------\n")
                    flag = 1
    if flag == 0:
        print(f"There is not book with this id ({id_num})!")
            

def add_to_list(num_list, id_num, u):
    wishlist = []
    readinglist = []
    readedlist = []
    with open("users.json", "r+") as file:
        file_data = json.load(file)
        users = file_data['users']
        for user in users:
            if user["username"] == u["username"]:
                wishlist = user['wishlist']
                readinglist = user['readinglist']
                readedlist = user['readedlist']
    if num_list == 1:
        if not(id_num in wishlist):
            wishlist.append(id_num)
        else:
            print("This book is already aded!")
    if num_list == 2:
        if not(id_num in readinglist):
            readinglist.append(id_num)
        else:
            print("This book is already aded!")
    if num_list == 3:
        if not(id_num in readedlist):
            readedlist.append(id_num)
        else:
            print("This book is already aded!")
    with open("users.json", "w") as file:
        json.dump(file_data, file)
    
def see_list(num_list, u):
    wishlist = []
    readinglist = []
    readedlist = []
    with open("users.json", "r+") as file:
        file_data = json.load(file)
        users = file_data['users']
        for user in users:
            if user["username"] == u["username"]:
                wishlist = user['wishlist']
                readinglist = user['readinglist']
                readedlist = user['readedlist']
    if num_list == 1:
        print(wishlist)
    if num_list == 2:
        print(readinglist)
    if num_list == 3:
        print(readedlist)

def remove_from_list(num_list, id_num, u):
    wishlist = []
    readinglist = []
    readedlist = []
    with open("users.json", "r+") as file:
        file_data = json.load(file)
        users = file_data['users']
        for user in users:
            if user["username"] == u["username"]:
                wishlist = user['wishlist']
                readinglist = user['readinglist']
                readedlist = user['readedlist']
    if num_list == 1:
        if id_num in wishlist:
            wishlist.remove(id_num)
    if num_list == 2:
        if id_num in wishlist:
            readinglist.remove(id_num)
    if num_list == 3:
        if id_num in wishlist:
            readedlist.remove(id_num)
    with open("users.json", "w") as file:
        json.dump(file_data, file)

def rate_book(id_num, rate, u):
    with open("books.json", "r+") as file:
        file_data = json.load(file)
        books = file_data["books"]
        for book in books:
            if book["id"] == id_num:
                book["rate"].append({u["username"]: rate})
    with open("books.json", "w") as file:
        json.dump(file_data, file)

def comment_book(id_num, comment, u):
    with open("books.json", "r+") as file:
        file_data = json.load(file)
        books = file_data["books"]
        for book in books:
            if book["id"] == id_num:
                book["comment"].append({u["username"]: comment})
    with open("books.json", "w") as file:
        json.dump(file_data, file)

first_step = input("Press 1 for sign up or 2 for sign in: ")

while first_step != "1" and first_step != "2":
    first_step = input("Press 1 for sign up or 2 for sign in: ")

if first_step == "1":
    user = sign_up()
else:
    user = sign_in()

while True:
    print("Press 1 to see all books")
    print("Press 2 to see book info id")
    print("Press 3 to add book")
    print("Press 4 to see/add/removw from your wish book list")
    print("Press 5 to see/add/remove your reading book list")
    print("Press 6 to see/add/remove/rate/review your read book list")
    print("Press 7 to rate a book")
    print("Press 8 to make a comment for book")
    print("Press 9 to exit")
    second_step = input("Enter number: ")
    if second_step == "1":
        print_all_books()
    elif second_step == "2":
        id_num = input("Enter id number of book you want to see: ")
        try:
            id_num = int(id_num)
        except ValueError:
            print("Id number have to be int!")
        else:        
            print_book_with_id(id_num)
    elif second_step == "3":
        add_book()
    elif second_step == "4":
        print("Press 1 to see your book wishlist ")
        print("Press 2 to add book to your wishlist")
        print("Press 3 to remove book from your wishlist")
        wishlist = input("Enter number: ")
        while wishlist != '1' and wishlist != '2' and wishlist != '3':
            wishlist = input("You can enter only number betweem 1-3 (1 - see, 2 - add, 3 - remove)")
        if wishlist == '1':
            see_list(1, user)
        elif wishlist == '2':
            book_id = input("Enter book_id of the book: ")
            while check_if_id_is_valid(book_id) == False:
                book_id = input("You have entered wrong id! Try again: ")
            add_to_list(1, book_id, user)
        else:
            pass
    elif second_step == "5":
        print("Press 1 to see your reading book list ")
        print("Press 2 to add book to your reading list")
        print("Press 3 to remove book from your reading list")
        wishlist = input("Enter number: ")
        while wishlist != '1' and wishlist != '2' and wishlist != '3':
            wishlist = input("You can enter only number betweem 1-3 (1 - see, 2 - add, 3 - remove)")
        if wishlist == '1':
            see_list(2, user)
        elif wishlist == '2':
            book_id = input("Enter book_id of the book: ")
            while check_if_id_is_valid(book_id) == False:
                book_id = input("You have entered wrong id! Try again: ")
            add_to_list(2, book_id, user)
        else:
            book_id = input("Enter book_id of the book: ")
            while check_if_id_is_valid(book_id) == False:
                book_id = input("You have entered wrong id! Try again: ")
            remove_from_list(1, book_id, user)
    elif second_step == "6":
        print("Press 1 to see your readed book list ")
        print("Press 2 to add book to your readed book list")
        print("Press 3 to remove book from your readed book list")
        wishlist = input("Enter number: ")
        while wishlist != '1' and wishlist != '2' and wishlist != '3':
            wishlist = input("You can enter only number betweem 1-3 (1 - see, 2 - add, 3 - remove)")
        if wishlist == '1':
            see_list(3, user)
        elif wishlist == '2':
            book_id = input("Enter book_id of the book: ")
            while check_if_id_is_valid(book_id) == False:
                book_id = input("You have entered wrong id! Try again: ")
            add_to_list(3, book_id, user)
        else:
            book_id = input("Enter book_id of the book: ")
            while check_if_id_is_valid(book_id) == False:
                book_id = input("You have entered wrong id! Try again: ")
            remove_from_list(3, book_id, user)
    elif second_step == '7':
        book_id = input("Enter book_id of the book: ")
        while check_if_id_is_valid(book_id) == False:
            book_id = input("You have entered wrong id! Try again: ")
        rate = input(f"Enter your rate for {book_id}! Enter number between 0 - 10: ")
        while int(rate) < 0 or int(rate) > 10:
            rate = input("Enter valid number(between 0 - 10): ")
        rate_book(int(book_id), rate, user)
    elif second_step == "8":
        book_id = input("Enter book_id of the book: ")
        while check_if_id_is_valid(book_id) == False:
            book_id = input("You have entered wrong id! Try again: ")
        comment = input(f"Enter your comment for {book_id}: ")
        comment_book(int(book_id), comment, user)
    elif second_step == "9":
        break






    
