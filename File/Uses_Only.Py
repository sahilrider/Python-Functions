# A program where the user inputs a string. The program will then search the file, looking at each word line by line.
# It then will determine if the word contains ONLY the user's inputted letters. (Doesn't have to be all the letters in a user's inputted string.)

# Note: The word or sentence, must be in quotes.
# Ex: "apple"

# Ex: Enter a string: "Neck"
# cee
# eke
# keck
# keek

def uses_only(word,string):
    for letter in word:
        if letter not in string:
            return False
    return True

fin=open('words.txt')
string=str(input('Enter a string:'))
for line in fin:
    word=line.strip()
    if uses_only(word,string):
        print(word)
