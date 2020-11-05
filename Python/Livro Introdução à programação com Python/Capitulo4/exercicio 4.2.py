velocidade = int(input("Qual a velocidade do seu carro no momento?"))
if velocidade <= 80 :
    print("O carro esta dentro dos limites de velocidade!")
if velocidade > 80 :
    multa = (velocidade - 80) * 5
    print("Voce foi multado em: R$%5.2f" % multa)
