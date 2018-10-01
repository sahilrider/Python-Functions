def uses_only(word,string):
    return all(letter not in string for letter in word)


fin=open('words.txt')
string=str(input('Enter a string:'))
for line in fin:
    word=line.strip()
    if uses_only(word,string):
        print(word)
