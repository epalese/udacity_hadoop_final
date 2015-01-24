#!/usr/bin/python

import sys

currentAuthorId = None
numOfScores = 0
sumOfScores = 0
numOfBodyLengths = 0
sumOfBodyLengths = 0

# The mapper output will be: "authorid"\t"averagelength"\t"averagescore"

for line in sys.stdin:
	data = line.strip().split("\t")
    	if len(data) != 3:
		# Something has gone wrong. Skip this line.
		continue

	authorId, bodyLength, score = data
	if (not score.isdigit() or not bodyLength.isdigit()):
		# Something has gone wrong. Skip this line.
		continue 
		
	if currentAuthorId and currentAuthorId != authorId:
		# calcuate the average score
		if numOfScores > 0:
			avgScore = sumOfScores / numOfScores
		else:
			avgScore = 0
		# calculate the average body length
		if numOfBodyLengths > 0:
			avgBodyLength = sumOfBodyLengths / numOfBodyLengths
		else:
			avgBodyLength = 0
		print currentAuthorId, "\t", avgBodyLength, "\t", avgScore

		numOfScores = 0
		sumOfScores = 0
		numOfBodyLengths = 0
		sumOfBodyLengths = 0
	
	currentAuthorId = authorId
	numOfScores += 1
	sumOfScores += float(score)
	numOfBodyLengths += 1
	sumOfBodyLengths += float(bodyLength)

if currentAuthorId != None:
	if numOfScores > 0:
		avgScore = sumOfScores / numOfScores
	else:
        	avgScore = 0
	if numOfBodyLengths > 0:
		avgBodyLength = sumOfBodyLengths / numOfBodyLengths
	else:
		avgBodyLength =	0
	print currentAuthorId, "\t", avgBodyLength, "\t", avgScore

