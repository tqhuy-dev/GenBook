import datetime
from book import Book
import json


class Transaction:

    # initialize class
    # @param owner: person who is keeping books
    # @param receiver: person who want to get books
    def __init__(self , owner , receiver):
        self.owner = owner
        self.receiver = receiver
        # TODO set day by system datetime
        self.day = str(datetime.datetime.now())
        # self.day = 'test'

    # set the book to create a transaction
    def setBook(self , book):
        self.book = book
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def toString(self):
        return (self.owner + " " + self.receiver + " " + self.book.toString())