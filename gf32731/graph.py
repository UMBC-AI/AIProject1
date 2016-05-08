import queue
from priorityQueue import PriorityQueue
from node import Node

class Graph:

    graph = []
    buildList = []
    start = ""
    end = ""

    
    def __init__(self, inputFile, start, end):
        myFile = open(inputFile)
        lines = myFile.readlines()
        self.start = start
        self.end = end
        for line in lines:
            self.addLine(line)
            
    def addLine(self,line):
        data = line.split(" ")
        data[2] = int(data[2].rstrip())
        if not data[0] in self.buildList:
#            print("CREATING NODE",data[0],"WITH CHILD ->",data[1])
            n = Node(data[0],data[1],data[2])
            self.graph.append(n)
            self.buildList.append(data[0])
        else:
#            print("ADDING CHILD",data[0],"->",data[1])
            n = self.findNode(data[0])
            n.addChild(data[1],data[2])

    def findNode(self, name):
        for node in self.graph:
            if node.name == name:
                return node
        return None
    
    #Breadth First Search
    def solveBFS(self):
#        return ["A","B","C"]
        visited = [self.start]
        q = queue.Queue()
        if self.start == self.end:
            print("Graph already solved! start and end nodes are the same!")
        else:
            #Build Queue
            startNode = self.findNode(self.start)
            for child in startNode.children:
                print("ADDING",child,"PARENT",startNode.name)
                q.put((child,startNode.name))
                visited.append(child)

            #Recursively solve
            path = []
            self.rsolveBFS(q,path,visited)
            path.append(self.start)
            return path
            
    #Recursive call for BFS
    def rsolveBFS(self,myQueue,path,visited):
        data = myQueue.get()
        currName = data[0]
        parent = data[1]
        print("EXPLORING",currName,"FROM PARENT",parent)
        currentNode = self.findNode(currName)

        #check for goal node
        if currName == self.end:
            print("GOAL IDENTIFIED, RETURNING...",parent)
            path.append(currName)
            return parent

        #Check for node with children
        if currentNode != None:


            #Current node is not the final node, add all connected nodes to the queue
            for child in currentNode.children:
                if not child in visited:
                    print("ADDING",child,"TO QUEUE")
                    myQueue.put((child,currentNode.name))
                    visited.append(child)

        #Recurse and further solve, take solution's parent
        ans = self.rsolveBFS(myQueue,path,visited)

        print("TESTING PARENT",currName,"AGAINST TARGET PARENT",ans)

        #Is the current node on the path back? If so, return that node's parent,
        if ans == currName:
            print(ans,"==",currName)
            path.append(currName)
            return parent
        #Otherwise return the current parent needed for the path.
        else:
            return ans

    def solveDFS(self):
#        return ["A","B","C"]
        visited = [self.start]
        stack = []
        if self.start == self.end:
            print("Graph already solved! start and end nodes are the same!")
        else:
            #Build Queue
            startNode = self.findNode(self.start)
            for child in startNode.children:
                print("ADDING ",child,"PARENT",startNode.name)
                stack.append((child,startNode.name))
                visited.append(child)

            #Recursively solve
            path = []
            self.rsolveDFS(stack,path,visited)
            path.append(self.start)
            return path
            
    #Recursive call for BFS
    def rsolveDFS(self,myStack,path,visited):
        data = myStack.pop()
        currName = data[0]
        parent = data[1]
        print("EXPLORING",currName,"FROM PARENT",parent)
        currentNode = self.findNode(currName)

        #check for goal node
        if currName == self.end:
            print("GOAL IDENTIFIED, RETURNING...",parent)
            path.append(currName)
            return parent

        #Check for node with children
        if currentNode != None:


            #Current node is not the final node, add all connected nodes to the queue
            for child in currentNode.children:
                if not child in visited:
                    print("ADDING",child,"TO STACK")
                    myStack.append((child,currentNode.name))
                    visited.append(child)

        #Recurse and further solve, take solution's parent
        ans = self.rsolveDFS(myStack,path,visited)

        print("TESTING PARENT",currName,"AGAINST TARGET PARENT",ans)

        #Is the current node on the path back? If so, return that node's parent,
        if ans == currName:
            print(ans,"==",currName,"ADDING TO SOLVED PATH")
            path.append(currName)
            return parent
        #Otherwise return the current parent needed for the path.
        else:
            return ans


    def solveUCS(self):
#        return ["A","B","C"]
        visited = [self.start]
        q = PriorityQueue()
        if self.start == self.end:
            print("Graph already solved! start and end nodes are the same!")
        else:
            #Build Queue
            startNode = self.findNode(self.start)
            for child in startNode.children:
                print("ADDING",child,"PARENT",startNode.name)
                q.put((child,startNode.name,startNode.children[child]))
                visited.append(child)

            #Recursively solve
            path = []
            self.rsolveUCS(q,path,visited)
            path.append(self.start)
            return path
            
    #Recursive call for BFS
    def rsolveUCS(self,myQueue,path,visited):
        data = myQueue.get()
        currName = data[0]
        parent = data[1]
        parentWeight = data[2]
        print("EXPLORING",currName,"FROM PARENT",parent)
        currentNode = self.findNode(currName)

        #check for goal node
        if currName == self.end:
            print("GOAL IDENTIFIED, RETURNING...",parent)
            path.append(currName)
            return parent

        #Check for node with children
        if currentNode != None:


            #Current node is not the final node, add all connected nodes to the queue
            for child in currentNode.children:
                if not child in visited:
                    print("ADDING",child,"TO QUEUE")
                    newWeight = currentNode.children[child]+parentWeight
                    myQueue.put((child,currentNode.name,newWeight))
                    visited.append(child)

        #Recurse and further solve, take solution's parent
        ans = self.rsolveUCS(myQueue,path,visited)

        print("TESTING PARENT",currName,"AGAINST TARGET PARENT",ans)

        #Is the current node on the path back? If so, return that node's parent,
        if ans == currName:
            print(ans,"==",currName)
            path.append(currName)
            return parent
        #Otherwise return the current parent needed for the path.
        else:
            return ans
