#entrada de dados
'''
print("Entrada de dados")
x = float(input("Digite um valor: "))

print(x)

nome = input("Digite seu nome: ")

print("Vocẽ digita %s" % nome)

print("Olá, %s!" % nome)

#Conversão de valores
print('conversão de entrada de dados')

anos = int(input("Anos de serviço: "))

valor_por_ano = float(input("Valor por ano: "))

bonus = anos * valor_por_ano

print("Bônus de %5.2f" % bonus)

print("Exercício 3.7")

#Exercício 3.7 Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela.

num1 = int(input("Digite o primeiro número: "))

num2 = int(input("Digite o segundo número: "))

print(num1 + num2)

print("Exercício 3.8")

#Exercício 3.8 Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

metros = float(input("Digite em metros: "))

metros_centimetros = (metros * 100)

print(f"{metros} metros em centimetros é: {int(metros_centimetros)}cm")

print("Exercício 3.9")

#Exercício 3.9 Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dia = int(input("Digite o dia: "))
hora = int(input("Digite a hora: "))
minuto = int(input("Digite o minuto: "))
segundos = int(input("Digite o segundo: "))

total_segundos = ((dia * 24 * 60 * 60) + (hora * 60 * 60) + (minuto * 60) + segundos)

print(total_segundos)

#Exercício 3.10 Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Digite o valor d salário: "))

aumento = float(input("Digite a porcetagem de aumento: "))

aumento_salario = salario + ((aumento/100)*salario)

acrescimo = (aumento/100 * salario)

print(f"O valor do salário com aumento é de: {aumento_salario}")

print(f"O acrescimo em cima do salário é de: {acrescimo}")
'''
#Exercício 3.11 Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

preco_merc = float(input())