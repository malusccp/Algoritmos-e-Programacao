# 6. Escreva um algoritmo para determinar o número de dígitos de um número informado.

def main():
    num = int(input('Número: '))

    digitos = 0
    for i in range(num):
        num /= 10
        digitos +=1
        if num < 1: break
    print(f'O número tem {digitos} dígitos')

main()