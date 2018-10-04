def fibonacci(n):                #prints n'th term of the Fibonacci sequence
    if(n==1 or n==2):
        return 1
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

a=fibonacci(10)
print a
