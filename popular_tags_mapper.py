#!/usr/bin/python

# input format:
# "id"\t"title"\t"tagnames"\t"author_id"\t"body"\t"node_type"\t"parent_id"\t"abs_parent_id"\t"added_at"\t"score"\t"state_string"\t"last_edited_id"\t"last_activity_by_id"\t"last_activity_at"\t"active_revision_id"\t"extra"\t"extra_ref_id"\t"extra_count"marked"

import sys, csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None)	# skip header

for line in reader:
	if (line != None and len(line) == 19):
		node_type = line[5]
		# Consider tags only from question nodes
		if line[5] == 'question':
			tags = line[2].split(' ')
			for tag in tags:
				print "{0}\t{1}".format(tag, line[0])
