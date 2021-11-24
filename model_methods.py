import pandas as pd
import pickle
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier

def predict(arr):
    with open('random_forest_model_1.pkl' , 'rb') as f:
        model = pickle.load(f)

    result = model.predict(arr)

    if result[0] == 0:
        result = "Customer will continue with the service"

    else:
        result = "Customer will unsubscribe the service"

    return result
