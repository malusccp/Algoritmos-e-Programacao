import utils

def main():
    N = utils.get_integer_number_min('N: ', 0)

    soma = 0
    for i in range(1, N+1):
        soma += i

        print(soma)
main()

