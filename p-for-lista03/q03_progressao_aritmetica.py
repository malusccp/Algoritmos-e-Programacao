def main():
    a0 = int(input('A0: '))
    limite = int(input('Limite: '))
    R = int(input('R: '))

    for pa in range(a0, limite+1,R):
        if pa < limite:
            print(pa)

main()