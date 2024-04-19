#tipo de daddos 
print("tipo de dados")
num1 = 4 
print(type(num1))
num2 = 5.2
print(type(num2))

#bool
print("Bool")
a = 3
b = 2
c = 9
d = 1

print(a < b) #false
print(c > a) #true
print(d <= c) #true
print(d != a) #true

var1 = 5
var2 = 7

print(var1 > var2) #false

a2 = True
b2 = False
c2 = True

print("Exercício 3.4")
#Exercício 3.4 Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00.

salario = float(input("Digite o valor do salário: "))

if salario > 1200:
    print("Você deverá pagar imposto")
else:
    print("Você não deverá pagar imposto")

print("Exercício 3.6")
#Exercício 3.6 Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.

materia1 = float(input("Digite a nota da materia 1: "))
materia2 = float(input("Digite a nota da materia 2: "))
materia3 = float(input("Digite a nota da materia 3: "))

media = ((materia1 + materia2 + materia3)/3)

if media > 7:
    print("Aprovado")
else:
    print("Reprovado")

#função len
print("função len")
    
print("Exercício: Calcular e imprimir o comprimento de uma string.")

print(len("Testando"))

#função indice
print("função indice")

print("Exercício: Imprimir o caractere no índice 5 da string.")

indice = ('caractere')

print(indice[5])

#concatenação
print("concatenação")

print("Exercício")
#Exercício: Concatenar uma letra "D" à string "ABC" e imprimir o resultado.
l = ("ABC")
print(l + "D")



