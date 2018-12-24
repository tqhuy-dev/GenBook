class Book:

    def __init__(self , name , owner , typeBook , author , day):
        self.name = name
        self.owner = owner
        self.typeBook = typeBook
        self.author = author
        self.day = day

    def setOwner(self , owner):
        self.owner = owner

    def setDay(self , day):
        self.day = day

    