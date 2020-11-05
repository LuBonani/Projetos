def imprimir_iniciais(palavras):
    for p in palavras:
        primeira_letra=p[0]
        if primeira_letra.isupper():
            print(primeira_letra)


def soma(a, b, *numeros):
    return a + b + sum(numeros, start=0)


if __name__ == '__main__':
    imprimir_iniciais("Luciana Bonani Domiciano".split())
    imprimir_iniciais("Renzo dos Santos".split())
    print(soma(1, 2))
    print(soma(2, 3))
    print(soma(2, 3, 4))
    print(soma(2, 3, 4, 5))

