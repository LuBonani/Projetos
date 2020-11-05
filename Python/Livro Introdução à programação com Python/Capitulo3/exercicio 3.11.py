mercadoria = int(input("preço mercadoria:"))
percentual = int(input("Percentual de desconto:"))
desconto = mercadoria*percentual/100
novo_preco = mercadoria - desconto
print("o valor do desconto é %d e o preço a pagar é R$ %d" % (desconto, novo_preco))
