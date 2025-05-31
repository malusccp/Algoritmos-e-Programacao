import utils

def main():
    N = utils.get_integer_number_min('N: ', 2)

    x = 0
    y = 1

    for i in range(N):
        print(x)
        proximo = x + y
        x = y
        y = proximo
        






main()