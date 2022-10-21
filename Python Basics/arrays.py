def cumsum_and_erase(A, erase=1):
    B = []
    for i in range(1,len(A)+1):
        b = sum(A[:i])
        if b != erase:
            B.append(b)
    return B