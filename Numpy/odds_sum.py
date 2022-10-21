import numpy as np #не стирать!        

def diag_2k(a):
    diag = np.diagonal(a)    
    i = 0
    result = diag[diag % 2 == 0].sum()    
    return result