#!/usr/bin/python

import sys
import csv
import string

reader = csv.reader(sys.stdin, delimiter='\t')
	
for line in reader:
	body = line[4]
	id = line[0]
	
	words = body.strip().split()
	for word in words:
        	if 'fantastic' in word.lower():
            		print "{0}\t{1}".format(word.lower(), id)

