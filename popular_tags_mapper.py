#!/usr/bin/python

# Format of each line is:
# id title tagnames author_id body node_type parent_id abs_parent_id added_at score state_string last_edited_id last_activity_by_id last_activity_at active_revision_id extra extra_ref_id extra_count marked
# fields are \t separated

import sys, csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
# writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
next(reader, None)	# skip header

for line in reader:
	if (line != None and len(line) == 19):
		node_type = line[5]
		if line[5] == 'question':
			tags = line[2].split(' ')
			for tag in tags:
				print "{0}\t{1}".format(tag, line[0])
