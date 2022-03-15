#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""
import os
import joblib
import sys
sys.path.append(os.path.abspath("C:\\Users\\liang\\Documents\\Udacity ML\\ud120-projects\\tools"))
from feature_format import featureFormat, targetFeatureSplit

data_dict = joblib.load(open("C:\\Users\\liang\\Documents\\Udacity ML\\ud120-projects\\final_project\\final_project_dataset.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list, sort_keys = "C:\\Users\\liang\\Documents\\Udacity ML\\ud120-projects\\tools\\python2_lesson14_keys.pkl")
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 42)
print(len(features_test), sum(x for x in labels_test if x == 1))
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
index_list = []
for i in range(len(pred)):
    if pred[i] == 1 and labels_test[i] == 1:
        index_list.append(i)

from sklearn.metrics import accuracy_score, precision_score, recall_score
accuracy = accuracy_score(pred, labels_test)
print(accuracy, len(pred), index_list)
precision = precision_score(labels_test, pred)
print(precision)
recall = recall_score(labels_test, pred)
print(recall)