#!/usr/bin/python

import sys

# Return the indexes of the max elements
def findMaxHours(hoursCount):
	m = max(hoursCount)
	maxHours = [i for i, j in enumerate(hoursCount) if j == m]
	return maxHours

# An array is used to store user's post counts.
# The array position corresponds to the hour: 
# e.g: 
# hoursCout[0] is the count for 00.00 (12.00 AM)
# hoursCount[20] is the count for 20.00 (08.00 PM)
hoursCount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
currentAuthorId = None

for line in sys.stdin:
	data = line.strip().split("\t")
    	if len(data) != 3:
		# Something has gone wrong. Skip this line.
        	print 'data less than 3', data
		continue

	authorId, hour, count = data
	if (not hour.isdigit()) or (not count.isdigit()):
		# Something has gone wrong. Skip this line.
		print 'no digit ', data
		continue 

	if currentAuthorId and currentAuthorId != authorId:
		# find the max hour
		maxHours = findMaxHours(hoursCount)
		for maxHour in maxHours:
			print currentAuthorId, "\t", maxHour
	
		# set up for next authorId
		hoursCount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	currentAuthorId = authorId
	hourInt = int(hour)
	countInt = int(count)
	hoursCount[hourInt] += countInt

if currentAuthorId != None:
	# find the max hour
	maxHours = findMaxHours(hoursCount)
	for maxHour in maxHours:
		print currentAuthorId, "\t", maxHour
