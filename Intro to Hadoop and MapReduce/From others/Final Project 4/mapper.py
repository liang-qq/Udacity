#!/usr/bin/python

import csv, sys

reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()

for line in reader:
    if len(line) == 19:
        node_type = line[5]
        
        if node_type == "question":
            identifier = line[0]
        else:
            identifier = line[7]

	print "{0}\t{1}".format(identifier, line[3])
