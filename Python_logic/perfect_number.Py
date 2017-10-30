def perfect(n):
    ctr=False
    p=[2,3,5,7,13,17,19,31,61,89,107,127]
    for i in p:
        per=(2**(i-1))*(2**i-1)
        if per==n:
            ctr=True
            break
    return ctr

print(perfect(8589869058))

