#!/usr/bin/python

# input format:
# "id"\t"title"\t"tagnames"\t"author_id"\t"body"\t"node_type"\t"parent_id"\t"abs_parent_id"\t"added_at"\t"score"\t"state_string"\t"last_edited_id"\t"last_activity_by_id"\t"last_activity_at"\t"active_revision_id"\t"extra"\t"extra_ref_id"\t"extra_count"marked"

import sys, csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None)	# skip header

for line in reader:
	if (line != None and len(line) == 19):
		author_id = line[3]
		
		# added_at values have the followign format: 2012-02-21 05:08:03.824261+00
		# In the following statement added_at is split at the plus symbol. The rpartion
		# function will so return the date part up to the plus symbol, the plus symbol and
		# the remaining UTC offset.
		added_at, symbol, utc = line[8].rpartition('+')
		added_at_hour = datetime.strptime(added_at, '%Y-%m-%d %H:%M:%S.%f').hour 
		
		print "{0}\t{1}\t{2}".format(author_id, added_at_hour, 1)
