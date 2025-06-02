# Leia 2 números inteiros e escreva o quociente e o resto da divisão dos mesmos, sem que os operadores
# de divisão (/ e %) sejam utilizados.
import utils

def main():
    num1 = utils.get_integer_number_min('Número 1: ', 0)
    num2 = utils.get_integer_number_min('Número 2: ', 0)


    if num2 == 0:
        print('Erro. Divisão por 0 não é permitida')
    else:
        quociente = 0
        resto = num1

        for _ in range(num1):
            if resto >= num2:
                resto -= num2
                quociente += 1
            else: 
                break
        
        print(f'O quociente e o resto da divisão entre os números {num1} e {num2} é igual a:\nQuociente: {quociente}\nResto: {resto} ')

main()