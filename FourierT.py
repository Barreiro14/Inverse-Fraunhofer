import numpy as np
from scipy.fft import fft2, ifft2

def Ftransform(arr):
    return fft2(arr)

def IFtransform(arr):
    return ifft2(arr)