
# Leia um número e divida-o por dois (sucessivamente) até que o resultado seja menor que 1. Escreva o
# resultado da última divisão efetuada.


def main():
    num = int(input('Número: '))

    for i in range(num):
       divisao = 2 / num
       if divisao < 1: break

    print(f'{divisao:.2f}')

main()