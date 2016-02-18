# Filename: proj1.py
# Nick Pascarella np5@umbc.edu
# 2/15/16
# 
#For this project, I'll be writing breadth first search, depth first search
#and uniform cost search
#

import sys

from Queue import *


def BreadthFirstSearch(startNode, endNode, possiblePaths):

	searchQueue = Queue()
	searchQueue.put(startNode)

	pathTaken = {}
	pathTaken[startNode] = []
	nodesVisited = [startNode]

	

	while searchQueue.qsize() > 0:
		currNode = searchQueue.get()

		nodesVisited.append(currNode)

		

		#if the end node is reached
		if currNode == endNode:

			print "FOUND THE END"
			
			return pathTaken

		#if the end isn't reached yet
		#if the current node is the start of a path
		if currNode in possiblePaths.keys():

			pathsToTake = list(possiblePaths[currNode].keys())
			pathsToTake.sort() #puts them in alphabetic order

			#checks all the nodes that can accessed from this node
			for eachNode in pathsToTake:

				#if the node in this path hasnt been seen yet
				if eachNode not in nodesVisited:

					#if we havent gone down this path yet
					if eachNode not in pathTaken:

						searchQueue.put(eachNode)
						pathTaken[eachNode] = currNode

	#if no path is found, return empty string
	return []






def DepthFirstSearch(startNode, endNode, possiblePaths):
	
	searchStack = [startNode]

	pathTaken = {}
	pathTaken[startNode] = []
	nodesVisited = [startNode]

	
	#while stack isn't empty
	while searchStack:
		currNode = searchStack.pop()

		nodesVisited.append(currNode)

		

		#if the end node is reached
		if currNode == endNode:

			print "FOUND THE END"
			
			return pathTaken

		#if the end isn't reached yet
		#if the current node is the start of a path
		if currNode in possiblePaths.keys():

			pathsToTake = list(possiblePaths[currNode].keys())
			pathsToTake.sort() #puts them in alphabetic order

			#checks all the nodes that can accessed from this node
			for eachNode in pathsToTake:

				#if the node in this path hasnt been seen yet
				if eachNode not in nodesVisited:

					searchStack.append(eachNode)

					pathTaken[eachNode] = currNode

	#if no path is found, return empty string
	return []



def UniformCostSearch(startNode, endNode, possiblePaths):

	prioQueue = [startNode]

	pathTaken= {}
	pathTaken[startNode] = 0
	costsTaken = {}
	costsTaken[startNode] = 0

	nodesVisited = [startNode]

	while prioQueue:

		print "       top Prio is "
		print prioQueue[0]
		currNode = prioQueue[0]

		for eachNode in prioQueue:

			#finds the smallest weight in the queue
			if costsTaken[eachNode] > costsTaken[currNode]:
				currNode = eachNode


		#This removes it from teh queue but still saves it
		#thanks to stackoverflow for this one
		prioQueue.remove(currNode)


		if currNode in possiblePaths.keys():

			print "        currNode is in keys"

			pathsToTake = list(possiblePaths[currNode].keys())

			print pathsToTake
			
			for eachNode in pathsToTake:

				print "                  checking eachNode: ", eachNode

				if eachNode in nodesVisited:

					print "            in visited"

					if (possiblePaths[currNode][eachNode] + costsTaken[currNode]) < costsTaken[eachNode]:
						
						costsTaken[eachNode] = possiblePaths[eachNode] + costsTaken[currNode]
						pathTaken[eachNode] = currNode

				else:

					print "            not in visited"

					pathTaken[eachNode] = currNode
					prioQueue.append(eachNode)
					nodesVisited.append(eachNode)

					currentCost = possiblePaths[currNode][eachNode] + costsTaken[currNode]
					costsTaken[eachNode] = currentCost


	if endNode not in nodesVisited:

		print "endNode not found"
		return {}

	else:

		print "   pathTaken is "
		print pathTaken

		return pathTaken







def main(argv):

	
	inFile = argv[1]


	graphFile = open(inFile, 'r')
	possiblePaths = {} #this is a dictionary

	for line in graphFile:

		edgeData = line.split() #contains both nodes in the edge and its weight

		edgeData[2] = int(edgeData[2])
		#if the node doesnt have paths started yet
		#then add a dict under that key
		if edgeData[0] not in possiblePaths:

			possiblePaths[edgeData[0]] = {}

		#takes the weight and puts in the proper path
		possiblePaths[edgeData[0]][edgeData[1]] = edgeData[2]
		

	graphFile.close()

	
	print "List of Edges:"
	print possiblePaths

	outFile = argv[2]
	pathDict = {}
	pathList = []

	startNode = argv[3]
	endNode = argv[4]


	searchType = argv[5]

	if searchType == "BFS":

		pathDict = BreadthFirstSearch(startNode, endNode, possiblePaths)
		print "    pathDict is: "
		print pathDict

	elif searchType == "DFS":

		pathDict = DepthFirstSearch(startNode, endNode, possiblePaths)

	elif searchType == "UCS":

		pathDict = UniformCostSearch(startNode, endNode, possiblePaths)

	else:
		print "No search type found."

	#if a path to last node wasnt found
	if not pathDict[endNode]:
		print pathDict[endNode]

	#if path was found
	else:

		#goes through the pathDict and creates a list containing the path found
		currStep = endNode
		while currStep != startNode:

			pathList = [currStep] + pathList
			print "pathDict[currStep] = "
			print pathDict[currStep]
			currStep = pathDict[currStep]

		pathList = [startNode] + pathList

		print "           pathList is: "
		print pathList


	results = open(outFile, 'w')

	for eachNode in pathList:
		results.write(eachNode + '\n')

	results.close()



main(sys.argv)
