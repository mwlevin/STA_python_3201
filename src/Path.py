

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
    
    
        
    # returns True if this path represents a connected list of links, or False otherwise
    def isConnected(self):
        for x in range(1, len(self.links)):
            if self.links[x].start != self.links[x - 1].end:
                return False
        return True
    
    # returns the origin node of this path
    def getSource(self):
        return self.links[0].start
    
    # returns the destination node of this path
    def getDest(self):
        return self.links[-1].end
        
    # **********
    # Exercise 6(a)
    # **********   
    # returns the travel time of this path
    def getTravelTime(self):
        # fill this in
        return 0
        
    # **********
    # Exercise 3(a)
    # **********  
    def addHstar(self, h):
        # fill this in
        pass