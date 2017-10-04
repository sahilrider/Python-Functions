'''
A Counter is subclass of dictionary in Python.It is an unordered collection where elements and their respective count are stored as dictionary.This is equivalent to multiset of other languages.
 '''
from collections import Counter

c=Counter()   #initializing a empty counter
#update for providing data , Use any of the following methods
#c.update(['a','b','c','a','d'])  #by list 
#c.update({'A':3,'B':2,'C':2})    #by dictionary
#c.update(a=3,b=2,c=1)      #with keyword arguments

#To count number of occurences of each letter in a word


a=input('Enter String --> ')
a=list(a)  #typecasting as counter take list as data input
c.update(a)
d=Counter([' ']) # creating this counter so as to exclude spaces from counter c 
c.subtract(d)    #elements from d are subtracted from c

'''
The elements() method returns an iterator that produces all of the items known to the counter.Here I have used set over it as it produces each element the number of times its value.
'''
for i in set(c.elements()): 
  print(i ,c[i])
