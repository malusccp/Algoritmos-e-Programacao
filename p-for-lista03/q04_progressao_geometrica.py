def main():
    a0 = int(input('A0: '))
    limite = int(input('Limite: '))
    R = int(input('R: '))

    termo = a0
    for i in range(a0, limite, 1):
        termo *= R
        if termo <= limite:
            print(termo)
    


main()