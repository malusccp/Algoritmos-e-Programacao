def main():
    numero = int(input('Número: '))

    for i in range(numero-1, 1, -1):
        numero *= i

    print(numero)

main()