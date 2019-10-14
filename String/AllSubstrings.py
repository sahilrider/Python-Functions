from itertools import combinations 

test_str = input("Enter string")

print("The original string is : " + str(test_str)) 
  
# Get all substrings of string 
res = [test_str[x:y] for x, y in combinations( 
            range(len(test_str) + 1), r = 2)] 
  
# printing result  
print("All substrings of string are : " + str(res)) 
