'''A much efficient way is written at:
   https://github.com/sahilrider/Python-Functions/tree/master/Dictionary'''

def fibonacci(n):
    a=0
    b=1
    print(a)
    while b<n :
        temp=b
        b=b+a
        a=temp
        print(b)
        

fibonacci(int(input("enter number_:")))
