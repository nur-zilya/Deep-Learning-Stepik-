import numpy as np

def transform(X, a=1):
    b = X.copy()
    b[:,1::2]=a
    b[:,0::2]= b[:,0::2]**3
    b = b[:,::-1]
    return (np.concatenate((X,b), axis=1)) 