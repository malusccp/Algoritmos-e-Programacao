def main():
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite um número: '))
    numero3 = int(input('Digite um número: '))
    maior_numero(numero1, numero2, numero3)


def maior_numero(numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3:
        return print(f'O número {numero1} é o maior')
    if numero2 > numero1 and numero2 > numero3:
        return print(f'O número {numero2} é o maior')
    if numero3 > numero1 and numero3 > numero2:
        return print(f'O número {numero3} é o maior')
    if numero1 == numero2 == numero3:
        return print(f'Os números possuem o mesmo valor')



main()