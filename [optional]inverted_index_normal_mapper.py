#!/usr/bin/python

# input format:
# "id"\t"title"\t"tagnames"\t"author_id"\t"body"\t"node_type"\t"parent_id"\t"abs_parent_id"\t"added_at"\t"score"\t"state_string"\t"last_edited_id"\t"last_activity_by_id"\t"last_activity_at"\t"active_revision_id"\t"extra"\t"extra_ref_id"\t"extra_count"marked"

import sys, csv, re

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None)	# skip header

for line in reader:
    if (line != None):
	# split the body content using a set of word separators and then
	# clean the list removing all the length 0 words
	words = filter(None, re.split("[ .,!?:;\"\(\)#$=\-/]+", line[4]))
	words = [x.lower() for x in words]

	for word in words:
		if len(word) > 0 and len(line[0]) > 0:
			print "{0}\t{1}".format(word, line[0])
