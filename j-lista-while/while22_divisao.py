# Leia 2 números inteiros e escreva o quociente e o resto da divisão dos mesmos, sem que os operadores
# de divisão (/ e %) sejam utilizados.
import utils

def main():
    num1 = utils.get_integer_number_min('Número 1: ', 0)
    num2 = utils.get_integer_number_min('Número 2: ', 0)

    quociente = 0
    resto = 0
    while num1 > resto:
        quociente += 1
        resto = num1 - num2
    
    print(f'O quociente e o resto da divisão entre os números {num1} e {num2} é igual a:\nQuociente: {quociente}\nResto: {resto} ')

main()