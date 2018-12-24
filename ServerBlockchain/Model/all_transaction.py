import datetime

class AllTransaction:

    def __init__(self):
        thisDay = datetime.datetime.now()
        self.day = thisDay.strftime("%x")
        self.transaction = []

    def addTransaction(self , transaction):
        self.transaction.append(transaction)

