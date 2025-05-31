# 24. Escreva um algoritmo que leia a razão de uma PA (Progressão Aritmética) e o seu primeiro termo e
# escreva os N termos da PA. Ler o valor de N.
import utils
def main():
    razao = utils.get_integer_number('Razão: ')
    primeiro_termo = utils.get_integer_number('Primeiro termo: ')
    N = utils.get_decimal_number_min('Termos: ', 0)

    contador = 0
    while contador < N:
        termo_pa = primeiro_termo + (contador * razao)
        print(termo_pa)
        contador += 1


main()