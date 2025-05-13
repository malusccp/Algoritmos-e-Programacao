def main():
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite um número: '))
    numero3 = int(input('Digite um número: '))
    igualdade_numeros(numero1, numero2, numero3)

def igualdade_numeros(numero1, numero2, numero3):
    if numero1 == numero2 != numero3 or numero3 == numero2 != numero1 or numero1 == numero3 != numero2 :
        print('Existem dois números iguais')
    elif numero1 == numero2 == numero3:
        print('Existem três números iguais')
    elif numero1 != numero2 != numero3:
        print('Não existe nenhum número igual')


main()
