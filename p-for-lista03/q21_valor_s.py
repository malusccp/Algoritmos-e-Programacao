import utils

def main():
    N = utils.get_integer_number_min('N: ', 0)

    numerador = 1
    S = 0
    for denominador in range (1, N+1):
        termo = numerador / denominador
        S += termo
        numerador += 2

    print(f'S = {S:.2f}')


main()