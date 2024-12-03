#Vejamos o exemplo de calcular a conta de um telefone celular da empresa Tchau. Os  planos  da  empresa Tchau  são  bem  interessantes  e  oferecem  preços  diferenciados de acordo com a quantidade de minutos usados por mês. Abaixo de 200 minutos, a empresa cobra R$ 0,20 por minuto. Entre 200 e 400 minutos, o preço é de R$ 0,18. Acima de 400 minutos, o preço por minuto é de R$ 0,15.

planotelefonico = int(input("Digite a quantidade de minutos usados na telefonia: "))



if planotelefonico < 200:
    preco = 0.20
elif planotelefonico < 400:
    preco = 0.18
else:
    preco = 0.15

print(" Vocẽ vai pagar este mẽs: R$%6.2f" % (planotelefonico * preco))