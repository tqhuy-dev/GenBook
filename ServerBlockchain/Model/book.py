import datetime

class Book:

    # initialize class
    # @param name:  name of book
    # @param owner: the person who is keeping this book
    # @param typeBook: typical of book (like skill , education , ditective,... )
    # @param author: the person who wrote this book  
    def __init__(self , name , owner , typeBook , author):
        self.name = name
        self.owner = owner
        self.typeBook = typeBook
        self.author = author
        # TODO set day by system datetime
        # self.day = str(datetime.datetime.now())
        self.day = 'test'

    # set name of owner
    # @param newOwner: name of person who want to get this book
    def setNewOwner(self , newOwner):
        self.owner = newOwner

    # set dayAway
    # @param dayAway: the day this book is take away
    def setDayAway(self , dayAway):
        self.day = dayAway

    # print data of this book
    def toString(self):
        return self.name + " " + self.owner + " " + self.typeBook + " " + self.author
