'''Question1
   Define a Python function "descending(l)" that returns True
   if each element in its input list is at most as big as the one before it'''

def descending(li):
    l=len(li)
    if l==0 or l==1 or len(li)==0:
        return True
    else:
        for i in range(1,l):
            if li[i]==li[i+1]:
                return True
            else:   
               return False
'''Question 2
   Define a Python function "alternating(l)" that returns True
   if
   the values in the input list alternately go up and down (in a strict manner)'''
def alternating(li):
    l=len(li)
    if l==0 or l==1:
        return True
    if li[0]==li[1]:
        return False
    elif li[0]>li[1]:         #start-down-up...
        for i in range(2,l):
            if i%2==0:
                if li[i]<=li[i-1]:
                    return False
            else:
                if li[i]>=li[i-1]:
                    return False
        return True
    elif li[0]<li[1]:         #start-up-down...
        for i in range(2,l):
            if i%2==0:
                if li[i]>=li[i-1]:
                    return False
            else:
                if li[i]<=li[i-1]:
                    return False
        return True

'''Question 3
Write a Python function "matmult(m1,m2)" that takes as input two matrices
using this row-wise representation and returns the matrix product m1*m2 '''

def matmult(li1,li2):
    r1=len(li1)
    c1=len(li1[0])
    r2=len(li2)
    c2=len(li2[0])
    li3=[]
    for i in range(r1):
        li3.append([])
    for i in range(r1):
        for j in range(c2):
            sum=0
            for k in range(r2):
                sum+=li1[i][k]*li2[k][j]
            li3[i].append(sum)
    return li3

'''Example:

>>> descending([])
True

>>> descending([4,4,3])
True

>>> descending([19,17,18,7])
False

>>> alternating([])
True

>>> alternating([1,3,2,3,1,5])
True

>>> alternating([3,2,3,1,5])
True

>>> alternating([3,2,2,1,5])
False

>>> alternating([3,2,1,3,5])
False

>>> matmult([[1,2],[3,4]],[[1,0],[0,1]])
[[1,2],[3,4]]

>>> matmult([[1,2,3],[4,5,6]],[[1,4],[2,5],[3,6]])
[[14, 32], [32, 77]]
'''
