from src import Node


class Zone(Node.Node):

    def __init__(self, id):
        super().__init__(id)
        self.demand = {}
        self.thruNode = True
    
    def addDemand(self, dest, dem):
        if dest in self.demand.keys():
            self.demand[dest] = self.demand[dest] + dem
        else:
            self.demand[dest] = dem
    
    # returns the number of trips from this node to the destination
    def getDemand(self, dest):
        if dest in self.demand.keys():
            return self.demand[dest]
        else:
            return 0
    
    def getProductions(self):
    
        total = 0.0
        
        for s in self.demand.keys():
            total += self.demand[s]
        
        return total
    
    def isThruNode(self):
        return self.thruNode
    
    # set a boolean indicating whether this node is a thru node
    def setThruNode(self, thru):
        self.thruNode = thru

