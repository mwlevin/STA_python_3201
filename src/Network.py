from src import Node
from src import Link
from src import Path
from src import Zone


class Network:

    # construct this Network with the name; read files associated with network name
    def __init__(self, name):
        self.nodes = [] 
        self.links = []
        self.zones = []
        self.readNetwork("data/" + name + "/net.txt")
        self.readTrips("data/" + name + "/trips.txt")
        
    # read file "/net.txt"
    def readNetwork(self, netFile):
        # **********
        # Exercise 5(b)
        # ********** 
        
        # **********
        # Exercise 5(c)
        # ********** 
        
        # **********
        # Exercise 5(d)
        # ********** 
        
        # fill this in
        pass
        
    def readTrips(self, tripsFile):

        # **********
        # Exercise 5(d)
        # ********** 
        
        # fill this in
        pass

    def getLinks(self):
        return self.links
    
    def getNodes(self):
        return self.nodes
    
    def getZones(self):
        return self.zones

    # **********
    # Exercise 5(e)
    # ********** 
    # find the node with the given id
    def findNode(self, id):
        # fill this in
        return None

    # find the link with the given start and end nodes
    def findLink(self, i, j):
        # fill this in
        return None

 

    def dijkstras(self, origin):
        # **********
        # Exercise 6(b)
        # ********** 

        # fill this in

        # **********
        # Exercise 6(c)
        # ********** 
        
        # fill this in
        pass
  
    # **********
    # Exercise 6(d)
    # ********** 

    def trace(self, r, s):
        # fill this in
        return None

    # **********
    # Exercise 7
    # ********** 
    # returns the total system travel time
    def getTSTT(self):
        # fill this in
        return 0

    # returns the total system travel time if all demand is on the shortest path
    def getSPTT(self):
        # fill this in
        return 0

    # returns the total number of trips in the network
    def getTotalTrips(self):
        # fill this in
        return 0

    # returns the average excess cost
    def getAEC(self):
        # fill this in
        return 0

    # **********
    # Exercise 8(a)
    # ********** 
    # find the step size for the given iteration number
    def calculateStepsize(self, iteration):
        # fill this in
        return 0

    # **********
    # Exercise 8(b)
    # ********** 
    # calculate the new X for all links based on the given step size
    def calculateNewX(self, stepsize):
        # fill this in
        pass

    # **********
    # Exercise 8(c)
    # ********** 
    # calculate the all-or-nothing assignment
    def calculateAON(self):
        # fill this in
        pass

    # **********
    # Exercise 8(d)
    # ********** 
    def msa(self, max_iteration):
        # fill this in
        return ""

