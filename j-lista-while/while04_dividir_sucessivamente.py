# Leia um número e divida-o por dois (sucessivamente) até que o resultado seja menor que 1. Escreva o
# resultado da última divisão efetuada.

import utils

def main():
    num = utils.get_integer_number_min('Número: ', 0) 
    resultado = num/2
    while resultado > 1:
       resultado /= 2 
    
    print(f'{resultado}')


main()