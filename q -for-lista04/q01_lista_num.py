

def main():

    while True:
        numero = int(input('Número: '))
        if numero == 0: break
        
        print(f'Divisores de {numero}:')

        for i in range(1, numero+1):
            if numero % i == 0: print(i)


main()
