import datetime

class Book:

    def __init__(self , name , owner , typeBook , author):
        self.name = name
        self.owner = owner
        self.typeBook = typeBook
        self.author = author
        # TODO set day by system datetime
        # self.day = str(datetime.datetime.now())
        self.day = 'test'

    def setOwner(self , owner):
        self.owner = owner

    def setDay(self , dayAway):
        self.day = dayAway

    def toString(self):
        return self.name + " " + self.owner + " " + self.typeBook + " " + self.author
