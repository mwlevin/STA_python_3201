from autograde import Autograde
from src import Network


def test():

    test = Network.Network("test only")
    
    test.beta[(1,2)] = 4
    test.t_ff[(1,2)] = 10
    test.C[(1,2)] = 2580
    test.alpha[(1,2)] = 0.15
    
    test.beta[(2,3)] = 4
    test.t_ff[(2,3)] = 12
    test.C[(2,3)] = 1900
    test.alpha[(2,3)] = 0.35
    

    test.x[(1,2)] = 1320.2
    test.x[(2,3)] = 570
    print("link 1 TT with flow 1320.2", test.getTravelTime((1,2)))

    print("link 2 TT with flow 570", test.getTravelTime((2,3)))


    test.x[(1,2)] = 0
    test.x[(2,3)] = 2512

    print("link 1 TT with flow 0", test.getTravelTime((1,2)))
    print("link 2 TT with flow 2512", test.getTravelTime((2,3)))
    
    network = Network.Network("SiouxFalls")
                
        
    for i in test.links:
        test.x[i] = 1021 + i * 500
        
    print("TSTT", test.getTSTT())
 
        
    autograde()
    
    
def autograde():
    auto = Autograde.Autograde()
    
    test = Network.Network("test only")
    
    test.beta[(1,2)] = 4
    test.t_ff[(1,2)] = 10
    test.C[(1,2)] = 2580
    test.alpha[(1,2)] = 0.15
    
    test.beta[(2,3)] = 4
    test.t_ff[(2,3)] = 12
    test.C[(2,3)] = 1900
    test.alpha[(2,3)] = 0.35
    
    test.x[(1,2)] = 1320.2
    test.x[(2,3)] = 570
    auto.test(abs(test.getTravelTime((1,2)) - 10.077538130554997) < 0.01)

    auto.test(abs(test.getTravelTime((2,3)) - 12.378) < 0.01)
        
    test.x[(1,2)] = 0
    test.x[(2,3)] = 2512
        

    auto.test(abs(test.getTravelTime([(1,2)]) - 10.0) < 0.01)
    auto.test(abs(test.getTravelTime((2,3)) - 19.341441772853184) < 0.01)
    
    auto.flush("1(a): Link.getTravelTime()"); 
    
    
    

    test = Network.Network("SiouxFalls")
    test.readFiles()


    for i in range(0, len(test.links)):
        test.x[i] = 1021 + i * 500
    
    auto.test(abs(test.getTSTT() - 8.007500975406816E8) < 1)

    auto.flush("1(b): getTSTT()")


    auto.end()
        
