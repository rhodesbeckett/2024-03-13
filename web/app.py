from flask import Flask,jsonify,request
from flask_cors import CORS
import pymongo
from bson.json_util import dumps
import json
from bson.objectid import ObjectId
import requests
from model import Model

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["videosdb"]
collection = mydb["matchCompilations"]

app = Flask(__name__)
model = Model(collection)
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
        "highlights": [{"min":None,"sec":None,"toAdd":None,"id":0}],
        "testing": {
                "src":False,
                "halfTime":False,
                "highlights":False
        },
        "canCut": False,
        "canRender": False,
    }
    matchCompID = collection.insert_one(matchComp)
    print(matchCompID.inserted_id)

    return jsonify({"mcID":f'{matchCompID.inserted_id}'})

""" @app.route('/update/<ID>/canCut',methods=["POST"])
def updateCanCut(ID):
    return jsonify({"msg":"success"}) """

@app.route('/update/<ID>/<key>',methods=["POST"])
def update(ID,key):
    new_property = {"$set":{key:get_value(request,key)}}
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
    model.set_id(ID)
    model.test_all()
    return jsonify({"test":model.testResponse})

    """ result = collection.find_one({"_id":ObjectId(ID),}) """
    """ return jsonify({"test":dumps(result["testing"])}) """

@app.route('/getPhoto/<minute>/<second>')
def get_photo(minute,second):
    row = {"min":int(minute),"sec":int(second)}
    model.test_all()
    file_name = model.test_photo(row)
    return jsonify({"imgSrc":f'http://localhost:5000/static/{file_name}'})

@app.route('/getCanCut/<ID>',methods=["GET"])
def get_can_cut(ID):
    result = collection.find_one({"_id":ObjectId(ID),})
    return jsonify({"canCut":dumps(result["canCut"])})

@app.route('/cut/<ID>',methods=["GET"])
def cut(ID):
    model.set_id(ID)
    model.cut_all()
    return jsonify({'test': False})

@app.route('/render/<ID>', methods= ["GET"])
def render(ID):
    model.set_id(ID)
    model.test_all()
    model.make_txt_file()
    model.render()
    return jsonify({'render': True})

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

def get_value(request,key):
    if key == "canCut":
        try:
            response = request.get_json(force=True)
            return response
        except:
            print("error")
            return False
    else:
        return request.get_json(force=True)

if __name__ == "__main__":
    app.run(debug=True)