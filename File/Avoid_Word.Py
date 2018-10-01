def avoid(word,string):
    return all(letter not in word for letter in string)



fin=open('words.txt')
string=str(input('Enter a string:'))
for line in fin:
    word=line.strip()
    if avoid(word,string):
        print(word)
