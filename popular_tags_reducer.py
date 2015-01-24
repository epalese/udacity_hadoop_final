#!/usr/bin/python

import sys

# This function insert the element {tag: tagname, counts: value} in taglist only if conuts value is greater than
# the minimum value of counts already present in the list. 
# After the insertion, the element with the minimum value for counts is removed.
# The function in other words keeps the top 10 by counts elements in taglist.
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
		tagCount = 0
	
	currentTag = tag
	tagCount += 1

if currentTag != None:
	top10tags = insertTop10({'tag': tag, 'count': tagCount}, top10tags)
	for elem in top10tags:
		print elem['tag'], "\t", elem['count']
