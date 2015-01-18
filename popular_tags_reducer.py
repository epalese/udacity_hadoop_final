#!/usr/bin/python

import sys

# insert the element {tag: tagname, counts: value} in list
# if value is greater than the minimum value of counts that
# is already in the list. 
# After the insertion, the element with the minimum value for
# counts is removed 
def insertTop10(element, taglist):
	i = 0
	inserted = False
	while (not inserted):
		if (i<len(taglist)):
			if element['count'] > taglist[i]['count']:
				taglist.insert(i,element)
				inserted = True
			else:
				i += 1 
		else:
			taglist.insert(i, element)
			inserted = True
	return taglist[:10]
   
currentTag = None
tagCount = 0
top10tags = []

# The mapper output will be a tab separated list: [authorid]\t[hour]\t[count]
# The count field will contain always a value of 1 unless a combiner is used that will group results by authorid and hour   

for line in sys.stdin:
	data = line.strip().split("\t")
    	if len(data) != 2:
		# Something has gone wrong. Skip this line.
		continue

	tag, nodeId = data
	if (not nodeId.isdigit()):
		# Something has gone wrong. Skip this line.
		continue
		
	if currentTag and currentTag != tag:
		top10tags = insertTop10({'tag': currentTag, 'count': tagCount}, top10tags)
		# print top10tags
		tagCount = 0
	
	currentTag = tag
	tagCount += 1

if currentTag != None:
	top10tags = insertTop10({'tag': tag, 'count': tagCount}, top10tags)
	for elem in top10tags:
		print elem['tag'], "\t", elem['count']