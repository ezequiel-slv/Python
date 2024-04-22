#fatiamento

s = "ABCDEFGHI"

print(s[0:2]) #0 = inicio do fatiamento, 2 = até onde será pego pelo fatiamento
 
print(s[1:3])

print(s[0:4])

print(s[1:8])

print("omitir caractere")

print(s[:2]) #indica do início até o segundo caractere (sem incluí-lo)

print(s[:8])

print(s[3:]) #indica do caractere de posição 1 até o final da string.

print("fatiamento com omissão de valores e com índices negativos")

#ABCDEFGHI

print(s[:2]) #AB

print(s[1:]) #BCDEFGHI

print(s[0:-2]) #ABCDEFG

print(s[:]) #ABCDEFGHI

print(s[-1:]) #I

print(s[-5:7]) #EFG

print(s[s[-2:1]])