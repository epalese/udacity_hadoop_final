#!/usr/bin/python
# The reducer receives as input a tab separated list of: tag, node id, authorid
# The final output will be the Top 10 tags by:
# tagCount: number of times tag has been used in questios, answers or comments
# numberOfTagUsers: the number of different users that have used the specific tag
# numberOfAllUsers: the number of different users that have posted a question, answer or comment
#
# The reducer will produce a top 10 list by the following weighted sum:
# tagCount * numberOgTagUsers / numberOfAllUsers 

import sys

currentTag = None
tagCount = 0
allUsers = set()
tagUsers = set()
tagsStats = []

for line in sys.stdin:
	data = line.strip().split("\t")
    	if len(data) != 3:
		# Something has gone wrong. Skip this line.
		continue

	tag, nodeId, authorId = data
		
	if currentTag and currentTag != tag:
		tagsStats.append({'tag': currentTag, 'tagCount': tagCount, 'usersCount': len(tagUsers)})
		tagCount = 0
		tagUsers = set()
	
	currentTag = tag
	tagCount += 1
	allUsers.add(authorId)
	tagUsers.add(authorId)

if currentTag != None:
	output = []
	for tagStats in tagsStats:
		tag = tagStats['tag']
		usersCount = tagStats['usersCount']
		tagPerUserRatio = float(tagCount) * usersCount / len(allUsers)
		output.append({'tag': tag, 'tagPerUserRatio': tagPerUserRatio})

	for elem in sorted(output, key=lambda k: k['tagPerUserRatio'], reverse=True)[:10]:
		print elem['tag'], "\t", elem['tagPerUserRatio']
