#!/usr/bin/python

import sys
oldquestion = None
students = []

for line in sys.stdin:
    data = line.strip().split('\t')

    if len(data) != 2:
        continue

    question, author = data

    if oldquestion != None and oldquestion != question:
        print "{0}\t{1}".format(oldquestion, students)
        students = []

    oldquestion = question
    students.append(author)

if oldquestion != None:
	print "{0}\t{1}".format(oldquestion, students)
