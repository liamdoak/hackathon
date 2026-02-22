#pressure
#imports
import numpy as np

alpha = 0.0873
Mach = 2.6

def p_above(M,a):

    Cp = -(2)/np.sqrt(M**2 - 1)
    frac = (1.4 * (M**2) * Cp)/2
    p = frac*a + 1


    return p

def p_below(M,a):

    Cp = (2)/np.sqrt(M**2 - 1)
    frac = (1.4 * (M**2) * Cp)/2
    p = frac*a + 1


    return p
