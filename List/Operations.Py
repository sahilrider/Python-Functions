'''To find sum of all nested lists'''

def nested_sum(t):
    s=0
    for i in range(len(t)):
        s+=sum(t[i])
    return s

t=[[1,2],[3],[4,5,6]]
print(nested_sum(t))

'''To find sum till prev no.'''

def cumsum(li):
    li2=[]
    for i in li:
        li2.append(sum(li[:i]))
    return li2

t=[1,2,3,4,5,6]
print(cumsum(t))

    return li2

t=[1,2,3,4,5,6]
print(cumsum(t))

'''To return a list without first and last element'''

def middle(t):
    return t[1:-1]

t=[1,2,3,4,5]
print(middle(t))


'''To chop head and tail of list'''

def chop(t):
    del t[0]
    del t[-1]

t=[1,2,3,4]
chop(t)
print(t)
