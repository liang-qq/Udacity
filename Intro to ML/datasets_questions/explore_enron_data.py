#!/usr/bin/python3

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import joblib
import sys

from numpy import quantile
sys.path.append("C:\\Users\\liang\\Documents\\Udacity ML\\ud120-projects\\final_project")
enron_data = joblib.load(open("C:\\Users\\liang\\Documents\\Udacity ML\\ud120-projects\\final_project\\final_project_dataset.pkl", "rb"))
print(len(enron_data.keys()))
print(len(list(enron_data.values())[0]))
count = 0
for key, value in enron_data.items():
    if enron_data[key]["poi"] == 1:
        count += 1
print(count)

poi_names_txt = open("C:\\Users\\liang\\Documents\\Udacity ML\\ud120-projects\\final_project\\poi_names.txt", "r").read()
poi_names_txt = poi_names_txt.split("\n")
poi_names = []
for item in poi_names_txt:
    name = item.split(")")
    if len(name) > 1:
        poi_names.append(name[1].strip(" "))
print(len(poi_names))
#from poi_email_addresses import *
#print(len(poiEmails()))
print(enron_data["PRENTICE JAMES"])
print(enron_data["PRENTICE JAMES"]["total_stock_value"])

print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

print(enron_data["LAY KENNETH L"]["total_payments"])
print(enron_data["SKILLING JEFFREY K"]["total_payments"])
print(enron_data["FASTOW ANDREW S"]["total_payments"])

quantile_salary = [x for x,y in enron_data.items() if y["salary"] != "NaN"]
print(len(quantile_salary))
known_email = [x for x,y in enron_data.items() if y["email_address"] != "NaN"]
print(len(known_email))

sys.path.append("C:\\Users\\liang\\Documents\\Udacity ML\\ud120-projects\\tools")
from feature_format import featureFormat, targetFeatureSplit

missing_payments = [x for x,y in enron_data.items() if y["total_payments"] == "NaN"]
print(len(missing_payments), len(missing_payments)/len(enron_data))

poi_missing_payments = [x for x,y in enron_data.items() if y["total_payments"] == "NaN" and y["poi"]]
print(len(poi_missing_payments), len(poi_missing_payments)/len(enron_data))

enron_data_total = len(enron_data) + 10
missing_payments_total = len(missing_payments) + 10
print(missing_payments_total, enron_data_total)

poi_total = len([x for x,y in enron_data.items() if y["poi"]]) + 10
print(poi_total)