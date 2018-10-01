def uses_all(word,string):
    return all(letter in word for letter in string)

fin=open('words.txt')
string=str(input('Enter a string:'))
for line in fin:
    word=line.strip()
    if uses_all(word,string):
        print(word)