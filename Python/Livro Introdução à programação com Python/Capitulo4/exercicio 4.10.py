quantidade = int(input("Informe a quantidade kWh consumida"))
instalacao = input("Informe o tipo de instação: (R para residências, I para indústrias e C para comércios)")
if instalacao == "R":
    if quantidade <= 500:
        preco = quantidade * 0.4
    else:
        preco = quantidade * 0.65
elif instalacao == "C":
    if quantidade <= 1000:
        preco = quantidade * 0.55
    else:
        preco = quantidade * 0.6
elif instalacao == "I":
    if quantidade <= 5000:
        preco = quantidade * 0.55
    else:
        preco = quantidade * 0.6
else:
    print("Insira um tipo de instalação válido!")
print("O preço a pagar pelo fornecimento de energia é R$%6.2f" % preco)
