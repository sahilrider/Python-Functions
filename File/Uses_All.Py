# A program where the user inputs a string. The program will then search the file, looking at each word line by line.
# It then will determine if the user's inputted letters, are ALL contained in a word in the file.

# Note: The word or sentence, must be in quotes.
# Ex: "apple"

# Enter a string:"zylophone"
# hypnotizable
# psychoanalyze
# psychoanalyzed
# psychoanalyzes


def uses_all(word,string):
    for letter in string:
        if letter not in word:
            return False
    return True

fin=open('words.txt')
string=str(input('Enter a string:'))
for line in fin:
    word=line.strip()
    if uses_all(word,string):
        print(word)
