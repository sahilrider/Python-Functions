def fibo(n):
    a,b=0,1
    print (a)
    print (b)
    n=n-2
    while n>0:
     c=a+b
     a=b
     b=c
     n=n-1
     print (c)
num=int(input("enter the limit"))
fibo(num)
