# coding: utf-8

# Jeremy Aguillon
# CMSC 471
# Project 1
# Due 2/15/2016

# imports queues for BFS and UCS
from queue import Queue
from queue import PriorityQueue
# imports sys for command line arguments (argv)
import sys


## Constants ## 
# Command line arguments
INPUT_FILE = 1
OUTPUT_FILE = 2
START_NODE = 3
END_NODE = 4
SEARCH_TYPE = 5

# Input file arguments
NODE_1 = 0
NEIGHBOR_1 = 1
WEIGHT = 2

# Error flags
FILE_IO = -1
MISSING_NODE = -2
MISSING_START = -3
MISSING_END = -4
NO_NEIGHBORS = -5
NO_PATH = ""


# getNodes() takes in a filename and parses the file to create nodes for each of the inputs in the file
#            This also validates that the file exists and can be opened, and the start and end nodes are
#            in the given graph.
# Input: Filename - string of the filename of the input
#        start - the node to begin searching at
#        end - the node to stop searching at
# Output: The nodes that are created and stored in a dictionary or an error flag
def getNodes(Filename, start, end):
    # flags to validate that nodes exist in the given graph
    foundStart = 0
    foundEnd = 0

    # validation for opening the file
    try:
        inFile = open(Filename, 'r')

    except IOError as e:
        print ("I/O error({0}): {1} \"{2}\"".format(e.errno, e.strerror, Filename),)
        # error flag of -1 for main
        return FILE_IO

    # initialized dictionary
    nodeDict = {}

    # loops through each line of the file
    for line in inFile:
        line = line.split()

        # checks for start and end nodes and sets flag when found
        if line[NODE_1] == start or line[NEIGHBOR_1] == start:
            foundStart = 1

        if line[NODE_1] == end or line[NEIGHBOR_1] == end:
            foundEnd = 1

        # adds an entry for each unadded node as the key with a tuple of neighbors and weight as the value
        if line[NODE_1] in nodeDict.keys():
            nodeDict[ line[NODE_1] ].append( ( line[NEIGHBOR_1], int(line[WEIGHT]) ) )
        # if the node already exists, adds another node to the neighbors
        else:
            nodeDict[ line[NODE_1] ] = [(line[NEIGHBOR_1], int(line[WEIGHT]) )]
            
    inFile.close()

    # returns the dictionary if the nodes exist
    if foundStart and foundEnd:
        if start in nodeDict.keys():
            return nodeDict
        else:
            return NO_NEIGHBORS
    # returns an error message otherwise
    elif foundStart:
        return MISSING_END
    elif foundEnd:
        return MISSING_START
    else: 
        return MISSING_NODE


# DFS() uses a graph to search depth first to find a path to a given end node 
#       from a start node and returns the path as a list
# Input: nodeDict - a dictionary of nodes representing a graph
#        start - a start node that is in the graph
#        end - the goal node that is in the graph
# Output: a list of the path from start to end 
def DFS(nodeDict, start, end):
    # creates lists for nodes to visit and visited nodes
    Open = []
    closed = []

    # begins with the start node
    Open.append(start)

    # loops through the unvisited nodes until there are no more
    while Open:
        # examines the node at the top of the stack
        curNode = Open.pop()
        # checks if the node is found
        if curNode == end:
            # adds the final node and returns the path
            closed.append(curNode)
            return closed
        # checks if you have visited the node before
        elif curNode not in closed:
            # adds the current node to visited nodes
            closed.append(curNode)
            # checks if the current node has neighbors for directed graphs
            if curNode in nodeDict.keys():
                # adds all neighbors of the current node to unvisited
                for pair in sorted(nodeDict[curNode], reverse=True):
                    Open.append(pair[0])

    # return blank string if none found
    return ""
    

# BFS() uses a graph to search breadth first to find a path to a given end node 
#       from a start node and returns the path as a list
# Input: nodeDict - a dictionary of nodes representing a graph
#        start - a start node that is in the graph
#        end - the goal node that is in the graph
# Output: a list of the path from start to end 
def BFS(nodeDict, start, end):
    # creates the unvisited nodes as a queue
    Open = Queue()
    # closed 1 is the path taken and closed 2 is the node that led to the next node
    seen = []
    closed1 = []
    closed2 = []

    # begins searching at the start node which is the node and what led to it
    Open.put((start,start))
    seen.append(start)

    # loops until there are no more unvisited nodes
    while Open:
        # dequeues the first node
        curNode = Open.get()
    
        # checks if the node is at the end and stops if it is
        if curNode[0] == end:
            # adds the final node and what sent it to the lists
            closed1.append(curNode[0])
            closed2.append(curNode[1])

            # begins tracing list one back for the path at the goal node
            cur = closed1[len(closed1)-1]
            final = [cur]
            
            # searches each pair until it goes back to the start node
            while cur != start:
                # finds the location of the current node
                loc = closed1.index(cur)
                # finds the node that sent the current node
                cur = closed2[loc]
                # adds the node that sent it to the list
                final.append(cur)

            # returns the final path reversed for consistency with DFS
            return reversed(final)

        # checks if the current node has neighbors for directed graphs
        elif curNode[0] in nodeDict.keys():
            # Adds each of the neighbors of the node if it is not the goal
            for pair in sorted(nodeDict[curNode[0]]):
                # must check if it is not in seen in case a previous node added it before closing
                if pair[0] not in seen:
                    seen.append(pair[0])
                    # each node is classified by the node it is at and the node that led to it
                    Open.put((pair[0], curNode[0]))

        
        # updates the visited lists and how they got there
        closed1.append(curNode[0])
        closed2.append(curNode[1])
        
    # return blank string if none found
    return ""


# UCS() uses a graph to search using Dijkstra's algorithm to find 
#       a path to a given end node from a start node and returns 
#       the path as a list
# Input: nodeDict - a dictionary of nodes representing a graph
#        start - a start node that is in the graph
#        end - the goal node that is in the graph
# Output: a list of the path from start to end 
def UCS(nodeDict, start, end):
    # crates the priority queue with a max value of 10,000
    Open = PriorityQueue(10000)
    # creates dictionaries to keep track of distance and previous node of each element
    distance = {}
    previous = {}

    # Initializes each node to have infinity length and no previous
    for node in nodeDict.keys():
        # gives the initial node 0 distance to be chosen first
        if node == start:
            distance[node] = 0
        else:
            distance[node] = float('inf')

        previous[node] = None

        # adds each node to the queue
        Open.put((distance[node], node))

    # iterates through each node of the graph
    while Open:
        # gets the least valued piece from the queue
        cur = Open.get()
        
        # checks if reached the end
        if cur[1] == end:
            temp = end
            finalPath = [temp]
            # loops backwards through the found path until reaches start
            while temp != start:
                temp = previous[temp]
                finalPath.append(temp)
            # returns start reverse for consistency
            return reversed(finalPath)

        # list of nodes that are in open that need to be updated
        openNodes = []
        # Adds each of the neighbors of the node and compares their length
        for pair in sorted(nodeDict[cur[1]]):
            # distance of current path is saved and compared with distance
            alternate = distance[cur[1]] + pair[1]

            # if the distance is shorter it replaces in the algorithm
            if alternate < distance[pair[0]]:
                distance[pair[0]] = alternate
                previous[pair[0]] = cur[1]

                # finds if the nodes are in the open queue and adds the new value to temp list
                if pair[0] in [x[1] for x in Open.queue]:
                    openNodes.append( (alternate, pair[0]) )

        # list of all the nodes in open including updated ones
        newOpen = []    

        # dequeues each of the nodes in Open to update the ones that need it
        for i in range(len(Open.queue)):
            node = Open.get()
            if node[1] in [x[1] for x in openNodes]:
                newOpen.append([x for x in openNodes if x[1] == node[1]][0])
            else:
                newOpen.append(node)

        # repopulates Open with updated values
        for node in newOpen:
            Open.put(node)

    # end while loop

    # returns blank string if no output found
    return ""


# writePath() writes the final path it takes to search from start to end to a new file 
# Input: outFile - the filename of the file to be written to
#        finalPath - a list of the nodes of the path from start to end nodes
# Output: None
def writePath(outFile, finalPath):
    outFile = open(outFile, 'w')

    if NO_PATH != finalPath:
        for node in finalPath:
            outFile.write("{0}\n".format(node))
    else:
        outFile.write("No path found")
        
    outFile.close()
    
    
# main
def main(argv):
    # validates amount of arguments given
    if len(argv) != 6:
        print("Invalid Input\nUsage: python Search.py <input file> <output file> <start node> <end node> <search_type>")
    # validates correct search types entered
    elif "DFS" != argv[SEARCH_TYPE] and "BFS" != argv[SEARCH_TYPE] and "UCS" != argv[SEARCH_TYPE]:
        print("Invalid Search Type\nUsage: python Search.py <input file> <output file> <start node> <end node> <search_type>\n<search_type> = DFS or BFS or UCS")
    else:
        # Gets the dictionary of nodes and weights
        nodeDict = getNodes(argv[INPUT_FILE], argv[START_NODE], argv[END_NODE])

        # validates start and end nodes exist in graph
        if type(nodeDict) == int and nodeDict <= MISSING_NODE:
            if nodeDict == MISSING_START:
                print("Start node ({0}) is not in the given graph.".format(argv[START_NODE]))        
            elif nodeDict == MISSING_END:
                print("End node ({0}) is not in the given graph.".format(argv[END_NODE]))    
            elif nodeDict == NO_NEIGHBORS:
                print("Start node ({0}) has no neighbors.".format(argv[START_NODE]))   
            else:
                print("Start node ({0}) and/or End node ({1}) are not in the given graph.".format(argv[START_NODE], argv[END_NODE]))        
        
        # checks if file was sucessfully opened
        elif nodeDict != FILE_IO:    
            # performs the search on the graph that the user requests
            if "DFS" == argv[SEARCH_TYPE]: 
                finalPath = (DFS(nodeDict, argv[START_NODE], argv[END_NODE]))
            elif "BFS" == argv[SEARCH_TYPE]:
                finalPath = BFS(nodeDict, argv[START_NODE], argv[END_NODE])    
            elif "UCS" == argv[SEARCH_TYPE]:
                finalPath = UCS(nodeDict, argv[START_NODE], argv[END_NODE])

            # writes the final result to the provided file
            writePath(argv[OUTPUT_FILE], finalPath)

# call to main
main(sys.argv)

# old test cases
#main(['Search.py','test.txt','sup1.txt','A','F', 'DFS'])
#main(['Search.py','utube.txt','sup2.txt','A','H', 'BFS'])
#main(['Search.py','other.txt','sup3.txt','S','G', 'DFS'])
#main(['Search.py','sample.txt','final.txt','1','50', 'BFS'])
#main(['Search.py','another.txt','one.txt','a','g', 'UCS'])


