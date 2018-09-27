'''A much efficient way is written at:
   https://github.com/sahilrider/Python-Functions/tree/master/Dictionaryi
The fibonacci sequence is found throughout nature and mathematics. The patern goes:
    1,1,2,3,5,8.9
    Where the sum of the current(n) and the previous(n-1) are added to produce the next 
    value in the sequence(n+1)
'''

def fibonacci(n):
    a=0
    b=1
    print(a)
    while b<n :
        print(b)
        temp=b
        b=b+a
        a=temp
        

fibonacci(100)
