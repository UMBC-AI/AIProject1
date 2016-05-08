# Andrew Maddox
# CMSC 471
# Project 1

import sys
from collections import deque

try: 
	import Queue as Q
except ImportError:
	import queue as Q


# Read input
# Save the input to a variable

def readInput(fileName):
	graph = dict()
	with open(fileName, "r") as f:
		for line in f:
			data = line.split(" ")
			if data[0] in graph:
				temp = graph[data[0]]
				temp.update({str(data[1]) : int(data[2])})
				graph[data[0]] = temp
			else:
				graph[str(data[0])] = {str(data[1]) : int(data[2])}
	return graph





# Depth-first search

def dfs(graph, end, stack):
	while stack:
		currentNode = {}
		start, visited = stack.pop()
		if start in graph:
			currentNode = graph[start]
			del graph[start]
		
		if(start == end):
			return visited
		else:
			for key, value in sorted(currentNode.items(), reverse=True):
				stack.append((str(key), visited + [key]))

	return list()


# Breadth-first search

def bfs(graph, end, queue):
	while queue:
		currentNode = {}
		start, visited = queue.popleft()

		if start in graph:
			currentNode = graph[start]
			del graph[start]
		if(start == end):
			return visited
		else:
			for key, value in sorted(currentNode.items()):
				queue.append((str(key), visited + [key]))

	return list()



# Uniform-cost search

def ucs(graph, end, pQ):
	while not pQ.empty():
		currentNode = {}
		cost, start, visited = pQ.get()

		if start in graph:
			currentNode = graph[start]
			del graph[start]
		if(start == end):
			return visited
		else:
			for key in currentNode:
				pQ.put((cost + currentNode[key], str(key), visited + [key]))
	return list()



# Write output

def writeFile(fileName, visited):
	out = open(fileName, "w")
	for key in visited:
		print(key)
		out.write(key + "\n")
	out.close()



		



# Main
# Check user input to make sure they entered 5 arguments
# Start search based on user input 
# Print results of search

def main():
	if len(sys.argv) < 6:
		print("***You need 5 command line arguments to run this program***")

	else:
		inputFile = sys.argv[1]
		outputFile = sys.argv[2]
		start = sys.argv[3]
		end = sys.argv[4]
		search = sys.argv[5]
		visited = list()


		# Read input
		graph = readInput(inputFile)
		
		if search == "DFS":
			stack = [(start, list(start))]
			visited = dfs(graph, end, stack)
		elif search == "BFS":
			queue = deque()
			queue.append((start, list(start)))
			visited = bfs(graph, end, queue)
		elif search == "UCS":
			pQ = Q.PriorityQueue()
			pQ.put((0, start, list(start)))
			visited = ucs(graph, end, pQ)
		else:
			dfs(graph, start, end, visited)

		writeFile(outputFile, visited)
main()



















