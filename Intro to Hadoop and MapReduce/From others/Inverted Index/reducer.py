#!/usr/bin/python

import sys

count = 0
list = []

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue
	
	thisKey, thisValue = data_mapped
	
	if 'fantastic' in thisKey:
        	if 'fantastically' not in thisKey:
            		count += 1

    	if 'fantastically' in thisKey:
        	list.append(int(thisValue))
		

list = sorted(list)
print "{0}\t{1}".format(count, list)
