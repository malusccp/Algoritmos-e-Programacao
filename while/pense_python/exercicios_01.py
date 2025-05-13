from uteis import obter_numero_inteiro
import math
def main():
 raiz = obter_numero_inteiro("Escreva um número para calcular a raiz: ")
 estimativa = obter_numero_inteiro("Escreva uma estimativa: ")
 mysqrt(raiz, estimativa)
 test_square_root(raiz, estimativa)


def mysqrt(raiz, estimativa):
 while True:
    print(raiz)
    y = (estimativa + raiz/estimativa)/ 2
    if y == estimativa:
      break
    estimativa = y


def test_square_root(raiz, estimativa):
    print(f'{raiz} {mysqrt(raiz, estimativa)}  {math.sqrt(raiz)} {mysqrt(raiz, estimativa) - math.sqrt(raiz)} )')
    print(f'----    ------------    ---------------- -----------')


main()