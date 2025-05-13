from minha_funcoes import obter_numero_inteiro
import math

def main():
    a = obter_numero_inteiro('Digite o valor do coeficiente a: ')
    b = obter_numero_inteiro('Digite o valor do coeficiente b: ')
    c = obter_numero_inteiro('Digite o valor do coeficiente c: ')
    if a == 0:
        print('O valor de a deve ser diferente de 0')
        return main()
    else:
        calcular_raizes(a,b,c)



def calcular_delta(a,b,c):
    return b**2 - 4 * a * c

def calcular_raizes(a,b,c):
    raiz1 = (-b + math.sqrt(calcular_delta(a,b,c)))/2 * a
    raiz2 = (-b - math.sqrt(calcular_delta(a,b,c)))/2 * a
    return print(f'As raízes da equação do 2° grau são iguais a {raiz1, raiz2}')

main()