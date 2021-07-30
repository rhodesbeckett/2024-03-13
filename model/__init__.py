import pymongo


def factory_collection():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["videosdb"]
    collection = mydb["matchCompilations"]
    return collection
