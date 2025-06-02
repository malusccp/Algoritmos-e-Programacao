def main():
    num1 = int(input('Número 1: '))
    num2 = int(input('Número 2: '))

    for i in range(menor_num(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0: break

    print(f'O MDC({num1},{num2}) é igual a {i}')


def menor_num(num1: int, num2: int):
    if num1 > num2: return num2
    elif num2 > num1: return num1

main()