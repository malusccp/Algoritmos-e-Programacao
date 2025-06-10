def main():
    num = int(input('Número: '))
    print(calcular_fatorial(num))


def calcular_fatorial(num: int, anterior=1):
    fatorial = num
    if anterior >= num: return fatorial
    fatorial = fatorial * anterior
    calcular_fatorial(num, anterior+1)


main()
