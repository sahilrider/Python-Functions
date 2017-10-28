# to check string is a palindrome ro not
#for easy understanding for the logic of palindrome

def palindrome(word):
	#reverse of the string
	reverse = rev_string(word)
	if (word == reverse):
		print('Palindrome')
	else:
		print('Not a palindrome')

		
def rev_string(word):
	new_word = ''
	for index in range(len(word),0,-1):
		new_word += word[index-1]
	return new_word
		
palindrome('madam')