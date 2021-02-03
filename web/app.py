from flask import Flask,jsonify,request
from flask_cors import CORS
import pymongo
from bson.json_util import dumps
import json
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["videosdb"]
collection = mydb["matchCompilations"]

app = Flask(__name__)
""" mongo = PyMongo(app) """

CORS(app,resources={r'/*': {'origins': '*'}})

@app.route('/testJSON',methods=['POST'])
def testJSON():
    print(request.get_json(force=True))
    print("testJSON")
    return jsonify({"poruka":"Hello World!"})

@app.route('/insert',methods=['GET'])
def insert():
    matchComp = {
        "compDesc": {
        "title": "",
        "src": "",
        "editing": "",
        "time": {
            "isChosen": False,
            "firstHalf": {"min": None,"sec":None},
            "secondHalf": {"min": None,"sec":None}
            }
        },
        "highlights": [{"min":None,"sec":None,"toAdd":None}],
        "testing": {
                "src":False,
                "halfTime":False,
                "highlights":False
        } 
    }
    matchCompID = collection.insert_one(matchComp)
    print(matchCompID.inserted_id)

    return jsonify({"mcID":f'{matchCompID.inserted_id}'})

@app.route('/update/<ID>/<key>',methods=["POST"])
def update(ID,key):
    new_property = {"$set":{key:request.get_json(force=True)}}
    collection.update_one({"_id":ObjectId(ID)},new_property)
    return jsonify({"msg":"success"})

@app.route('/getMC/<ID>',methods=["GET"])
def get_mc(ID):
    result = collection.find_one({"_id":ObjectId(ID),})
    return jsonify({"compDesc":dumps(result["compDesc"])})

@app.route('/getHighlights/<ID>',methods=["GET"])
def get_highlights(ID):
    result = collection.find_one({"_id":ObjectId(ID),})
    return jsonify({"highlights":dumps(result["highlights"])})

@app.route('/getTest/<ID>')
def get_test(ID):
    result = collection.find_one({"_id":ObjectId(ID),})
    return jsonify({"test":dumps(result["testing"])})

@app.route('/getPhoto/<id>')
def get_photo(id):
    return jsonify({"msg":"success"})

@app.route('/getCutProgress<id>')
def get_cut_progress(id):
    return jsonify({"msg":"success"})

@app.route('/getRenderProgress<id>')
def get_render_progress(id):
    return jsonify({"msg":"success"})

@app.route('/getAll',methods=["GET"])
def get_all():
    lista = collection.find({})
    return jsonify({"allComps":dumps(lista)})

@app.route('/deleteAll',methods=["GET"])
def deleteAll():
    collection.delete_many({})
    return jsonify({"msg":"success"})

if __name__ == "__main__":
    app.run(debug=True)