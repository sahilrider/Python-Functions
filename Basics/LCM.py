def gcd(a,b): 
      
    # Everything divides 0  
    if (a == 0): 
        return b 
    if (b == 0): 
        return a 
  
    # base case 
    if (a == b): 
        return a 
  
    # a is greater 
    if (a > b): 
        return gcd(a-b, b) 
    return gcd(a, b-a)
a,b=map(int,input().split())
gcd=gcd(a,b)
lcm=(a*b)/gcd