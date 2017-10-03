# A program where the user inputs a string. The program will then search the file, looking at each word line by line.
# It then will determine if ANY of the letters in the users inputted string, is in the word. If it is, it won't be printed out.

# Note: The word or sentence, must be in quotes.
# Ex: "apple"

def avoid(word,string):
    for i in string:
        if i in word:
            return False
    return True

fin=open('words.txt')
string=str(input('Enter a string:'))
for line in fin:
    word=line.strip()
    if avoid(word,string):
        print(word)
