#!/usr/bin/python

import sys

hours = [0] * 24
old_author = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    author_id, added_at = data

    if old_author and old_author != author_id:
        hour_posts = max(hours)
        for hour, post_count in enumerate(hours):
            if post_count == hour_posts:
                print "{0}\t{1}".format(old_author, hour)
        	hours = [0] * 24

    active_hour = int(added_at.split(" ")[1][0:2])
    hours[active_hour] += 1
    old_author = author_id

hour_posts = max(hours)
for hour, posts_count in enumerate(hours):
    if posts_count == hour_posts:
        print "{0}\t{1}".format(old_author, hour)
