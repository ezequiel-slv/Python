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