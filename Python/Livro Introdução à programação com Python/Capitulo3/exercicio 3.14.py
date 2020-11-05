km = float(input("qual a quantidade de km percorridos:"))
dias = int(input("quantidade de dias do aluguel do carro"))
total = (dias * 60) + (km * 0.15)
print("o total a pagar será R$ %5.2f" % total)
