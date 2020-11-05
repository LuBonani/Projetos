salario = int(input("salario:"))
porcentagem = int(input("porcentagem do aumento do salario:"))
novo = salario + (salario * porcentagem/100)
print("O novo salario é %d e a porcentagem é %d " % (novo, porcentagem))
