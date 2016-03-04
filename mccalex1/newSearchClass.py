#############################################################
# File name: Search.py
# Author: Alex McCaslin
# Date Modified: 2/4/16
#
# Description: Class made for BFS, DFS, and UCS
#              
#############################################################

import queue

class search:

    def __init__(self, theInputFile, theOutputFile, theStartNode, theEndNode):
        self.inputFile = theInputFile
        self.outputFile = theOutputFile
        self.startNode = theStartNode
        self.endNode = theEndNode

        self.myDict = {}

    def ReadFile(self):

        infile = open(self.inputFile, 'r')
        
        for line in infile:
            line = line.split()

            #line[0] holds key, line[1] holds neighboor, line[2] holds distance

            if(line[0] not in self.myDict):
                self.myDict[line[0]] = []
            self.myDict[line[0]].append((line[1], int(line[2]))) 
        

        infile.close()

    def WriteFile(self, nodeOrder):
        outFile = open(self.outputFile, 'w')
        for node in nodeOrder:
            outFile.write(node)
            outFile.write("\n")

        outFile.close()

    def DoBFS(self):

        nodeOrder = []
        nodeOrder.append(self.startNode)
        
        visitedNodes = []
        dictToTraverse = {}

        theQueue = []

        #if the start node is the node we are looking for end the program right there
        if(self.startNode == self.endNode):
            WriteFile(nodeOrder)
        
        else:
            currentNode = self.startNode
            theQueue.append(currentNode)

            while(len(theQueue) > 0):

                currentNode = theQueue.pop(0)
                visitedNodes.append(currentNode)

                #get the neighboors, check if its already been visited and not already in the queue
                if(currentNode in self.myDict):
                    for node in self.myDict[currentNode]:

                        if node[0] not in visitedNodes and node[0] not in theQueue:
                            dictToTraverse[node[0]] = currentNode

                            #if(node[0] in self.myDict or node[0] == self.endNode)
                            theQueue.append(node[0])

                        



            #traverse list backwards after finding the final node
            self.traverseList(dictToTraverse)

    def DoDFS(self):

        stack = []
        stack.append(self.startNode)

        alreadyVisited = []
        dictToTraverse = {}

        while len(stack) != 0:
            current = stack.pop(0)

            #makes sure you don't continue to get the same node
            if(current not in alreadyVisited):
                alreadyVisited.append(current)

                if(current in self.myDict):
                    #get the neighboors and set their paent nodes to current

                    for node in self.myDict[current]:
                        if node[0] not in alreadyVisited and node[0] not in stack:
                            dictToTraverse[node[0]] = current
                            
                            if(node[0] in self.myDict or node[0] == self.endNode):
                                #makes sure to append node to front for stack
                                stack = [node[0]] + stack

        self.traverseList(dictToTraverse)
        
    def DoUCS(self):

        nodeOrder = []
        nodeOrder.append(self.startNode)
        
        visitedNodes = []
        dictToTraverse = {}
        weights = {}
        theQueue = []

        weights[self.startNode] = 0
      
        #if the start node is the node we are looking for end the program right there
        if(self.startNode == self.endNode):
            WriteFile(nodeOrder)

        else:
            currentNode = self.startNode
            theQueue.append(currentNode)

            while(len(theQueue) > 0):                

                #get lowest weighted node
                for theNode in theQueue:
                    if(weights[theNode] < weights[currentNode]):
                        currentNode = theNode

                
                visitedNodes.append(currentNode)
                theQueue.remove(currentNode)

                #get the neighboors, check if its already been visited and not already in the queue
                if(currentNode in self.myDict):
                    for node in self.myDict[currentNode]:

                        #if node hasnt been visited
                        if node[0] not in visitedNodes:
                            if node[0] in theQueue:
                                if(weights[currentNode] + node[1] < weights[node[0]]):

                                    weights[node[0]] = weights[currentNode] + node[1]
                                    dictToTraverse[node[0]] = currentNode

                            #if the node isn't already in the queue
                            else:
                                weights[node[0]] = weights[currentNode] + node[1]
                                dictToTraverse[node[0]] = currentNode
                                theQueue.append(node[0])    


                #if theres still an item left get it for the next iteration
                if len(theQueue) > 0:
                    currentNode = theQueue[0]

            #traverse list backwards after finding the final node
            self.traverseList(dictToTraverse)


        

    def traverseList(self, dictToTraverse):
        
        if(self.startNode not in self.myDict):
            print("Why would you enter a start node that doesn't exist....exiting")
            exit(0)

        currentNode = self.endNode
        nodeList = []

        while currentNode != self.startNode:
            nodeList.append(currentNode)

            if(self.endNode in dictToTraverse):
                currentNode = dictToTraverse[nodeList[-1]]
            else:
                currentNode = self.startNode
                
            if(dictToTraverse[nodeList[-1]] == self.startNode):
                nodeList.append(self.startNode)

        self.WriteFile(nodeList[::-1])
        
        

