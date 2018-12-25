from flask import Flask , jsonify

app = Flask(__name__)
@app.route('/api/v1/genbook' , methods = ['GET'])
def homepage():
    response = {'message' : 'blockchain is working' ,
                'status_code' : 'success'}
    return jsonify(response) , 200


app.run(host='0.0.0.0' , port=5000)