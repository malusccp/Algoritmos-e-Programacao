from minha_funcoes import obter_numero_inteiro
from minha_funcoes import eh_par

def main():
    x = obter_numero_inteiro('Digite um número: ')
    y = obter_numero_inteiro('Digite um número: ')
    condicoes(x, y)


def condicoes(x, y):
    if x % y == 1:
        return print(f'A soma de {x}, {y} e o resto é {(x + y) + 1} ')
    elif x % y == 2:
        eh_par(x)
        eh_par(y)
    elif x % y == 3:
        return print(f'A soma de {x} e {y} multiplicado por {x} é {(x + y) * x} ')
    elif x % y == 4 and y != 0:
        return print(f'A soma de {x} e {y} dividida por {y} é {(x + y) / y}')
    else:
        print(f'O quadrado dos números {x} e {y} é {x * x} e {y * y}, respectivamente.')

main()
    
