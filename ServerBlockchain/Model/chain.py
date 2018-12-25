from block import Block
import datetime
import hashlib
import json

class Chain:

    def __init__(self):
        self.blockchain = []
        genesysBlock = Block( 1 , 0 , 0)
        self.createBlock(genesysBlock)

    def createBlock(self , newBlock):
        self.blockchain.append(newBlock)

    def getPreviousBlock(self):
        return self.blockchain[len(self.blockchain) -1]

    def getAllBlock(self):
        for x in self.blockchain:
            print(x.toJSON())

