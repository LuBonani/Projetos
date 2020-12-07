distancia = int(input("Digite a distancia que pretende percorrer em metros: "))

if distancia <= 200:
    valor = distancia * 0.5
    print("O valor a ser pago é: R$%6.2f " % valor)
else:
    valor = distancia * 0.45
    print("O valor a ser pago é: R$%6.2f " % valor)
