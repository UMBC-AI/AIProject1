import sys
import copy
from collections import deque


# create a node object, and use link list to connect all of them togethor.
# Because next nodes of a node is more than one, so we create a array to store them. 
class node(object):
    name = ""
    nextnode = []
    weight = []
    

    def __init__(self, name):
        self.name = name
        self.nextnode = []
        self.weight = []

#DFS search
def DFS(allnodes, allnames, startnode, endnode, outputfilename):
    target = open(outputfilename, 'w')    
    thestart = allnodes[allnames.index(startnode)]
    theend = allnodes[allnames.index(endnode)]
    #Create a stack, because BFS is LIFO
    stack = []
    stack.append([thestart])
    newlist = []
    checked = []

    #Loop through the stack until it is empty
    while stack:
        # "path" store the final path.
        path = stack.pop(-1)
        thenode = path[-1]
        #if thenode has checked, skip
        if thenode in checked:
            continue

        else:
            checked.append(thenode)
            #Found the end node, BREAK.
           
            if thenode.name == theend.name:
                for i in path:
                    target.write(i.name)
                    target.write("\n")   
                break      
            #Check all the children nodes, if the node does not have children, skip.
            if not thenode.nextnode:
                continue
            del newlist[:]
            for i in thenode.nextnode:
                path2 = list(path)
                path2.append(i)
                newlist.append(path2)
            #reverse the list and append to stack
            newlist.reverse()
            for j in newlist:
                stack.append(j)
    target.close()

#BFS Search
def BFS(allnodes, allnames, startnode, endnode, outputfilename):
    target = open(outputfilename, 'w')    
    thestart = allnodes[allnames.index(startnode)]
    theend = allnodes[allnames.index(endnode)]
    #Create a queue, because BFS is FIFO
    queue = []
    queue.append([thestart])
    #Loop through the stack until it is empty
    while queue:
        # "path" store the final path.
        path = queue.pop(0)
        thenode = path[-1]
        #if thenode in checked:
            #continue
        #checked.add(thenode)
        #Found the end node, BREAK.
        if thenode.name == theend.name:
            for i in path:
                target.write(i.name)
                target.write("\n")   
            break      
        #Check all the children nodes.
        for i in thenode.nextnode:
            path2 = list(path)
            path2.append(i)
            queue.append(path2)
    target.close()
    
#UCS search
def UCS(allnodes, allnames, startnode, endnode, outputfilename):
    # open the output file
    target = open(outputfilename, 'w')    
    thestart = allnodes[allnames.index(startnode)]
    theend = allnodes[allnames.index(endnode)]
    
    checked = []
    ready = []

    nodeweight = {}
    nodepath = {}
    # give all nodes expect start node a very large weight, give start node a 0 weight. 
    for i in allnames:
        if i == startnode:
            nodeweight[i] = 0
            nodepath[i] = [i]
        else:
            nodeweight[i] = 100000
            nodepath[i] = []

    thenode = thestart
    # loop until checked all nodes.
    while len(checked) < len(allnames):
        checked.append(thenode.name)
        # look all the children of the node, update the weight. 
        for i in thenode.nextnode:
            ready.append(i.name)
            edge = thenode.weight[thenode.nextnode.index(i)]
            newweight = edge + nodeweight[thenode.name]
            # find a smaller weight, and update the path 
            if newweight < nodeweight[i.name]:
                nodeweight[i.name] = newweight
                
                a = copy.deepcopy(nodepath[thenode.name])
                a.append(i.name)
                
                nodepath[i.name] =a        
        for j in ready:
            if j in checked:
                ready.remove(j)
            else:
                thenode = allnodes[allnames.index(j)]
                ready.remove(j)
              
                break
    # if the path found, write on the output file.            
    if len(nodepath[endnode]) > 0:
    
        for i in nodepath[endnode]:
            target.write(i) 
            target.write("\n")          
        target.write(str(nodeweight[endnode])) 
        target.write("\n")   
        target.close()
    else:
        target.write("No path found")


        



#main function
def main():
    try:
        #get input from command line arguments. 
        inputfilename = sys.argv[1]
        outputfilename = sys.argv[2]
        startnode = sys.argv[3]
        endnode = sys.argv[4]
        searchtype = sys.argv[5]
        flag = True
    
        inputFile= open(inputfilename,"r")
    
        allnodes = []
        allnames= []
        #split every line and save in the allnodes and allnames
        for line in inputFile:
            mylist =line.strip().split(' ')   

            if mylist[0] in allnames:
                node1 = allnodes[allnames.index(mylist[0])]
            else:
                node1 = node(mylist[0])
                allnames.append(mylist[0])
                allnodes.append(node1)

            if mylist[1] in allnames:
                node2 = allnodes[allnames.index(mylist[1])]
            else:
                node2 = node(mylist[1])
                allnames.append(mylist[1])
                allnodes.append(node2)

            node1.nextnode.append(node2)
            node1.weight.append(int(mylist[2]))
        target = open(outputfilename, 'w')
        #call function based on user choice.    
        if searchtype == "DFS":
    	    DFS(allnodes, allnames, startnode, endnode, outputfilename)
        
        elif searchtype == "BFS":
         
            BFS(allnodes, allnames, startnode, endnode, outputfilename)
            

        elif searchtype == "UCS":
            UCS(allnodes, allnames, startnode, endnode, outputfilename)

        else:
            target.write("the type is not found")

        target.close()
        

    except:  
        print("Inputfile error or unexpected node")

main()




