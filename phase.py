# code to manage phase wrapping :)
import numpy as np

def re_wrap(phases_list,phi0,norm=False):
    phases = np.array(phases_list)
    phases = (phases-phases[0]+phi0)%(2*np.pi)
    if norm == True:
        phases/=(2*np.pi)
    return(phases)

def shift(phases_list,delta_phi,norm=False):
    phases = np.array(phases_list)
    phases = (phases+delta_phi)%(2*np.pi)
    if norm == True:
        phases/=(2*np.pi)
    return(phases)

def detect_jump(phases_list, delta_phi_thresh=0.9*2*np.pi):
    cd=False
    phases=np.array(phases_list)
    for i in range(np.shape(phases)[0]-1):
        if np.abs(phases[i+1]-phases[i])>=delta_phi_thresh:
            cd=True
    return(cd)

def fix_jump(phases_list, delta_phi_thresh=0.9*2*np.pi):
    phases=np.array(phases_list)
    for i in range(np.shape(phases)[0]-1):
        if np.abs(phases[i+1]-phases[i])>=delta_phi_thresh:
            if(phases[i+1]-phases[i])>0:
                phases[i+1:]-=2*np.pi
            else:
                phases[i+1:]+=2*np.pi
    return(phases)
