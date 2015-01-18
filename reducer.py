#!/usr/bin/python
import sys

currentNode = None
students = []

for line in sys.stdin:
	data = line.strip().split("\t")
    	if len(data) != 2:
		# Something has gone wrong. Skip this line.
		continue

	node, authorId = data
		
	if currentNode and currentNode != node:
		print currentNode, '\t', students
		students = []
	
	currentNode = node
	students.append(authorId)

if currentNode != None:
	print currentNode, '\t', students
