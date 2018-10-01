def is_abecedarian(word):
    return all(nxt <= prev for nxt, prev in zip(word[:-1], word[1:]))

fin=open('words.txt')
for line in fin:
    word=line.strip()
    if is_abecedarian(word):
        print(word)
