minutos = int(input("Quantos minutos você utilizou esse mês:"))
if minutos < 200:
    preco = 0.2
else:
    if minutos < 400:
        preco = 0.18
    else:
        preco = 0.15
print("Você vai pagar este mês: R$%6.2f" % (minutos * preco))
