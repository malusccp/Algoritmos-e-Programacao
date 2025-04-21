from minha_funcoes import obter_numero_inteiro


def main():
    num = obter_numero_inteiro('Digite o número desejado: ')
    eh_par(num)


def eh_par(num):
    if num % 2 == 0:
        return print(f'O número {num} é par')
    else:
        return print(f'O número {num} é ímpar')
    
main()