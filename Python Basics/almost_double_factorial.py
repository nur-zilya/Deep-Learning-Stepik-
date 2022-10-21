def almost_double_factorial(n):
    count = 1
    for i in range(n+1):
        if i == 0:
            count *= 1
        if i % 2 != 0:
            count *= i            
    return count