valor1 = int(input("Informe o primeiro numero"))
valor2 = int(input("Informe o segundo numero"))
operacao = input("Informe a operação que deseja realizar")
if operacao == "+" :
    resultado = valor1 + valor2
elif operacao == "-":
    resultado = valor1 - valor2
elif operacao == "*":
    resultado = valor1 * valor2
elif operacao == "/":
    resultado = valor1 / valor2
else:
    print("Informe uma operacao valida")
print(resultado)
