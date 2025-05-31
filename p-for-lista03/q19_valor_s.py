import utils

def main():
    N = utils.get_integer_number_min('N: ', 0)

    
    S = 0
    numerador = 1
    denominador = N
    sinal = 1
    for i in range(N):
        S += sinal * (numerador / denominador)

        if i % 2 == 0: numerador = N - numerador
        else: numerador = i + 2

        denominador = N - i - 1

        sinal *= -1

    print(f'S = {S}')

main()