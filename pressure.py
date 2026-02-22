#pressure
#imports
import numpy as np

alpha = 0.0873
Mach = 2.6

#Cp = (2)/np.sqrt(Mach**2 - 1)

#print(Cp)

def p_above(M,a):

    Cp = -(2)/np.sqrt(M**2 - 1)
    frac = (1.4 * (M**2) * Cp)/2
    p = frac*a + 1


    return p

print(p_above(Mach,alpha))

def p_below(M,a):

    Cp = (2)/np.sqrt(M**2 - 1)
    frac = (1.4 * (M**2) * Cp)/2
    p = frac*a + 1


    return p

print(p_below(Mach,alpha))