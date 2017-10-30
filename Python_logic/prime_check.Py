def prime(n):
    for i in range(2,n):
        if n%i==0:
            print(i)
            print("Not a Prime No.")
            return 0
    print("Prime No.")
    return 1

prime(2)
