

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
        self.xstar = 0
        self.start.addOutgoingLink(self)

    # updates the flow to the given value
    def setFlow(self, x):
        self.x = x
    
    def __repr__(self):
        return str(self)
        
    # **********
    # Exercise 1(a)
    # **********    
    def getTravelTime(self):
        t_ij = 0.0
        # fill this in
        return t_ij
        
        

        
    def __str__(self):
        return "("+str(self.start)+", "+str(self.end)+")"
        
    def addXstar(self, flow):
        self.xstar += flow
        
    # **********
    # Exercise 3(a)
    # **********   
    def calculateNewX(self, stepsize):
        # fill this in
        pass