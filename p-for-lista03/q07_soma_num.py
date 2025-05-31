def main():
    N = int(input('N: '))

    soma = 0
    for number in range(1,N+1,1):
        soma += number
    print(soma)


main()
