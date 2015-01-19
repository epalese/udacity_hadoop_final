#!/usr/bin/python

import sys

wordNodes = []
oldWord = None

# input: word\tnode
# Where 'node' is the node whose body contains the word

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisWord, node = data_mapped
    if len(thisWord) == 0 or len(node) == 0:
        # Something has gone wrong. Skip this line.
	continue

    # print the values for the current word before going to the next one
    if oldWord and oldWord != thisWord:
	wordNodes.sort()
        print oldWord, "\t", wordNodes
	
	# reset variables for the next word
        oldWord = thisWord;
        wordNodes = []

    oldWord = thisWord
    wordNodes.append(node)

# handle the last key value
if oldWord != None:
    wordNodes.sort()
    print oldWord, "\t", wordNodes
