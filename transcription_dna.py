#Transcricao do DNA
#Alunos- Luis Carlos e Rodolfo

input = "GCC.GCC.GGT.TAA.TGC.CGA.TAA.TGC.ATG"

output = ""
for m in input:
    if m == 'G':
        output += "C"
    elif m == 'C':
        output += "G"
    elif m == 'T':
        output += "A"
    elif m == 'A':
        output += "U"
    elif m == '.':
        output += "."

print("DNA - ", input)
print("RNAm - ", output)
