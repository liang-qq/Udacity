#!/usr/bin/python

import csv, sys

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    author_id = line[3]
    hour = line[8]

    if author_id == "author_id":
        continue

    print "{0}\t{1}".format(author_id, hour)

