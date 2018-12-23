import datetime
import hashlib
import json
from flask import Flask ,  jsonify


class BlockData:
    def __init__(self , index , timespamp , prev_proof , previous_hash , data):
        self.index = index
        self.timespamp = timespamp
        self.proof = self.proof_of_work(prev_proof)
        self.previous_hash = previous_hash
        self.data = data

    def proof_of_work(self , previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
                print(hash_operation)
            else:
                new_proof += 1
        
        print(new_proof)
        return new_proof


class Block:
    def __init__(self, blockdata):
        self.block = { 'index': blockdata.index ,
                  'timestamp': "101010",
                  'proof': blockdata.proof ,
                  'previous_hash':blockdata.previous_hash}

        jsonString = json.dumps(self.block , sort_keys = True).encode()
        self.hash = hashlib.sha256(jsonString).hexdigest()


blockdata  = BlockData(1,str(datetime.datetime.now()), 1321 , '0' , 'Huy')
# print(blockdata)
block = Block(blockdata)
print(block.hash)