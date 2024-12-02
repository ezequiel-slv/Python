#Formato da estrutura de condicional if

#Listagem 4.2 – Condições
a = int(input("Primeiro valor: "))

b = int(input("Segundo valor: "))

if a > b:
    print('O primeiro número é o maior')
if b > a: 
    print('O segundo número é o maior')

calculo = int(input("1 x 2: "))

if calculo == 2:
    print('Correto')
else:
    print('Incorreto')
    
#Listagem 4.3 – Carro novo ou velho, dependendo da idade

idade = int(input('Digite a idade do seu carro: '))

if idade <= 3:
    print('Novo')
if idade > 3:
    print('Velho')
    
#Exercício 4.2 Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

velocidade = int(input('Digite a velocidade do carro: '))

multa = velocidade * 5 

if velocidade > 80:
    print(f'Você recebeu uma multa no valor de: {multa}R$')
if velocidade <= 80:
    print('Veiculo liberado')
    
#Exercício 4.3 Escreva um programa que leia três números e que imprima o maior e o menor.

salario = float(input('Digite o valor do seu salário: '))
base = salario
imposto = 0
if base > 3000: 
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print('Salário: R$%6.2f imposto a pagar: R$%6.2f' % (salario, imposto)) 

#Exercício 4.4 Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))

maxnum = max(num1, num2, num3)
minnum = min(num1, num2, num3)

print(f"O maior número e o menor número, respectivamente são: {maxnum} e {minnum}")

#Exercício 4.5 Execute o programa (Listagem 4.5) e experimente alguns valores. Verifique se os resultados foram os mesmos do programa anterior 

salario = int(input('Digite seu salário: '))

dezporc = salario * 1.10
quinzeporc = salario  * 1.15

if salario > 1250:
    print(dezporc)
else:
    print(quinzeporc)

#Exercício 4.6 Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

distancia = float(input('Digite a distância em km que o carro percorreu: '))

passagem = 100
cobrancaum = (0.50 * distancia) + passagem
cobrancadois = (0.45 * distancia) + passagem

if distancia <= 200:
    print(f"O valor a ser cobrado será de: {cobrancaum} Reais")
elif distancia >200:
    print(f"O valor a ser cobrado será de: {cobrancadois} Reais")