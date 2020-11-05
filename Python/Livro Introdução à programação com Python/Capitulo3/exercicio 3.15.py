cigarros = int(input("qual a quantidade de cigarros fumados por dia:"))
anos = int(input("por quantos anos você fuma"))
total = (cigarros*anos*0.00694444*365)
print("Voce já perdeu %d dias de vida por fumar" % total)
