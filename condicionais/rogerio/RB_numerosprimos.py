import math

def main():
    num = int(input('Digite o número e verifique se é primo ou não: '))
    verificar_primo(num)


def verificar_primo(num):
    if num <= 1:
        return print(f'O número {num} não é primo')
    if num == 2:
        return print(f'O número {num} é primo')
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return print(f'O número {num} não é primo!!')
        else:
            return print(f'O número {num} é primo!!')
        


main()