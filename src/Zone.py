from src import Node


class Zone(Node.Node):

    # **********
    # Exercise 4(a)
    # ********** 
    def __init__(self, id):
        # add instance variables as needed
        pass
    
    # **********
    # Exercise 4(b)
    # ********** 
    # adds the specified demand to an internal data structure for the demand from this node to the destination
    def addDemand(self, dest, dem):
        # fill this in
        pass
    
    # returns the number of trips from this node to the destination
    def getDemand(self, dest):
        # fill this in
        return 0
    
    # **********
    # Exercise 4(c)
    # ********** 
    # returns the total number of outgoing trips from this node
    def getProductions(self):
        # fill this in
        return 0
    
    # **********
    # Exercise 4(d)
    # ********** 
    # returns aboolean indicating whether this node is a thru node
    def isThruNode(self):
        # fill this in
        return False
    
    # set a boolean indicating whether this node is a thru node
    def setThruNode(self, thru):
        # fill this in
        pass

