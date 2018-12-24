import datetime
import hashlib
import json

class User:

    def __init__(self, name , age , address , touchID):
        self.name = name 
        self.age = age
        self.address = address
        self.date = str(datetime.datetime.now())
        self.touchID = touchID

    def addBook(self , book):
        self.books = []
        self.books.append(book)
    # def generateKey():

