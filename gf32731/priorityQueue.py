class PriorityQueue:

    elements = []
    
    def __init__(self):
        return

    def put(self,element):
        self.elements.append(element)

    def get(self):
        topElement = self.elements[0]
        for element in self.elements:
            if element[2] < topElement[2]:
                topElement = element
        
        self.elements.remove(topElement)
        return topElement

    def getQueue(self):
        return self.elements

    def contains(self,element):
        for e in self.elements:
            if e[0] == element:
                return True
        return False

    def getWeight(self,element):
        for e in self.elements:
            if e[0] == element:
                return e[2]

    def getElement(self,element):
        for e in self.elements:
            if e[0] == element:
                return e


    def updateElement(self,element,parent,weight):
        for e in self.elements:
            if e[0] == element:
                e[1] = parent
                e[2] = weight
