import datetime
import hashlib
import json

class Block:

    def __init__(self , prevProof , previousHash):
        self.transaction = []
        self.prevProof = prevProof
        self.timestamp = str(datetime.datetime.now())
        self.previousHash = previousHash
        self.proof = self.proof_of_work

    def addTransaction(self , transactionChild):
        self.transaction.append(transactionChild)

    # def generateHash(self):

    def proof_of_work(self):
        newProof = 1
        checkProof = False
        while checkProof is False:
            hashOperation = hashlib.sha256(str(newProof**2 - self.prevProof**2).encode()).hexdigest()
            if hashOperation[:4] == '0000':
                checkProof = True
                print(hashOperation)
            else:
                newProof += 1
        
        print(newProof)
        return newProof
        