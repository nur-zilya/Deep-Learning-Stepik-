import numpy as np

def no_numpy_scalar(v1, v2):
    result = 0
    for x, y in zip(v1, v2):
        result += x * y
    return result

def numpy_scalar (v1, v2):
    result = np.dot(v1, v2)
    return result