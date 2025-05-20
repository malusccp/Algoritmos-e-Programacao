# Leia dois números X e N. A seguir, escreva o resultado das divisões de X por N onde, após cada
# divisão, X passa a ter como conteúdo o resultado da divisão anterior e N é decrementado de 1 em 1, até
# chegar a 2.

import utils

def main():
    num_x = utils.get_integer_number_min('Número X: ', 0)
    num_n = utils.get_integer_number_min('Número N: ', 0)

    while num_n > 2:
        resultado = num_x//num_n
        print(resultado)
        num_x = resultado
        num_n -= 1

main()
        