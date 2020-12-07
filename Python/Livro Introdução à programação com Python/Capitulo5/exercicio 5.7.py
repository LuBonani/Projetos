n = int(input("Tabuada de:"))
x = int(input("Digite o numero de inicio"))
fim = int(input("Digite o numero de fim"))
while x <= fim:
    print("%i x %i = %i" % (n, x, n*x))
    x = x + 1
    
