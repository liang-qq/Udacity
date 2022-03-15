#!/usr/bin/python

import csv, sys

reader = csv.reader(sys.stdin, delimiter='\t')
# Skip header.
reader.next()

for line in reader:
	if len(line) == 19:
		node_type = line[5]
		if node_type == "question":
                	tagnames_str = line[2]
                	tagnames = tagnames_str.split()
                	for tagname in tagnames:
				print "{0}\t{1}".format(tagname, "1")
