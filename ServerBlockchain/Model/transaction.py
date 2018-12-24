import datetime
from book import Book

class Transaction:

    def __init__(self , owner , receiver):
        self.owner = owner
        self.receiver = receiver
        self.day = str(datetime.datetime.now())

    def setBook(self , book):
        self.book = book
        
    def toString(self):
        print(self.owner + " " + self.receiver + " " + self.book.author)