def main():
    limite_inf = int(input('Limite Inferior: '))
    limite_sup = int(input('Limite Superior: '))

    for i in range(limite_inf,limite_sup,1):
        if not i % 2 == 0:
            print(i)


main()