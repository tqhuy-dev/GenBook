from block import Block
import datetime
import hashlib
import json

class Chain:

    # initialize blockchain
    def __init__(self):
        self.blockchain = []
        genesysBlock = Block( 1 , 0 , 0)
        self.createBlock(genesysBlock)

    # add new block in chain
    def createBlock(self , newBlock):
        self.blockchain.append(newBlock)

    # return the last block in chain
    def getPreviousBlock(self):
        return self.blockchain[len(self.blockchain) -1]

    # print all block in chain
    def getAllBlock(self):
        for x in self.blockchain:
            print(x.toJSON())

