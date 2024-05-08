#entrada de dados

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

#Exercício 3.11 Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

preco_merc = float(input("Digite o preço da mercadoria: "))

perc_desconto = float(input("Digite o percentual de desconto: "))

val_desc = (perc_desconto/100 * preco_merc)

val_pag = preco_merc - (perc_desconto/100 * preco_merc)

print(f"O valor do desconto e de: {val_desc:.1f}")

print(f"O valor a ser pago é de: {val_pag:.1f}")

#Exercício 3.12 Escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.


distancia = int(input("Informe a distância a percorrer da viagem em km: "))

velocidade = int(input("Informe a velocidade do veiculo em km/h: "))

tempo_viagem = distancia / velocidade

print(f"O tempo da viagem em horas é de: {tempo_viagem}")

#Exercício 3.13 Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa conversão é:

celsius = float(input("Digite a temperatura em Celsius: "))

celsius_fahrenheit = ((9 * celsius)/5 + 32)

print(f"O valor de {celsius} em Fahrenhheit é: {celsius_fahrenheit}")


#Exercício 3.14 Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

km = int(input("Digite a quantidade de km percorridos pelo carro: "))

reais_km = 0.15 * km

dias = int(input("Digite a quantidade de dias utilizando o carro: "))

reais_dias = 60 * dias

reais_total = (60 * dias) + (0.15 * km)

print(f"O valor total a se pagar pelo aluguel do carro é de: {reais_total} reais")


#Exercício 3.15 Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

qt_cigarros = int(input("Digite a quantidade de cigarros fumados pelo usuário: "))


anos_usados = int(input("Digite o tempo em anos em que o usuário fumou: "))



