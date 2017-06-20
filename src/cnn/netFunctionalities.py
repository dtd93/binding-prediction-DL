from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import numpy
import os


def loadModelFromFile(file_model, file_weights):
    json_file = open(file_model, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights(file_weights)
    print("It is necessary the compile method before fit")
    return loaded_model


def evaluateModel(model, X, Y):
    score = model.evaluate(X, Y, verbose=0)
    print("Acc = " + str(score[1]*100))
    print("Rec = " + str(score[2]))


def saveModelToFile(path, model):
    model_json = model.to_json()
    with open(path+"model.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights(path+"model.h5")
    print("Saved model to disk")
