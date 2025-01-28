# code for ploting data from COMSOL export txt
import numpy as np

def csv(path,lmin = None,lmax = None,cmin = None,cmax = None,start=4, split=',',i_to_j=True, coma_to_point=False, point_to_coma=False):
    with open(path) as doc:
        lines = doc.readlines()
    lines=lines[start:]
    doc.close()
    for i in range(len(lines)):
        if i>=0:
            if i_to_j:
                lines[i]=lines[i].replace("i","j")
            if coma_to_point:
                lines[i]=lines[i].replace(",",".")
            if point_to_coma:
                lines[i]=lines[i].replace(",",".")
            lines[i]=lines[i].replace("True","1")
            lines[i]=lines[i].replace("False","0")
            lines[i]=lines[i].strip("\n")
            lines[i]=lines[i].split(split)
    Tab = np.array(lines[:]).astype(np.complex128).T
    return(Tab[lmin:lmax,cmin:cmax])

