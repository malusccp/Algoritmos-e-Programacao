import utils

def main():
    N = utils.get_integer_number_min('N: ', 0)

    soma = 0
    for N in range(1, N+1, 1):
        numero = utils.get_integer_number_min('Número: ', 0)
        soma += numero
    
    print(f'Soma: {soma}\nMédia: {soma/N} ')

main()