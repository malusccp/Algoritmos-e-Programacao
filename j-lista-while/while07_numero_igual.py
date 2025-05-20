# Leia um número e, a seguir, leia uma lista de números até achar um igual ao primeiro número lido.

import utils

def main():
    num = utils.get_integer_number_min('Número Candidato: ', 0)
    while True:
        lista_num = utils.get_integer_number_min('Lista de números: ', 0)
        if lista_num == num:
            break
        else:
            continue


main()