import datetime

class Book:

    def __init__(self , name , owner , typeBook , author):
        self.name = name
        self.owner = owner
        self.typeBook = typeBook
        self.author = author
        self.day = str(datetime.datetime.now())

    def setOwner(self , owner):
        self.owner = owner

    def setDay(self , dayAway):
        self.day = dayAway

    def toString(self):
        print(self.name + " " + self.owner + " " + self.typeBook + " " + self.author)
