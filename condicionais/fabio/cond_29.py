from minha_funcoes import obter_numero_inteiro
import math

def main():
    num = obter_numero_inteiro('Digite um número de 4 dígitos: ')
    eh_quadrado_perfeito(num)


def eh_quadrado_perfeito(num):
    if math.sqrt(num) == soma_dezenas(num):
        return print(f'{num} é um quadrado perfeito')
    else:
        return print(f'{num} não é um quadrado perfeito')


def soma_dezenas(num):
    d1 = (num // 1000) * 10 
    d2 = ((num % 1000) // 100)
    d3 = (((num % 1000) % 100) // 10) * 10
    d4 = ((num % 100) % 100) % 10
    return (d1+d2) + (d3+d4)


main()