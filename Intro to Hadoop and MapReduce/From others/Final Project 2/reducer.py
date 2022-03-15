#!/usr/bin/python

import sys

answers_length = 0
number_of_answers = 0
question_length = 0
old = None

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 3:
        continue

    id, node_type, body = data
    body = float(body)

    if old != None and old != id:
        if number_of_answers > 0:
            average_answer_length = answers_length / number_of_answers
        else:
            average_answer_length = 0

        print "{0}\t{1}\t{2}".format(old, int(question_length), average_answer_length)

        answers_length = 0
        number_of_answers = 0
        question_length = 0

    if node_type == "answer":
        answers_length += body
        number_of_answers += 1
    elif node_type == "question":
        question_length += body

    old = id

if old != None:
    if number_of_answers > 0:
        average_answer_length = answers_length / number_of_answers
    else:
        average_answer_length = 0

    print "{0}\t{1}\t{2}".format(old, int(question_length), average_answer_length)
