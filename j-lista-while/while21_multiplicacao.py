# 21. Leia 2 números inteiros e escreva a multiplicação dos mesmos, sem que o operador de multiplicação (*)
# seja utilizado.
import utils

def main():
    num1 = utils.get_integer_number_min('Número 1: ', 0)
    num2 = utils.get_integer_number_min('Número 2: ', 0)

    contador = num1
    while contador != num2:
        num1 += num2
        contador += 1

    print(f'A multiplicação {num1} x {num2} é igual a -> {num1} ')


main()