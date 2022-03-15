#!/usr/bin/python3
import os
import joblib
import sys
import matplotlib.pyplot
sys.path.append(os.path.abspath("C:\\Users\\liang\\Documents\\Udacity ML\\ud120-projects\\tools"))
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = joblib.load( open("C:\\Users\\liang\\Documents\\Udacity ML\\ud120-projects\\final_project\\final_project_dataset.pkl", "rb") )
data_dict.pop("TOTAL")
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus)
matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

for key, value in data_dict.items():
    if value["bonus"] == data.max():
        print(key)

for key, value in data_dict.items():
    if value["bonus"] != "NaN" and value["salary"] != "NaN":
        if int(value["bonus"]) > 5000000 and int(value["salary"]) > 1000000:
            print(key)