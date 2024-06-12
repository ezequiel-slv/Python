#Formato da estrutura de condicional if
'''
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

idade = int(input('Digite a idade do seu carro: '))

if idade <= 3:
    print('Novo')
if idade > 3:
    print('Velho')

velocidade = int(input('Digite a velocidade do carro: '))

multa = velocidade * 5 

if velocidade > 80:
    print(f'Você recebeu uma multa no valor de: {multa}R$')
if velocidade <= 80:
    print('Veiculo liberado')
'''
salario = float(input('Digite o valor do seu salário: '))
base = salario
imposto = 0
if base > 3000: 
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print('Salário: R$%6.2f imposto a pagar: R$%6.2f' % (salario, imposto)) 