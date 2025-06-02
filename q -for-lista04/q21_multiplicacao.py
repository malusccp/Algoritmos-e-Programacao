# 21. Leia 2 números inteiros e escreva a multiplicação dos mesmos, sem que o operador de multiplicação (*)
# seja utilizado.
import utils

def main():
    num1 = utils.get_integer_number_min('Número 1: ', 0)
    num2 = utils.get_integer_number_min('Número 2: ', 0)

    resultado = 0
    if num1 < num2:
        for i in range(1, num1+1, 1):
            resultado += num2
    else:
        for i in range(1, num2+1, 1):
            resultado += num1

    print(f'A multiplicação de {num1} x {num2} é igual a -> {resultado} ')



main()