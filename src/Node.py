

class Node:

    # construct this Node with the given id
    def __init__(self, id):
        # used for Dijkstra's implementation
        self.cost = 0.0
        self.predecessor = None
        self.id = id
        self.outgoing = []
        
    def __repr__(self):
        return str(self)
        
    # returns True if this node is a thru node
    def isThruNode(self):
        return True
    
    # will be overriden in Zone class to return non-zero demand
    def getDemand(self, s):
        return 0
      
    # will be overriden in Zone class to return non-zero demand  
    def addDemand(self, dest, dem):
        pass
        
    def getProductions(self):
        return 0
        
    def __str__(self):
        return str(self.id)
    
    # adds ij to list of outgoing links
    def addOutgoingLink(self, ij):
        if ij.start == self:
            self.outgoing.append(ij)
