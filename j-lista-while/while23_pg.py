# 23. Escreva um algoritmo que leia a razão de uma PG (Progressão Geométrica) e o seu primeiro termo e
# escreva os N termos da PG. Ler o valor de N.
import utils
def main():
    razao = utils.get_integer_number('Razão: ')
    primeiro_termo = utils.get_integer_number('Primeiro termo: ')
    N = utils.get_decimal_number_min('Termos: ', 0)

    contador = 0
    while contador < N:
        termo_pg = primeiro_termo * razao**(contador)
        print(termo_pg)
        contador += 1


main()