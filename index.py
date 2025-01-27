import numpy as np

def n_transv(eps1,l1,eps2,l2):
    f = l2/(l1+l2)
    return(np.power((1-f)*eps1 + f*eps2,0.5)) 

def n_long(eps1,l1,eps2,l2):
    f = l2/(l1+l2)
    return(np.power((1-f)/eps1 + f/eps2,-0.5))

def n_transv_2(eps1,eps2,f):
    return(np.power((1-f)*eps1 + f*eps2,0.5)) 

def n_long_2(eps1,eps2,f):
    return(np.power((1-f)/eps1 + f/eps2,-0.5))

