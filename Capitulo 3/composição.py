print("Composição com marcadores")

#%d: números inteiros
#s: String
#f: números decimais

#Listagem 3.10 – Exemplo de composição com marcadores

idade = 5

print("[%d]" % idade) #apresentará o número 5 

print("[%05d]" % idade) #apresentará o número 5 na posição 5, após 4 zeros

print("[%3d]"% idade) #apresentará o número 5 na posição 3, sem nenhum valor armazenado nas duas primeiras posições

print("[%-3d]" % idade) ##apresentará o número 5 na posição oposta do "[%3d]"


