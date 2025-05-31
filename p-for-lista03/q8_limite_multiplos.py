
def main():
    N = int(input('N: '))
    limite_inf = int(input('Limite Inferior: '))
    limite_sup = int(input('Limite Superior: '))

    for i in range(limite_inf,limite_sup,1):
        if i % N == 0:
            print(i)



main()
