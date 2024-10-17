

class Path:
    # construct this Path; it contains a list of links representing the links in this path
    def __init__(self):
        self.links = []
        
    def add(self, ij):
        self.links.append(ij)
    
    def addFront(self, ij):
        self.links.insert(0, ij)
        
    def size(self):
        return len(self.links)
        
    def __str__(self):
        return str(self.links)
    
    # **********
    # Exercise 6(a)
    # **********   
    # returns the travel time of this path
    def getTravelTime(self):
        # fill this in
        return 0
        
    # returns True if this path represents a connected list of links, or False otherwise
    def isConnected(self):
        # fill this in
        return False
    
    # returns the origin node of this path
    def getSource(self):
        # fill this in
        return None
    
    # returns the destination node of this path
    def getDest(self):
        # fill this in
        return None
        
    # **********
    # Exercise 8(a)
    # **********  
    def addHstar(self, h):
        # fill this in
        pass