
# File:       Search.py
# Written by: Siqi Lin
# Date:       2/5/16
# Class:      CMSC 471
# Instructor: Maksym Morawski
# Section:    02

#!/usr/bin/python
from __future__ import print_function
from queue import PriorityQueue
from collections import deque
import sys, getopt

class Vertex(object):

    def __init__(self, vertexName,vertexCost):
        self.vertex_name = vertexName
        self.cost = vertexCost

def printGraph(graph, verticesSet):
    for key, valueList in graph.items():
        print("vertex", key, " ", end="to: ")
        for item in valueList:
            print(" " ,item.vertex_name, end=":")
            print(item.cost, end="")
        print()
    print("verticesSet", verticesSet)
    #for i in graph:
    #   print (i)

     #       , graph[i])

def printAllNodes(nodes):
    print (nodes)

# File parsing
def ReadFile(fileName):

    graph = {}
    verticesSet = set()

    #open the input file to read
    infile = open(fileName, 'r')

    #iteate through the file
    for line in infile:
        line = line.split()
        verticesSet.add(line[0])
        verticesSet.add(line[1])
        key = line[0]
        value = Vertex(line[1],line[2])
        if key in graph:
            #assign edges of a node
            graph[key].append(value)
            graph[key] = sorted(graph[key], 
                key=lambda x: x.vertex_name, reverse=False)
        else:
            graph[key] = [value]
    return graph, verticesSet

# Write to an output file
def OutputFile(fileName, path):
    outfile = open(fileName, 'w')
    for item in path:
        outfile.write(item)
        outfile.write("\n")

def print_path(path):
    print("STARTING TO PRINT PATH")

    for item in path:
        print(item)

# Begin DFS
def depth_first_search(graph, start, end,fileName):
    stack = []
    path = []
    visited = []

    stack.append(start)
    # if the starting node and the ending node is the same
    if(start == end):
        path.append(start)
        OutputFile(fileName,path)
        return 0
    else:
        try:
            #Ensure that the stack is not empty
            while stack:
                #print("B------", stack)
                current_vertex = stack.pop()
                if(current_vertex not in graph.keys() 
                    and current_vertex != end):
                    path.pop()
                    current_vertex = stack.pop()
                path.append(current_vertex)
                # a path has been found
                if current_vertex == end:
                    OutputFile(fileName,path)
                    return 0
                # append to the visited list
                if current_vertex not in visited:
                    isNoOutlet = True
                    visited.append(current_vertex)
                    for item in graph[current_vertex]:
                        if (item.vertex_name not in visited and 
                            item.vertex_name not in stack):
                            stack.append(item.vertex_name)
                            isNoOutlet = False
                    if(isNoOutlet):
                        path.pop()
                #print("A------", stack)
                #print("visited ", visited)
                #print()
        # path not found
            OutputFile(fileName,[])
        except:
            OutputFile(fileName,path)

# End DFS

# Begin BFS
def breadth_first_search(graph, start, end, fileName):
    queue = deque([])
    path = []
    visited = []
    trace = {}
    queue.append(start)
    # if the starting node and the ending node is the same
    if (start == end):
        path.append(start)
        OutputFile(fileName,path)
        return 0
    else:
        #Ensure the queue is not empty
        while queue:
            #print("B------- ", queue)
            try:
                current_vertex = queue.popleft()
                if(current_vertex not in graph.keys() 
                                    and current_vertex != end):
                    current_vertex = queue.popleft()
                # if the path has been found
                if current_vertex == end:
                    iterator = current_vertex
                    path.append(iterator)
                    # Trace back from the current node to the source node
                    while iterator != start:
                        iterator = trace[iterator]
                        path.append(iterator)
                    path.reverse()
                    OutputFile(fileName,path)
                    return 0
                if current_vertex not in visited:
                    visited.append(current_vertex)
                    for item in graph[current_vertex]:
                        #print("Before:",queue)
                        #print("Item to be appended", item.vertex_name)
                        flag = item.vertex_name in queue or item.vertex_name in visited
                        if not flag:
                            queue.append(item.vertex_name)
                            trace[item.vertex_name] = current_vertex
                #print(queue)
            #no path has been found
                #print("Ah------- ", queue)
            except:
                OutputFile(fileName,path)
        if current_vertex == end:
                    iterator = current_vertex
                    path.append(iterator)
                    # Trace back from the current node to the source node
                    while iterator != start:
                        iterator = trace[iterator]
                        path.append(iterator)
                    path.reverse()
        OutputFile(fileName,path)
        #print(">_<", path)
# End BFS

# Begin UCS
def uniform_cost_search(graph, start,end,fileName):
    distance = {}
    #prev is used to trace paths
    prev = {}
    distance[start] = 0
    stack = []
    pQueue = PriorityQueue()
    temp_list = []

    for key in graph.keys():
        if key != start:
            # Initializing distance as infinity and previous node as unknown
            distance[key] = 9999
            prev[key] = ''
        # Insert item onto pQueue with priority
        pQueue.put(([distance[key]], key))
        for value in graph[key]:
            if value.vertex_name not in graph.keys():
                if value.vertex_name != start:
                    distance[value.vertex_name] = 9999
                    prev[value.vertex_name] = ''
                # insert an item onto the priority queue with priority
                pQueue.put(([distance[value.vertex_name]], value.vertex_name))

    #print("PREV: ", prev)

    while not pQueue.empty():
        current_vertex = pQueue.get()[1]
            #return 0
        #loop through the neighbor of the current_vertex
        if current_vertex in graph.keys():
            # tempQueue = PriorityQueue()
            # tempQueue = pQueue
            for neighbor in graph[current_vertex]:
                #calculate the cost needed to go from start to
                temp_cost = distance[current_vertex] + int(neighbor.cost)
                if temp_cost < distance[neighbor.vertex_name] :
                    distance[neighbor.vertex_name] = temp_cost
                    prev[neighbor.vertex_name] = current_vertex
                    temp_list = pQueue.queue
                    #decrease priority
                    temp_list[0][0][0] = distance[neighbor.vertex_name]
                    #print("Queue:",pQueue.queue)
                    #print("vertex:", neighbor.vertex_name)
                    #print("distance:", distance[neighbor.vertex_name])
    iterator = end
    #print("iterator:" ,iterator)
    #print("prev[iterator]:",prev[iterator])
    while( (iterator != start) and (prev[iterator] != '')):
#        print(iterator)
        stack.append(iterator)
        iterator = prev[iterator]
    stack.append(start)
    stack.reverse()
    OutputFile(fileName,stack)


    return 0
# End UCS


def main():

    map = {}

    if len(sys.argv) != 6 :
        print('Usage: python Search.py <input file> <output file> ', end="")
        print('<start node> <end node> <search_type>')
    else:
        inputFile = str(sys.argv[1])
        outputFile = str(sys.argv[2])
        startNode = str(sys.argv[3])
        endNode = str(sys.argv[4])
        searchType = str(sys.argv[5])

    # file parsing
    map, verticesSet = ReadFile(inputFile)
    #printGraph(map, verticesSet)
    if(startNode not in verticesSet or endNode not in verticesSet):
        OutputFile(outputFile,[])

    # perform searches
    if searchType == "DFS":
        depth_first_search(map, startNode, endNode,outputFile)
    elif searchType == "BFS":
        breadth_first_search(map, startNode, endNode,outputFile)
    elif searchType == "UCS":
        uniform_cost_search(map, startNode, endNode,outputFile)
    else:
        print('Usage: python Search.py <input file> <output file> ', end="")
        print('<start node> <end node> <search_type>')


main()
