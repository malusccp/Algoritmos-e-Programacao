import uteis

def main():
    numero = uteis.get_integer_number_min('Escreva um número "N" para realizar a contagem: ', 1)
    uteis.linhas()
    string(numero)
    ler_numeros_pares(numero)
    uteis.linhas()

def string(numero: int):
    if numero != 1:
        print(f'Os números pares de 1 até {numero} são: ')
    else:
        print(f'Não existem números pares de 1 até {numero}. ')


def ler_numeros_pares(numero: int):
    contador = 1
    while numero >= contador:
        if contador % 2 == 0:
            print(contador)
        contador += 1

main()