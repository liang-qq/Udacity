#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""
import os
import joblib
import sys
sys.path.append(os.path.abspath("C:\\Users\\liang\\Documents\\Udacity ML\\ud120-projects\\tools"))
from feature_format import featureFormat, targetFeatureSplit

data_dict = joblib.load(open("C:\\Users\\liang\\Documents\\Udacity ML\\ud120-projects\\final_project\\final_project_dataset.pkl", "rb") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list, sort_keys = "C:\\Users\\liang\\Documents\\Udacity ML\\ud120-projects\\tools\\python2_lesson13_keys.pkl")
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!  
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 42)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
print(accuracy)
