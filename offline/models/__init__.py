from models.Model import Model
def factory_model():
    if Model.counter == 0:
        return Model()