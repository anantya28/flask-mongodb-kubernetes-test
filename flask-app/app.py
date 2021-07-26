from flask import Flask, jsonify
from flask_pymongo import PyMongo
import os
import socket

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://root:pass@test_mongo:27017/animal_db?authSource=admin"
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
def ping_server():
    hostname = socket.gethostname()
    return "Welcome to the world of animals running on {}.".format(hostname)

@app.route('/animals')
def get_stored_animals():
    _animals = mongo.db.animal_tb.find()
    animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
    return jsonify({"animals": animals})
    
if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
