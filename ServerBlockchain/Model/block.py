import datetime
import hashlib
import json

class Block:

    def __init__(self , prevProof , previousHash , index):
        self.index = index
        self.transaction = []
        self.prevProof = prevProof
        self.timestamp = str(datetime.datetime.now())
        self.previousHash = previousHash
        self.proof = self.proof_of_work()

    def addTransaction(self , transactionChild):
        self.transaction.append(transactionChild.toJSON())

    # def generateHash(self):

    def proof_of_work(self):
        newProof = 1
        checkProof = False
        while checkProof is False:
            hashOperation = hashlib.sha256(str(newProof**2 - self.prevProof**2).encode()).hexdigest()
            if hashOperation[:4] == '0000':
                checkProof = True
                # print(hashOperation)
            else:
                newProof += 1
        
        # print(newProof)
        return newProof

    def toString(self):
        return (str(self.proof) + " " + self.previousHash)
        
    def getAllTransaction(self):
        for x in self.transaction:
            print(x.toString())

    def generateHash(self):
        block = {
            'index': self.index,
            'transaction': self.transaction,
            # TODO set timestamp by system datetime
            'timestamp' : 'test',
            'previousHash': self.previousHash,
            'proof': self.proof
        }

        jsonString = json.dumps(block , sort_keys = True).encode()
        print(jsonString)
        self.hash = hashlib.sha256(jsonString).hexdigest()
        print(self.hash)