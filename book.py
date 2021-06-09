import re
import json

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
        


def check_if_book_is_registered(title):
    with open("books.json", "r") as file:
            file_data = json.load(file)
            books = file_data['books']
            for book in books:
                if title == book["title"]:
                    return False
    return True

def check_if_id_is_valid(id_num):
    with open("books.json", "r") as file:
            file_data = json.load(file)
            books = file_data['books']
            for book in books:
                if id_num == str(book["id"]):
                    return True
    return False

def ckeck_if_published_year_is_correct(year):
    try:
        year = int(year)
    except ValueError:
        print("\nError in published year! Have to be number! \n")
        return False
    if year > 1500 and year < 2021:
        return True
    return False

def ckeck_if_ISBN_is_correct(ISBN):   
    if re.match(r'978(?:-?\d){10}', ISBN):  
        return True
    return False


def ckeck_if_pages_are_correct(pages):
    if pages > 1 and pages < 9999:
        return True
    return False

def ckeck_if_series_are_correct(s):
    if s == "True" or s == "False":
        return True
    return False
        
def check_if_num_in_series_is_correct(num):
    if num >= 0 and num < 1000:
        return True
    return False 
