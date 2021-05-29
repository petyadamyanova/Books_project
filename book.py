import re
import json

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
    if year > 1500 and year < 2021:
        return True
    return False

"""
def ckeck_if_ISBN_is_correct(ISBN):   #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if re.match(r'^(?:ISBN(?:-10)?:?\ )?(?=[0-9X]{10}$|(?=(?:[0-9]+[-\ ]){3})[-\ 0-9X]{13}$)[0-9]{1,5}[-\ ]?[0-9]+[-\ ]?[0-9]+[-\ ]?[0-9X]$', ISBN):  
        return True
    return False
"""

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
