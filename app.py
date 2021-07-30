from flask import Flask, jsonify, request
from flask_cors import CORS
from bson.json_util import dumps
from model import factory_collection
from model.Model import Model
from controller.Controller import Controller

app = Flask(__name__)
collection = factory_collection()
model = Model(collection)
controller = Controller(collection)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/insert', methods=['GET'])
def insert():
    result = model.insert()
    return jsonify({'mcID': str(result.inserted_id)})


@app.route('/getAll', methods=['GET'])
def get_all():
    return jsonify(model.get_all())


@app.route('/deleteAll', methods=['GET'])
def deleteAll():
    model.delete_all()
    return jsonify({'msg': "success"})


@app.route('/update/<ID>/<key>', methods=['POST'])
def update(ID, key):
    model.update(request, ID, key)
    return jsonify({'msg': 'success'})


@app.route('/get/<ID>/<key>', methods=['GET'])
def get(ID, key):
    result = model.get(ID, key)
    return jsonify(result)


@app.route('/test/<ID>', methods=['GET'])
def test(ID):
    test_response = controller.test(ID)
    return jsonify({'testing': dumps(test_response)})


@app.route('/getPhoto/<ID>/<minute>/<second>')
def get_photo(ID, minute, second):
    file_name = controller.get_photo(ID, int(minute), int(second))
    return jsonify({"imgSrc": f'http://localhost:5000/static/{file_name}'})


@app.route('/cut/<ID>', methods=['GET'])
def cut(ID):
    controller.cut(ID)
    return jsonify({'msg': 'success'})


@app.route('/render/<ID>', methods=['GET'])
def render(ID):
    controller.render(ID)
    return jsonify({'msg': "success"})


@app.route('/mergeVideos/<ID>', methods=['GET'])
def merge_videos(ID):
    controller.merge_videos(ID)
    return jsonify({"msg": "success"})


if __name__ == "__main__":
    app.run(debug=True)
