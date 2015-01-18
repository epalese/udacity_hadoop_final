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
		author_id = line[3]
		added_at, sym, utc = line[8].rpartition('+')
		# added_at values are as the following: 2012-02-21 05:08:03.824261+00
		added_at_hour = datetime.strptime(added_at, '%Y-%m-%d %H:%M:%S.%f').hour 
		
		print "{0}\t{1}\t{2}".format(author_id, added_at_hour, 1)
