print("Revisão")
exer1 = (35+35)
print(f"35+35 = {exer1}")
exer2 = (30-20)
print(f"30-20 = {exer2}")
exer3 = (10*5)
print(f"10*5 = {exer3}")
exer4 = (44/2)
print(f"44/2 = {int(exer4)}")
exer5 = (5**2)
print(f"5**2 = {exer5}")

print("expressões")
expressao1 = ((22*3 - 6)**2)
print(expressao1)
expressao2 = (4**2 / 2)
print(expressao2)

print("prioridade de operações")
print("exercício 1. faça o calculo baseado na prioridade dessa expressão: (10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2)")

prio1 = (10 % 3)
print(f"10 % 3 = {prio1}")
prio2 = (10 ** 2)
print(f"10 ** 2 = {prio2}")
prio3 = (4 / 2)
print(f"4 / 2 = {prio3}")
prio4 = ((prio1)*(prio2))
print(f"10 % 3 * 10 ** 2 = {prio4}")
prio5 = ((prio3)*10)
print(f"4/2 * 10 = {prio5}")
prio6 = ((prio4)+1)
print(f"10 % 3 * 10 ** 2 + 1 = {prio6}")
prio7 = ((prio6)-(prio5))
print(f"(10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2) = {prio7}")

print("gabarito")
resultado = (10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2)
print(resultado)

if prio7 == resultado:
    print("correto")
    
#Exercício 2.2 Digite a seguinte expressão e observe como a prioridade das operações é importante.
print("Exercício aumento de salário")

salario = 1400
aumento = 10

print(1400 + (salario * aumento/100))