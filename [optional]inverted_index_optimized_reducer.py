#!/usr/bin/python

import sys

wordNodes = []
oldWord = None

# input: word\tnodes
# Where 'nodes' is a list of one or more nodes whose body contains the word
# If this script is used as a combiner, 'nodes' will be a list with only one element.
# If used as a reducer it will contain a comma-separted list of nodes.

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisWord, nodesListStr = data_mapped
    if len(thisWord) == 0 or len(nodesListStr) == 0:
	# Something has gone wrong. Skip this line.
	continue

    # print the values for the current word before going to the next one
    if oldWord and oldWord != thisWord:
	wordNodes.sort()
        print oldWord, "\t", ', '.join(wordNodes)
	
	# reset variables for the next word
        oldWord = thisWord;
        wordNodes = []

    oldWord = thisWord
    # split the comma-seperated list of nodes, remove leading and trailing white spaces and remove
    # any Null element from the set
    nodesList = filter(None, [s.strip() for s in nodesListStr.split(',')])
    wordNodes.extend(nodesList)

# handle the last key value
if oldWord != None:
    wordNodes.sort()
    print oldWord, "\t", ', '.join(wordNodes)
