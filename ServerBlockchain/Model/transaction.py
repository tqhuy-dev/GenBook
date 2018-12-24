import datetime

class Transaction:

    def __init__(self , owner , receiver):
        self.owner = owner
        self.receiver = receiver
        self.day = str(datetime.datetime.now())