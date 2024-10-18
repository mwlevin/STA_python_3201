from autograde import Autograde
from src  import Link
from src import Node
from src import Path
from src import Network


def test():

    node1 = Node.Node(1)
    node2 = Node.Node(2)
    node3 = Node.Node(3)
    
    link1 = Link.Link(node1, node2, 10, 2580, 0.15, 4)
    link2 = Link.Link(node2, node3, 12, 1900, 0.35, 2)

    link1.setFlow(1320.2)
    print("link 1 TT with flow 1320.2", link1.getTravelTime())

    link2.setFlow(570)
    print("link 2 TT with flow 570", link2.getTravelTime())

    link1.setFlow(0)
    link2.setFlow(2512)

    print("link 1 TT with flow 0", link1.getTravelTime())
    print("link 2 TT with flow 2512", link2.getTravelTime())
    
    network = Network.Network("SiouxFalls")
                
    links = network.getLinks()
        
    for i in range(0, len(links)):
        links[i].setFlow(1021 + i * 500)
        
    print("TSTT", network.getTSTT())
 
        
    autograde()
    
    
def autograde():
    auto = Autograde.Autograde()
    
    
    
    node1 = Node.Node(1)
    node2 = Node.Node(2)
    node3 = Node.Node(3)
    
    link1 = Link.Link(node1, node2, 10, 2580, 0.15, 4)
    link2 = Link.Link(node2, node3, 12, 1900, 0.35, 2)


    link1.setFlow(1320.2)
    auto.test(abs(link1.getTravelTime() - 10.077538130554997) < 0.01)

    auto.test(abs(link2.getTravelTime() - 12.378) < 0.01)
        
    link1.setFlow(0)
    link2.setFlow(2512)
        

    auto.test(abs(link1.getTravelTime() - 10.0) < 0.01)
    auto.test(abs(link2.getTravelTime() - 19.341441772853184) < 0.01)
    
    auto.flush("1(a): Link.getTravelTime()"); 
    
    
    

    network = Network.Network("SiouxFalls")

    links = network.getLinks()

    for i in range(0, len(links)):
        links[i].setFlow(1021 + i * 500)
    
    auto.test(abs(network.getTSTT() - 8.007500975406816E8) < 1)

    auto.flush("1(b): getTSTT()")


    auto.end()
        
