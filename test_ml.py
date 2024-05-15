import pytest
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model
import os
import pandas as pd

# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_model_type():
    """
    # This test will check if the model is a Random Forest
    """
    x_data = [[9,5,2],[1,5,7]]
    y_data = ['a', 'b']
    model = train_model(x_data,y_data)
    assert isinstance(model, RandomForestClassifier)


# TODO: implement the second test. Change the function name and input as needed
def test_input_data_length():
    """
    # This tests if the input length is great then 3,000
    """
    data_path = os.path.join("data", "census.csv")
    input = pd.read_csv(data_path)
    
    assert len(input) > 2500
        


# TODO: implement the third test. Change the function name and input as needed
def test_all_features():
    """
    # This will ensure that all the features are present in the data set
    """
    data_path = os.path.join("data", "census.csv")
    data = pd.read_csv(data_path)

    feature_set = {
        'age', 
        'workclass', 
        'fnlgt', 
        'education', 
        'education-num', 
        'marital-status', 
        'occupation', 
        'relationship', 
        'race', 
        'sex', 
        'capital-gain', 
        'capital-loss', 
        'hours-per-week', 
        'native-country', 
        'salary'
    }

    assert set(data.columns) == feature_set
