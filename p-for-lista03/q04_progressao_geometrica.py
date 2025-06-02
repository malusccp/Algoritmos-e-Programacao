def main():
    a0 = int(input('A0: '))
    limite = int(input('Limite: '))
    R = int(input('R: '))

    print(a0)
    for i in range(99999999999999999):
        a0 *= R
        if a0 <= limite:
            print(a0)
        else: break
    


main()