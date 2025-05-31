import utils
import math

def main():
    N = utils.get_integer_number_min('N: ', 0)

    for i in range(N-1, 1, -1):
        if math.sqrt(i) == int(math.sqrt(i)):
            break
    print(f'O maior menor quadrado perfeito é {i}')

main()