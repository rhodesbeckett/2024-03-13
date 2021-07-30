from bson.json_util import dumps
from bson.objectid import ObjectId


class Model():
    def __init__(self, collection):
        self.collection = collection

    def insert(self):
        matchComp = {
            "compDesc": {
                "title": "",
                "src": "",
                "editing": "",
                "time": {
                    "isChosen": False,
                    "firstHalf": {"min": None, "sec": None},
                    "secondHalf": {"min": None, "sec": None}
                }
            },
            "highlights": [],
            "testing": {
                "src": False,
                "halfTime": False,
                "highlights": False
            },
            "cutAndRender": {
                "canCut": False,
                "canRender": False,
                "cutProgress": 0,
                "renderProgress": 0
            }
        }
        return self.collection.insert_one(matchComp)

    def get(self, ID, key):
        comp = self.collection.find_one({"_id": ObjectId(ID)})
        return get_data(comp, key)

    def get_all(self):
        comps = self.collection.find({})
        return {"allComps": dumps(comps)}

    def delete_all(self):
        self.collection.delete_many({})

    def update(self, request, ID, key):
        new_property = {"$set": {key: get_property(request, ID, key)}}
        self.collection.update_one({"_id": ObjectId(ID)}, new_property)

    # controller part


# helper functions
def get_data(comp: object, key: str):
    keys = key
    result = {}
    if "." in key:
        keys = key.split(".")
        document = keys[0]
        key_object = keys[1]
        result[key_object] = dumps(comp[document][key_object])
    else:
        result[key] = dumps(comp[key])
    return result


def get_property(request, ID, key):
    if key == "cutAndRender.canCut" or key == "cutAndRender.canRender":
        try:
            response = request.get_json(force=True)
            return response
        except Exception as e:
            return False
    elif key == "cutAndRender.cutProgress" or key == "cutAndRender.renderProgress":
        """ .split("cutProgress=")[1] """
        return float(request.get_data(key).decode("UTF-8").split(f'{key}=')[1])
    else:
        return request.get_json(force=True)
