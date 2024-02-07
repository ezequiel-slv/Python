print("Exercício 3.1")

#tipo de valor da variável
num1 = -2
print(type(num1)) 

num2 = 4.3
print(type(num2))

#teste
teste = (3*0.1)
print(teste)

print("Exercício 3.4")
#Exercício 3.4 Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00.

salario = float(input("Digite o valor do seu salário: "))

if salario > 1200:
    print("Deve pagar o imposto")   
else:
   print("Está isento do imposto")

print("Exercício 3.6 ")
#Exercício 3.6 Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.
materia1 = float(input("Digite a nota da materia 1: "))
materia2 = float(input("Digite a nota da materia 2: "))
materia3 = float(input("Digite a nota da materia 3: "))

resultado = ( materia1 + materia2 + materia3)/3

if resultado > 7:
    print("Aprovado")
else:
   print("Reprovado")