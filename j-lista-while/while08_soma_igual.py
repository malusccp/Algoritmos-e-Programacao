# Leia um numero X e, a seguir, leia e escreva uma lista de números com o término da lista ocorrendo
# quando a soma de dois números consecutivos da lista for igual a X.

import utils

def main():
    num_1 = utils.get_integer_number_min('Número Candidato: ', 0)

    while True:
        num_2 = utils.get_integer_number_min('Número Soma 1: ', 0)
        num_3 = utils.get_integer_number_min('Número Soma 2: ', 0)
        if (num_2 + num_3) == num_1:
            break
        else:
            continue

main()