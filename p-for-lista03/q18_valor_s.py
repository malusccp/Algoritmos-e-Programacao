import utils

def main():
    N = utils.get_integer_number_min('N: ', 0)

    S = 0
    numerador = 1
    denominador = N
    for i in range(1, N+1):
        S += numerador/denominador
        numerador = i + 1
        denominador -= 1

    print(f'{S: .2f}')

main()