import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def epsAg(l):
    file = pd.read_excel('/Users/tomjoly-jehenne/Documents/GitHub/modules/database/Ag.xlsx')
    data = np.array(file).T
    list_lambd_m = data[0]*1e-6
    list_eps_m = (data[1]+1j*data[2])**2
    list_n_m = data[1]
    argm = np.searchsorted(list_lambd_m,l)
    eps_m = (list_eps_m[argm]-list_eps_m[argm-1])*(l-list_lambd_m[argm-1]) / (list_lambd_m[argm]-list_lambd_m[argm-1]) + list_eps_m[argm-1]
    return(eps_m)

def epsAl(l):
    file = pd.read_excel('/Users/tomjoly-jehenne/Documents/GitHub/modules/database/Al.xlsx')
    data = np.array(file).T
    list_lambd_m = data[0]*1e-6
    list_eps_m = (data[1]+1j*data[2])**2
    list_n_m = data[1]
    argm = np.searchsorted(list_lambd_m,l)
    eps_m = (list_eps_m[argm]-list_eps_m[argm-1])*(l-list_lambd_m[argm-1]) / (list_lambd_m[argm]-list_lambd_m[argm-1]) + list_eps_m[argm-1]
    return(eps_m)

def epsAlumina(l):
    file2 = pd.read_excel('/Users/tomjoly-jehenne/Documents/GitHub/modules/database/Alumina.xlsx')
    data2 = np.array(file2).T
    list_lambd_d = data2[0]*1e-6
    list_eps_d = (data2[1]+1j*data2[2])**2
    list_n_d = data2[1]
    argd = np.searchsorted(list_lambd_d,l)
    eps_d = (list_eps_d[argd]-list_eps_d[argd-1])*(l-list_lambd_d[argd-1]) / (list_lambd_d[argd]-list_lambd_d[argd-1]) + list_eps_d[argd-1]
    return(eps_d)

def epsAu(l):
    file = pd.read_excel('/Users/tomjoly-jehenne/Documents/GitHub/modules/database/Au.xlsx')
    data = np.array(file).T
    list_lambd_m = data[0]*1e-6
    list_eps_m = (data[1]+1j*data[2])**2
    list_n_m = data[1]
    argm = np.searchsorted(list_lambd_m,l)
    eps_m = (list_eps_m[argm]-list_eps_m[argm-1])*(l-list_lambd_m[argm-1]) / (list_lambd_m[argm]-list_lambd_m[argm-1]) + list_eps_m[argm-1]
    return(eps_m)

def nAg(l):
    file = pd.read_excel('/Users/tomjoly-jehenne/Documents/GitHub/modules/database/Ag.xlsx')
    data = np.array(file).T
    list_lambd_m = data[0]*1e-6
    list_n_m = (data[1]+1j*data[2])
    argm = np.searchsorted(list_lambd_m,l)
    n_m = (list_n_m[argm]-list_n_m[argm-1])*(l-list_lambd_m[argm-1]) / (list_lambd_m[argm]-list_lambd_m[argm-1]) + list_n_m[argm-1]
    return(n_m)

def nAlumina(l):
    file2 = pd.read_excel('/Users/tomjoly-jehenne/Documents/GitHub/modules/database/Alumina.xlsx')
    data2 = np.array(file2).T
    list_lambd_d = data2[0]*1e-6
    list_n_d = (data2[1]+1j*data2[2])
    argm = np.searchsorted(list_lambd_d,l)
    n_d = (list_n_d[argm]-list_n_d[argm-1])*(l-list_lambd_d[argm-1]) / (list_lambd_d[argm]-list_lambd_d[argm-1]) + list_n_d[argm-1]
    return(n_d)

def nAl(l):
    file = pd.read_excel('/Users/tomjoly-jehenne/Documents/GitHub/modules/database/Al.xlsx')
    data = np.array(file).T
    list_lambd_m = data[0]*1e-6
    list_n_m = (data[1]+1j*data[2])
    argm = np.searchsorted(list_lambd_m,l)
    n_m = (list_n_m[argm]-list_n_m[argm-1])*(l-list_lambd_m[argm-1]) / (list_lambd_m[argm]-list_lambd_m[argm-1]) + list_n_m[argm-1]
    return(n_m)

def nSi(l):
    file = pd.read_excel('/Users/tomjoly-jehenne/Documents/GitHub/modules/database/Si.xlsx')
    data = np.array(file).T
    list_lambd_m = data[0]*1e-6
    list_n_m = (data[1]+1j*data[2])
    argm = np.searchsorted(list_lambd_m,l)
    n_m = (list_n_m[argm]-list_n_m[argm-1])*(l-list_lambd_m[argm-1]) / (list_lambd_m[argm]-list_lambd_m[argm-1]) + list_n_m[argm-1]
    return(n_m)

def epsSi(l):
    file = pd.read_excel('/Users/tomjoly-jehenne/Documents/GitHub/modules/database/Si.xlsx')
    data = np.array(file).T
    list_lambd_m = data[0]*1e-6
    list_eps_m = (data[1]+1j*data[2])**2
    list_n_m = data[1]
    argm = np.searchsorted(list_lambd_m,l)
    eps_m = (list_eps_m[argm]-list_eps_m[argm-1])*(l-list_lambd_m[argm-1]) / (list_lambd_m[argm]-list_lambd_m[argm-1]) + list_eps_m[argm-1]
    return(eps_m)   

def nSiO2(l):
    file = pd.read_excel('/Users/tomjoly-jehenne/Documents/GitHub/modules/database/SiO2.xlsx')
    data = np.array(file).T
    list_lambd_m = data[0]*1e-6
    list_n_m = (data[1]+1j*data[2])
    argm = np.searchsorted(list_lambd_m,l)
    n_m = (list_n_m[argm]-list_n_m[argm-1])*(l-list_lambd_m[argm-1]) / (list_lambd_m[argm]-list_lambd_m[argm-1]) + list_n_m[argm-1]
    return(n_m)

def epsSiO2(l):
    file = pd.read_excel('/Users/tomjoly-jehenne/Documents/GitHub/modules/database/SiO2.xlsx')
    data = np.array(file).T
    list_lambd_m = data[0]*1e-6
    list_eps_m = (data[1]+1j*data[2])**2
    list_n_m = data[1]
    argm = np.searchsorted(list_lambd_m,l)
    eps_m = (list_eps_m[argm]-list_eps_m[argm-1])*(l-list_lambd_m[argm-1]) / (list_lambd_m[argm]-list_lambd_m[argm-1]) + list_eps_m[argm-1]
    return(eps_m)   

def mirror_Al_F01(Lambda):
    """
    returns reflectance of Thorlabs F01 Al miror
    Lambda : wavelength in micrometer
    """
    Tab=np.array(pd.read_excel("/Users/tomjoly-jehenne/Documents/GitHub/modules/database/Aluminum_Coating_Comparison_Data.xlsx"))
    Tab = Tab[2:,2:4].astype(np.float64)
    wavelength, reflectance = Tab[:,0], Tab[:,1]
    idx1 = np.nanargmin(np.abs(wavelength-Lambda))
    if Lambda>=wavelength[idx1]:
        idx2 = idx1+1
    else:
        idx2 = idx1-1
    d1=np.abs(wavelength[idx1]-Lambda)
    d2=np.abs(wavelength[idx2]-Lambda)
    R = reflectance[idx1] + (reflectance[idx2]-reflectance[idx1])/(d2+d1)*d1
    return(R/100)

def mirror_Al_G01(Lambda):
    """
    returns reflectance of Thorlabs G01 Al miror
    Lambda : wavelength in micrometer
    """
    Tab=np.array(pd.read_excel("/Users/tomjoly-jehenne/Documents/GitHub/modules/database/Aluminum_Coating_Comparison_Data.xlsx"))
    Tab = Tab[2:,4:6].astype(np.float64)
    wavelength, reflectance = Tab[:,0], Tab[:,1]
    idx1 = np.nanargmin(np.abs(wavelength-Lambda))
    if Lambda>=wavelength[idx1]:
        idx2 = idx1+1
    else:
        idx2 = idx1-1
    d1=np.abs(wavelength[idx1]-Lambda)
    d2=np.abs(wavelength[idx2]-Lambda)
    R = reflectance[idx1] + (reflectance[idx2]-reflectance[idx1])/(d2+d1)*d1
    return(R/100)

def mirror_Ag_P01(Lambda):
    """
    returns reflectance of Thorlabs P01 Ag miror
    Lambda : wavelength in micrometer
    """
    Tab=np.array(pd.read_excel("/Users/tomjoly-jehenne/Documents/GitHub/modules/database/Silver_Coating_Comparison_Data.xlsx"))
    Tab = Tab[2:,2:4].astype(np.float64)
    wavelength, reflectance = Tab[:,0], Tab[:,1]
    idx1 = np.nanargmin(np.abs(wavelength-Lambda))
    if Lambda>=wavelength[idx1]:
        idx2 = idx1+1
    else:
        idx2 = idx1-1
    d1=np.abs(wavelength[idx1]-Lambda)
    d2=np.abs(wavelength[idx2]-Lambda)
    R = reflectance[idx1] + (reflectance[idx2]-reflectance[idx1])/(d2+d1)*d1
    return(R/100)

def mirror_Au_M01(Lambda):
    """
    returns reflectance of Thorlabs M01 Au miror
    Lambda : wavelength in micrometer
    """
    Tab=np.array(pd.read_excel("/Users/tomjoly-jehenne/Documents/GitHub/modules/database/Gold_Coating_Comparison_Data.xlsx"))
    Tab = Tab[2:,2:4].astype(np.float64)
    wavelength, reflectance = Tab[:,0], Tab[:,1]
    idx1 = np.nanargmin(np.abs(wavelength-Lambda))
    if Lambda>=wavelength[idx1]:
        idx2 = idx1+1
    else:
        idx2 = idx1-1
    d1=np.abs(wavelength[idx1]-Lambda)
    d2=np.abs(wavelength[idx2]-Lambda)
    R = reflectance[idx1] + (reflectance[idx2]-reflectance[idx1])/(d2+d1)*d1
    return(R/100)

def lens_NBK7(Lambda):
    """
    returns transmission of Thorlabs N-BK7 lens
    Lambda : wavelength in micrometer
    """
    Lambda*=1000 #in data, wavelength in nanometer
    Tab=np.array(pd.read_excel("/Users/tomjoly-jehenne/Documents/GitHub/modules/database/Uncoated_N-BK7_Transmission.xlsx"))
    Tab = Tab[1:,2:4].astype(np.float64)
    wavelength, transmission = Tab[:,0], Tab[:,1]
    idx1 = np.nanargmin(np.abs(wavelength-Lambda))
    if Lambda>=wavelength[idx1]:
        idx2 = idx1-1
    else:
        idx2 = idx1+1
    d1=np.abs(wavelength[idx1]-Lambda)
    d2=np.abs(wavelength[idx2]-Lambda)
    T = transmission[idx1] + (transmission[idx2]-transmission[idx1])/(d2+d1)*d1
    return(T/100)
