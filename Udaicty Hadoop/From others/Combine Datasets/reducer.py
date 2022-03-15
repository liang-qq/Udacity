#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys
import csv

key_A = None
key_B = None
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

def reducer():
    for line in sys.stdin:
        
        # YOUR CODE HERE
        data = line.strip().split('\t')

        if data[1] == 'A':
            key_A = data[0]
            data_A = data[2:]
        elif data[1] == 'B':
            key_B = data[0]
            data_B = data[2:]
        
        if key_A == key_B:
             writer.writerow(data_B[:3] + [key_A] + data_B[3:] + data_A)

if __name__=='__main__':
    reducer()