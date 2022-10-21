import numpy as np

def no_numpy_mult(first, second):
    length = len(first) 
    result_matrix = [[0 for i in range(length)] for i in range(length)]
    for i in range(length):
         for j in range(length):
            for k in range(length):
                   result_matrix[i][j] += first[i][k] * second[k][j]

    result = result_matrix
    return result

def numpy_mult(first, second):
    res = first.dot(second)
    
    result = res
    return result