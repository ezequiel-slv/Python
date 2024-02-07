#Exercício 3.1

#tipo de valor da variável
num1 = -2
print(type(num1)) 

num2 = 4.3
print(type(num2))

#teste
teste = (3*0.1)
print(teste)

#bool
a = 1
b = 5
c = 2
d = 1

print(a > b) #maior que
print(c < b) #menor que
print(a == d) # igual
print(c >= d) # maior que ou igual
print(b <= c) # menor que ou igual
print(a != d) # diferente 

# Operadores relacionais com variáveis do tipo lógico
nota = 8
media = 7
aprovado = nota > media

print(aprovado)

#Operador not
operador_not = "Operador not"
print(operador_not)

opnot = not True
print(opnot)

opnot2 = not False
print(opnot2)

#Operador and
operador_and = "Operador and"
print(operador_and)

opand = True and True
print(opand)

opand2 = True and False
print(opand2)

opand3 = False and True
print(opand3)

opand4 = False and False
print(opand4)

#Operador or
operador_or = "Operador or"
print(operador_or)

opor = True or True
print(opor)

opor2 = True or False
print(opor2)

opor3 = False or True
print(opor3)

opor4 = False or False
print(opor4)

print("exercicio")
#Exercício 3.3 Complete a tabela a seguir utilizando a = True, b = False e c = True.

a = True
b = False
c = True

print(a and a)
print(b and b)
print (not c)
print(not b)
print(not a)
print(a and b)
print(b and c)
print(a or c)
print(b or c)
print(c or a)
print(c or b)
print(c or c)
print(b or b)

print("Exercício 3.4")
#Exercício 3.4 Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00.

salario = float(input("Digite o valor do seu salário: "))

if salario > 1200:
    print("Deve pagar o imposto")   
else:
   print("Está isento do imposto")

#Exercício 3.6 Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.
materia1 = float(input("Digite a nota da materia 1: "))
materia2 = float(input("Digite a nota da materia 2: "))
materia3 = float(input("Digite a nota da materia 3: "))

resultado = ( materia1 + materia2 + materia3)/3

if resultado > 7:
    print("Aprovado")
else:
   print("Reprovado")

# função len
print(len("quantidade de letras")) #mostra quantas letras tem uma string

 #indice de uma string (mostra o indice da palavra)
indice = ("quantidade") 
#          0123456789
print(indice[5])

#concatenação (juntar duas ou mais strings em uma nova string)
s = ("ABC")
print(s + "D")

print(s + "C" * 4)

print(s + "x4 = " +s*4)

print("marrcadores")

#%d: números inteiros
#s: String
#f: números decimais