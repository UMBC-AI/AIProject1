
# coding: utf-8

# In[27]:

def loadFile(fileName):

    # Load the input file
    inputFile = open(fileName, 'r')

    #inputContents = inputFile.read()
    #print(inputContents)

    lines = []

    for line in inputFile:
        lines.append(line.rstrip('\n'))
        #print(lines)

    inputFile.close()

    graph = Graph()

    # Start looping for each line    

    for index in range(0, len(lines)):

        # Strips the start node from the line
        currentLine = lines[index]
        segments = currentLine.split(" ")

        nodeStart = segments[0]
        nodeEnd = segments[1]
        weight = segments[2]

        graph.addLine(nodeStart, nodeEnd, weight)

        #print(nodeStart + " start")
        #print(nodeEnd + " end")
        #print(weight + " cost\n")
        #print(lines[index] + "\n")

    #print(graph.getGraph())
    #print("\n")
    return graph
    


# In[28]:

def writePath(fileName, path):
    # Write to output file
    outputFile = open(fileName, 'w')

    for node in path:
        outputFile.write(str(node) + "\n")

    outputFile.close()


# In[29]:

class Graph:
    
    def __init__(self):
        self.nodesList = []
        self.graph = {}      
    
    def getGraph(self):
        return self.graph;
    
    def getNodes(self):
        return self.nodesList;
    
    def setNodes(self, givenList):
        self.nodes_list = givenList
        
    def addLine(self, start, end, cost):
        if (start in self.graph):
            self.graph[start][end] = cost
        else:
            self.graph[start] = { end : cost }
            
        if (start not in self.nodesList):
            self.nodesList.append(start)
                    
        if (end not in self.nodesList):
            self.nodesList.append(end)     
                    


# In[30]:

# Makes a path from end to start and reverses it. 
def backtrace(graph, endNode, visited):
    backwardsPath = []
    curNode = endNode    
    tries = 0
    
    while (curNode in graph.getGraph()):
        #print(backwardsPath)
        
        nodes = list(graph.getGraph()[curNode].keys())
        
        if(tries < len(nodes)):        
            curNode = nodes[tries]            
        else:            
            #print("We got lost")
            break
                        
        #print(curNode)
        if (curNode in visited):
            
            if (curNode in backwardsPath):
                #print("Already Added")
                tries += 1
            else:
                backwardsPath.append(curNode)
                tries = 0
        else:
            #print("Not our parent")
            tries += 1
            
    if (len(backwardsPath) > 0):
        backwardsPath.insert(0, endNode)    
            
    backwardsPath.reverse()    
    return backwardsPath


# In[31]:

import heapq
def UCS(start, end, graph):
                  
    myGraph = graph.getGraph()
    parentsGraph = Graph()
    
    path = []
    tempPath = []
    
    #heap holds the paths with lowest cost
    heap = [[0, [start]]]
    
    visited = []
    parentNode = ''
    currentNode = start    
    currentWeight = 0
    #myQueue.append(currentNode)
    #print(myGraph)
    isFirst = True

    #queue.append(start)
    while (len(heap) != 0 or isFirst):
    #while (len(queue) != 0):
        
        currentTuple = heapq.heappop(heap)
        currentPath = currentTuple[-1]
        currentNode = currentPath[-1]
        currentWeight = currentTuple[0]
        #print("currentPath: " + str(currentPath))
        #print("currentNode: " + str(currentNode))
        #print("currentWeight: " + str(currentWeight))
        
        if (currentNode != end):
            
            #if (currentNode in visited):
            #    print("Already visited " + currentNode)
            #    continue
            
            if (currentNode in myGraph):
                #print("EXPLORING " + currentNode)
                #print(myGraph[currentNode])
                
                children = myGraph[currentNode]
                parentNode = currentNode
                
                for child in children:
                    #print(child)
                    weight = children[child]
                    parentsGraph.addLine(child, parentNode, weight)
                    currentPath.append(child)
                    #creates a shallow copy
                    tempPath = list(currentPath)
                    #print("CURPATH: " + str(currentPath))
                    #if (child == end):
                    #    print("DONE?")
                    #    path = currentPath
                    #    break
                    #else:
                        #print("CURPATH: " + str(tempPath))
                        #print("BEFOREHEAP: " + str(heap))
                    heapq.heappush(heap, [currentWeight + int(weight), tempPath])
                        #print("AFTERHEAP: " + str(heap))
                    currentPath.pop()
                    #print("CURHEAP: " + str(heap))
                    
                
                visited.append(currentNode)            
            #else:
                #print(currentNode)
                #print("NOT IN LIST")
            
        else:
            #reached end
            #print("END")
            path = currentPath
            break;
            
        #print("---------------")
        #print("heap: " + str(heap))
        #print("path: " + str(currentPath))
        #print("paths at level(" + str(level) + "): " + str(paths))
        #print("parentNode, currentNode: " + parentNode + ", " + str(currentNode))
        #print("parentGraph: " + str(parentsGraph.getGraph()))
        #print("---------------")
        isFirst = False
        
    #path = backtrace(parentsGraph, end, visited)
        
    #print("\n")
    
    return path


# In[65]:

#levels is a list containing lists of paths for each level
#paths is a list containing lists of paths for each parent/child combination
#path is a list of chars denoting a path

def BFS(start, end, graph):
            
    myGraph = graph.getGraph()
    parentsGraph = Graph()
    queue = [[start]]
    path = []
    visited = []
    parentNode = ''
    currentNode = start    
    #myQueue.append(currentNode)
    #print(myGraph)
    isFirst = True

    #queue.append(start)
    while (len(queue) != 0 or isFirst):
    #while (len(queue) != 0):
        
        currentPath = queue.pop(0)
        currentNode = currentPath[-1]
        
        if (currentNode != end):
            
            if (currentNode in visited):
                #print("Already visited " + currentNode)
                #path.pop(currentNode)
                continue
            
            if (currentNode in myGraph):
                #print("EXPLORING " + currentNode)
                #print(myGraph[currentNode])
                
                children = myGraph[currentNode]
                parentNode = currentNode
                
                for child in children:
                    tempPath = list(currentPath)
                    tempPath.append(child)
                    #print(child)
                    #parentsGraph.addLine(child, parentNode, 1)
                    #print("tempPath: " + str(tempPath))
                    queue.append(tempPath)
                
                visited.append(currentNode)   
                path.append(currentNode)
            else:
                #no op as in no operation. i just want this else here for future reference
                no_op = 0
                #print(currentNode)
                #print("NOT IN LIST")
            
        else:
            #reached end
            #print("END")
            path = currentPath
            break;
            
        #print("---------------")
        #print("queue: " + str(queue))
        #print("curPath: " + str(currentPath))
        #print("paths at level(" + str(level) + "): " + str(paths))
        #print("parentNode, currentNode: " + parentNode + ", " + currentNode)
        #print("parentGraph: " + str(parentsGraph.getGraph()))
        #print("---------------")
        isFirst = False
        
    #path = backtrace(parentsGraph, end, visited)
        
    #print("\n")
    
    return path


# In[66]:

def DFS(start, end, graph):
    
    path = []
    
    myGraph = graph.getGraph()
    parentsGraph = Graph()
    myStack = [[start]]
    visited = []
    parentNode = ''
    #myQueue.append(currentNode)
    #print(myGraph)
    isFirst = True
    tries = 0
    
    #print(graph.getNodes())
    
    isDone = False
    while (not isDone):
        
        if (len(visited) >= len(graph.getNodes())):
            #print("No path found")
            path = []
            isDone = True
        else:
            #currentNode = myStack.pop()
            currentPath = myStack.pop()
            currentNode = currentPath[-1]
            
                
        if (currentNode != end):
            
            if (currentNode in visited):
                #print("Already visited " + currentNode)
                #if (currentNode in path):
                #    path.pop(path.index(currentNode))                
                continue
            
            if (currentNode in myGraph):
                #print("EXPLORING " + currentNode)
                #print(myGraph[currentNode])
                
                children = myGraph[currentNode]
                parentNode = currentNode
                for child in children:
                    
                    #if (not(child in visited)):
                        
                        if (len(currentPath) > 0):
                            tempPath = list(currentPath)
                            tempPath.append(child)
                            #print(child)
                            #parentsGraph.addLine(child, parentNode, 1)
                            #print("tempPath: " + str(tempPath))
                            myStack.append(tempPath)

                            #print(child)
                            #parentsGraph.addLine(child, parentNode, 1)
                            #myStack.append(child)
                
                #path.append(currentNode)     
                visited.append(currentNode)
                       
            else:
                #print(currentNode)
                #print("NOT IN LIST")
                #currentNode = parentNode
                #if (currentNode in path):
                #    path.pop(path.index(currentNode))
                #myStack.append(parentNode)
                visited.append(currentNode)
                #tries += 1
            
        else:
            #reached end
            #print("END")
            #path.append(currentNode)
            path = currentPath
            break;
            
            
        #print("---------------")
        #print("myStack: " + str(myStack))
        #print("parentNode, currentNode: " + parentNode + ", " + currentNode)
        #print("parentGraph: " + str(parentsGraph.getGraph()))
        #print("path: " + str(path))
        #print("visited: " + str(visited))
        #print("---------------")
        isFirst = False
        
    
    #path = backtrace(parentsGraph, end, visited)
    #if ((start not in path) and (len(path) > 0)):
    #    path.insert(0, start)
    #print (path)
        
    #print("\n")
    
    return path


# In[70]:

import sys

def main():
    inputFileName = "graph.txt"
    outputFileName = "output.txt"
    startNode = "C"
    endNode = "B"
    searchType = "bfs"

    if (len(sys.argv) != 6):
        print("Invalid number of arguments: Search.py input output start stop search")
        exit(1)
    else:
        inputFileName = sys.argv[1]
        outputFileName = sys.argv[2]
        startNode = sys.argv[3]
        endNode = sys.argv[4]
        searchType = sys.argv[5]

    graph = loadFile(inputFileName)
    path = []
    if (searchType.upper() == "UCS"):
        path = UCS(startNode, endNode, graph)
    elif (searchType.upper() == "DFS"):
        path = DFS(startNode, endNode, graph)
    elif (searchType.upper() == "BFS"):
        path = BFS(startNode, endNode, graph)
    else:
        print("Search type should be bfs, dfs, or ucs")
        exit(1)
        
        
    if (len(path) == 0):
        print("No path could be found")
    else:
        writePath(outputFileName, path)
        print(path)
    

main()


# In[ ]:




# In[ ]:




# In[ ]:



