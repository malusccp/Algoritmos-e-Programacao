def main():
    num1 = int(input('Número 1: '))
    num2 = int(input('Número 2: '))

    for i in range(maior_num(num1, num2), num1*num2 +1):
        if i % num1 == 0 and i % num2 == 0: break

    print(f'O MMC({num1},{num2}) é igual a {i}')


def maior_num(num1: int, num2: int):
    if num1 > num2: return num1
    elif num2 > num1: return num2

main()