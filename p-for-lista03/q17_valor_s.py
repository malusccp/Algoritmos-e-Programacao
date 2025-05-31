import utils

def main():
    N = utils.get_int_num_min('N: ', 0)

    S = 0
    for i in range(1, N+1, 1):
        S += 1/i
    print(f'{S:.2f}')

main()