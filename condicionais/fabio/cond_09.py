import math

def main():
    num = int(input('Digite um número entre 0 e verifique se é primo ou não: '))
    verificar_primo(num)


def verificar_primo(num):
    if num <= 1:
        return print(f'O número {num} não é primo')
    elif num == 2:
        return print(f'O número {num} é primo')
    elif num % 2 == 0:
        return print(f'O número {num} não é primo')
    elif num == 3:
        return print(f'O número {num} é primo')
    elif num % 3 == 0:
        return print(f'O número {num} não é primo')
    elif num == 5:
        return print(f'O número {num} é primo')
    elif num % 5 == 0:
        return print(f'O número {num} não é primo')
    elif num == 7:
        return print(f'O número {num} é primo')
    elif num % 7 == 0:
        return print(f'O número {num} não é primo')
    

        


main()