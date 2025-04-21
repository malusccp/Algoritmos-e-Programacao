from minha_funcoes import obter_numero_inteiro

def main():
    num1 = obter_numero_inteiro('Digite um número: ')
    num2 = obter_numero_inteiro('Digite um número: ')
    num3 = obter_numero_inteiro('Digite um número: ')
    num4 = obter_numero_inteiro('Digite um número: ')
    num5 = obter_numero_inteiro('Digite um número: ')
    media_aritmetica(num1, num2, num3, num4, num5)

def media_aritmetica(num1, num2, num3, num4, num5):
    media = (num1 + num2 + num3 + num4 + num5)/5
    if num1 > media:
      print(f'O número {num1} é maior que a média')
    if num2 > media:
        print(f'O número {num2} é maior que a média')
    if num3 > media:
        print(f'O número {num3} é maior que a média')
    if num4 > media:
        print(f'O número {num4} é maior que a média')
    if num5 > media:
        print(f'O número {num5} é maior que a média')

main()

