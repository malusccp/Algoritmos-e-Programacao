import uteis

def main():
    limite_inferior = uteis.get_integer_number("Escreva o limite inferior: ")
    limite_superior = uteis.get_integer_number_min("Escreva o limite superior: ", limite_inferior+1)
    uteis.linhas()
    print(f"Os algarismos ímpares dentro do intervalo de ({limite_inferior} - {limite_superior}) são iguais a: ")
    impares_entre_limites(limite_inferior, limite_superior)
    uteis.linhas()


def impares_entre_limites(limite_inferior:int, limite_superior:int):
    numero = limite_inferior
    while numero <= limite_superior:
        if not numero % 2 == 0:
            print(numero)
        numero += 1


main()