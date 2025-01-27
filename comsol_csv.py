# code for ploting data from COMSOL export txt
import numpy as np

def csv(path,lmin = None,lmax = None,cmin = None,cmax = None,start=4):
    with open(path) as doc:
        lines = doc.readlines()
    lines=lines[start:]
    doc.close()
    for i in range(len(lines)):
        if i>=0:
            lines[i]=lines[i].replace("i","j")
            lines[i]=lines[i].replace("True","1")
            lines[i]=lines[i].replace("False","0")
            lines[i]=lines[i].strip("\n")
            lines[i]=lines[i].split(",")
    Tab = np.array(lines[:]).astype(np.complex128).T
    return(Tab[lmin:lmax,cmin:cmax])

