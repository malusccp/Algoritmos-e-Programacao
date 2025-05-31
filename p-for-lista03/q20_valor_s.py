import utils

def main():
    N = utils.get_integer_number_min('N: ', 0)

    S = 0
    sinal = 1
    for i in range(1, N+1, 1):
        S += 1/i * sinal
        sinal *= -1
    print(f'{S:.2f}')

main()