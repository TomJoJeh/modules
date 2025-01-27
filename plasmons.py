import numpy as np

def plasmon_disp(Lambda, eps_m, eps_d):
    k0 = 2*np.pi/Lambda
    return(k0*np.sqrt(eps_d*eps_m/(eps_d+eps_m)))