import math
import utils

def main():
    limite_inf = utils.get_integer_number_min('Limite Inferior: ', 0)
    limite_sup = utils.get_integer_number_min('Limite Superior: ', 0)

    for i in range(limite_inf, limite_sup, 1):
        if eh_primo(i) == True: print(i)





def eh_primo(num: int):
    if num <= 1: return False
    if num == 2: return True
    if num > 2: 
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0: return False
        return True





main()