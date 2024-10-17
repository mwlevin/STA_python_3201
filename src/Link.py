

class Link:

    # construct this Link with the given parameters
    def __init__(self, start, end, t_ff, C, alpha, beta):
        self.start = start
        self.end = end
        self.t_ff = t_ff
        self.C = C
        self.alpha = alpha
        self.beta = beta
        self.x = 0

    # updates the flow to the given value
    def setFlow(self, x):
        self.x = x
    
    def __repr__(self):
        return str(self)
        
    # **********
    # Exercise 1
    # **********    
    def getTravelTime(self):
        t_ij = 0.0
        # fill this in
        return t_ij
        
    # **********
    # Exercise 2(a)
    # **********
    def getCapacity(self):
        # fill this in
        return 0
    
    def getFlow(self):
        # fill this in
        return 0
        
    # **********
    # Exercise 3(a)
    # **********  
    def getStart(self):
        # fill this in
        return None
    
    def getEnd(self):
        # fill this in
        return None
        
    # **********
    # Exercise 3(c)
    # **********   
    def __str__(self):
        # fill this in
        return ""
        
    # **********
    # Exercise 8(a)
    # **********   
    def addXstar(self, flow):
        # fill this in
        pass
        
    # **********
    # Exercise 8(b)
    # **********   
    def calculateNewX(self, stepsize):
        # fill this in
        pass