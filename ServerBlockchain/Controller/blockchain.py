from flask import Flask , jsonify
import pymongo

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["GenBook"]
blockchainDB = mydb["BlockchainDB"]

@app.route('/api/v1/genbook' , methods = ['GET'])
def homepage():
    response = {'message' : 'blockchain is working' ,
                'status_code' : 'success'}
    return jsonify(response) , 200


@app.route('/api/v1/blockchain' , methods = ['GET'])
def getBlockchain():
    data = blockchainDB.find()
    chain = []
    for x in blockchainDB.find({} , {"_id": 0}):
        chain.append(x)
    response = {'message' : 'blockchain is working' ,
                'data' : chain}
    return jsonify(response) , 200
    

app.run(host='0.0.0.0' , port=5000)