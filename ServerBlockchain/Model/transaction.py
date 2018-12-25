import datetime
from book import Book
import json

class Transaction:

    def __init__(self , owner , receiver):
        self.owner = owner
        self.receiver = receiver
        # TODO set day by system datetime
        # self.day = str(datetime.datetime.now())
        self.day = 'test'

    def setBook(self , book):
        self.book = book
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def toString(self):
        return (self.owner + " " + self.receiver + " " + self.book.toString())