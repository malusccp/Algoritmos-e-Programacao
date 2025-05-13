
from minha_funcoes import obter_numero_real

def main():
    num = obter_numero_real('Digite um número real: ')
    parte_fracionaria = obter_numero_real('Digite a parte fracionária: ')
    arredondamento(num, parte_fracionaria)


def arredondamento(num, parte_fracionaria):
    if parte_fracionaria >= 0.5:
        return print(f' O número {num} é aproximadamente {(num - parte_fracionaria) + 1}')
    else:
        return print(f' O número {num} é aproximadamente {(num - parte_fracionaria) - 1}')
    

main()