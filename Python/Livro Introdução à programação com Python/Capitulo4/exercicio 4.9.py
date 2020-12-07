casa = float(input("Informe o valor da casa a comprar:"))
salario = float(input("Informe seu salario:"))
anos = int(input("Informe a quantidade de anos a pagar:"))

prestacao = casa/(anos * 12)

if prestacao > (salario * 0.3) :
    print("empréstimo recusado")
else:
    print("empréstimo aprovado")
