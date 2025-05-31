import utils

def main():
    N = utils.get_integer_number_min('N: ', 0)

    maior = 0
    for N in range(1, N+1, 1):
        numero = utils.get_integer_number_min('Número: ', 0)
        if numero > maior:
            maior = numero
    
    print(f'O maior número da lista é {maior}')

main()