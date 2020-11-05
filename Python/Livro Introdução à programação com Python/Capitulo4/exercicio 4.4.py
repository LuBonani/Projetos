salario = float(input("Entre com o salário do funcionário"))
if salario <= 1250:
    aumento = salario * 0.15
if salario > 1250:
    aumento = salario * 0.1

print("O aumento é de %6.2f" % aumento)
