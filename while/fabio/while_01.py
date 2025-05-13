import uteis

def main():
    numero = uteis.get_integer_number_min('Escreva um número inteiro "N": ', 1)
    print(f"A contagem de 1 até {numero} é: ")
    uteis.linhas()
    numero_de_1_a_N(numero)
    uteis.linhas()


def numero_de_1_a_N(numero: int):
    contador = 1
    while numero >= contador:
        print(f'{contador}')
        contador += 1


main()