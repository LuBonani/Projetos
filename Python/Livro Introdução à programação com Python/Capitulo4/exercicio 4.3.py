a = int(input("Entre com o 1 numero: "))
b = int(input("Entre com o 2 numero: "))
c = int(input("Entre com o 3 numero: "))
if a > b :
    if a > c:
        maior = a
    if b > c:
        menor = c
    if c > b:
        menor = b
if b > a :
    if b > c:
        maior = b
    if a > c:
        menor = c
    if c > a:
        menor = a
if c > a:
    if c > b:
        maior = c
    if a > b:
        menor = b
    if b > a:
        menor = a
print("O maior numero é %d e o menor numero é %d" % (maior, menor))
        
