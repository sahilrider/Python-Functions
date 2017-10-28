def factorial(n):
	fact = 1
	if(n==0):
		print( 1)
	elif(n<0):
	  print("Please enter positive integers")
	else:
		for counter in range (n,0,-1):
			fact = fact * counter
			if(counter == 1):
				print(counter,end = '')
				break
			print(counter, " * ",end = '')
			
		print(" = ",fact)
		

factorial(-1)