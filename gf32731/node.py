
class Node:


    def __init__(self, name, firstChild, firstChildWeight):
        self.name = ""
        self.children = {}
        self.name = name
        self.children[firstChild] = firstChildWeight

    def addChild(self, childName, childWeight):
        #Don't add yourself as a child
        if childName != self.name:
                self.children[childName] = childWeight

