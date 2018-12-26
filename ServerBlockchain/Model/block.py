import datetime
import hashlib
import json

class Block:

    # initialize block 
    # @param prevProof: the proof of work (PoW) of previous block
    # @param prevHash: the hash of previous block
    # @param index: block 's position in chain 
    def __init__(self , prevProof , previousHash , index):
        self.index = index
        self.transaction = []
        self.prevProof = prevProof
        self.timestamp = str(datetime.datetime.now())
        self.previousHash = previousHash
        self.proof = self.mining()
        self.generateHash()

    # add a transaction
    # @param transactionChild: the transaction will be added to list
    def addTransaction(self , transactionChild):
        self.transaction.append(transactionChild)

    # def generateHash(self):

    # mining proof of work 
    def mining(self):
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
        return (str(self.proof) + "\n" + self.previousHash + "\n")
        
    # print all traction in list
    def getAllTransaction(self):
        for x in self.transaction:
            print(x.toString())

    # generate hash from data in block
    def generateHash(self):
        block = {
            'index': self.index,
            'transaction': self.transaction,
            # TODO set timestamp by system datetime
            'timestamp' : self.timestamp,
            'previousHash': self.previousHash,
            'proof': self.proof
        }

        jsonString = json.dumps(block , sort_keys = True).encode()
        print(jsonString)
        self.hash = hashlib.sha256(jsonString).hexdigest()
        print(self.hash)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)