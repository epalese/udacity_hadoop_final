#!/usr/bin/python

import sys

currentNodeId = None
questionLength = 0
countAnswerLength = 0
countAnswers = 0

# input from the mapper: "authorid"\t"hour"\t"count"
# The count field will contain always a value of 1 unless a combiner is used that will group results by authorid and hour   

for line in sys.stdin:
	data = line.strip().split("\t")
    	if len(data) != 3:
		# Something has gone wrong. Skip this line.
		continue

	nodeId, type, length = data
	if (not nodeId.isdigit()) or (not length.isdigit()):
		# Something has gone wrong. Skip this line.
		continue 
		
	if currentNodeId and currentNodeId != nodeId:
		if countAnswers > 0:
			avgAnswerLength	= countAnswerLength / countAnswers
		else:
			avgAnswerLength = 0
		print currentNodeId, "\t", questionLength, "\t", avgAnswerLength
		questionLength = 0
		countAnswers = 0
		countAnswerLength = 0
	
	currentNodeId = nodeId
	if type == 'question':
		questionLength = length
	if type == 'answer':
		countAnswers += 1
		countAnswerLength += float(length)

if currentNodeId != None:
	if type	== 'question':
                questionLength = length
        if type	== 'answer':
		countAnswers += 1
		countAnswerLength += float(length)
	
	if countAnswers	> 0:
		avgAnswerLength = countAnswerLength / countAnswers
	else:
		avgAnswerLength = 0	
	print currentNodeId, "\t", questionLength, "\t", avgAnswerLength
