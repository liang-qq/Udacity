#!/usr/bin/python

import csv, sys

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    if len(line) == 19:
        if not line[0].isdigit():
            continue

        node_id, title, tag_names, author_id, body, node_type, parent_id, abs_parent_id, added_at, score = line[0:10]
        
        if node_type == "answer":
            identifier = abs_parent_id
        elif node_type == "question":
            identifier = node_id

	print "{0}\t{1}\t{2}".format(identifier, node_type, len(body))

