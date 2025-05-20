# Escreva um algoritmo para determinar o número de dígitos de um número informado.

import utils

def main():
    num = utils.get_integer_number_min('Número: ', 0)
    contador = 0
    while num > 1:
        num /= 10
        contador += 1

    print(f'O número tem {contador} dígitos')

main()