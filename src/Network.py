


class Network:

    # construct this Network with the name; read files associated with network name
    def __init__(self, name):
        # list of nodes, each node is an integer id. First node is id 1
        self.nodes = [] 
        
        # list of links, each link is a tuple e.g. (1,2)
        self.links = []
        
        # link parameters: free flow speed t_ff, alpha, beta, capacity C all mapped to link tuples
        self.alpha = dict()
        self.beta = dict()
        self.t_ff = dict()
        self.C = dict()
        
        
        # flow on link
        self.x = dict()
        
        # this might be useful for storing xstar
        self.xstar = dict()
        
        # list of zones, each zone is an integer id
        self.zones = []
        
        # demand is a dict based on tuple (r,s)
        self.demand = dict()
        self.name = name
        
    def readFiles(self):
        
        self.readNetwork("data/" + self.name + "/net.txt")
        self.readTrips("data/" + self.name + "/trips.txt")
        
    # read file "/net.txt"
    def readNetwork(self, netFile):
        firstThruNode = 1
        numZones = 0
        numNodes = 0
        numLinks = 0
        
        file = open(netFile, "r")

        line = ""
        
        while line.strip() != "<END OF METADATA>":
            line = file.readline()
            
            if "<NUMBER OF ZONES>" in line:
            
                numZones = int(line[line.index('>') + 1:].strip());
            
            elif "<NUMBER OF NODES>" in line:
                numNodes = int(line[line.index('>') + 1:].strip())
            elif "<NUMBER OF LINKS>" in line:
                numLinks = int(line[line.index('>') + 1:].strip())
            elif "<FIRST THRU NODE>" in line:
                firstThruNode = int(line[line.index('>') + 1:].strip())

        for i in range(0, numZones):
            self.zones.append(i+1)

        for i in range(0, numNodes):
            if i < numZones:
                self.nodes.append(i+1)
            else:
                self.nodes.append(i + 1)

        line = ""
        while len(line) == 0:
            line = file.readline().strip()
        
        for i in range(0, numLinks):
            line = file.readline().split()
            
            start = int(line[0])
            end = int(line[1])
            link = (start, end)
            self.links.append(link)
            
            C = float(line[2])

            t_ff = float(line[4])
            alpha = float(line[5])
            beta = float(line[6])
            
            self.beta[link] = beta
            self.C[link] = C
            self.alpha[link] = alpha
            self.t_ff[link] = t_ff
            
        file.close()
        
        
        for i in self.links:
            self.x[i] = 0
            self.xstar[i] = 0
        
    def readTrips(self, tripsFile):

        file = open(tripsFile, "r")
        
        lines = file.readlines()
        
        line_idx = 0
        
        while lines[line_idx].strip() != "<END OF METADATA>":
            line_idx += 1
            
        line_idx += 1
        
        while lines[line_idx].strip() == "":
            line_idx += 1
            
        r = None
        
        idx = 0
        
        splitted = lines[line_idx].split()
        
        while len(lines) < line_idx or idx < len(splitted):

            next = splitted[idx]
            if next == "Origin":
                idx += 1
                r = int(splitted[idx])
            else:
                s = int(splitted[idx])
                idx += 2
                next = splitted[idx]
                d = float(next[0:len(next) - 1])
                
                self.demand[(r,s)] = d
                
            idx += 1
            if idx >= len(splitted):
                line_idx += 1
                while line_idx < len(lines) and lines[line_idx].strip() == "":
                    line_idx += 1
                    
                if line_idx < len(lines):
                    line = lines[line_idx].strip()
                    splitted = line.split()
                    idx = 0
            
        file.close()
        
    def getOutgoing(self, i):
        # return all outgoing links from i
        output = []
        
        for ij in self.links:
            if ij[0] == i:
                output.append(ij)
        return output
        
    def isConnected(self, path):
        for i in range(0, len(path)-1):
            if path[i][1] != path[i+1][0]:
                return False
        return True
        
        
    def getDemand(self, r, s):
        return self.demand[(r,s)]
    
    
    
    
    
    # **********
    # Exercise 1(a)
    # ********** 
    def getTravelTime(self, link):
        
        
        # link is a tuple, e.g. (1,2)
        # use link parameters self.t_ff, self.alpha, self.C, etc.
        
        
        # fill this in
        return 0
        
 
    # **********
    # Exercise 1(b)
    # ********** 
    # returns the total system travel time
    def getTSTT(self):
        # fill this in
        return 0
        
        
        
        
    # **********
    # Exercise 2(a)
    # **********     
    def getPathTravelTime(self, path):
        # path is a list of links
        # each link is a tuple e.g. (1,2)
        return 0
        
        

    

    

    # returns the total system travel time if all demand is on the shortest path
    def getSPTT(self):
        output = 0.0

        for r in self.zones:
            cost, pred = self.dijkstras(r)

            for s in self.zones:
                if self.demand[(r,s)] > 0:
                    output += self.demand[(r,s)] * cost[s]

        return output

    # returns the total number of trips in the network
    def getTotalTrips(self):
        output = 0.0

        for (r, s) in self.demand.keys():
            output += self.demand[(r,s)]

        return output

    # returns the average excess cost
    def getAEC(self):
        return (self.getTSTT() - self.getSPTT()) / self.getTotalTrips()
        
        
    
        
        
   
        
        
        
    def dijkstras(self, origin):
        cost = {i:0 for i in self.nodes}
        pred = {i:None for i in self.nodes}
        
        
        # **********
        # Exercise 2(b)
        # ********** 

        # fill this in

        # **********
        # Exercise 2(c)
        # ********** 
        
        # fill this in
        
        
        
        
        
        return cost, pred
  
    # **********
    # Exercise 2(d)
    # ********** 

    def trace(self, r, s):
        output = []
        # add links to path!
        
        # fill this in
    
    
    
        
        return output
    
    
    # **********
    # Exercise 3(a)
    # ********** 
    # calculate the all-or-nothing assignment
    def calculateAON(self):
        # fill this in
        # I recommend checking whether r to s demand > 0; if not, don't run shortest path.
        
        # if there is no demand from r to s, there may not be a path and calling trace() could crash. Check: if self.getDemand(r, s) > 0
        pass    
    
    # **********
    # Exercise 3(b)
    # **********
    # calculate the step size for given iteration
    def calculateStepsize(self, iteration):
        # fill this in
        return 0


    # **********
    # Exercise 3(b)
    # ********** 
    # calculate the new X for all links based on the given step size
    def calculateNewX(self, stepsize):
        # fill this in
        pass

    


    def msa(self, max_iteration):

        output = "Iteration\tAEC\n"

        for iteration in range(1, max_iteration + 1):
            
            # **********
            # Exercise 3(c)
            # ********** 
            
            
            
            
            
            # how far are we from UE?
            aec = self.getAEC()
            
            output += str(iteration) + "\t" + str(self.getAEC()) + "\n"
        
        
        print("\nlink flows after MSA")
        for ij in self.links:
            print("\t", ij, self.x[ij])
        
        
        return output

