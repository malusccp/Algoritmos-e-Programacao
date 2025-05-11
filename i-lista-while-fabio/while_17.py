import uteis

def main():
    num = uteis.get_integer_number_min("Número: ", 0)
    uteis.linhas()
    calcular_s(num)


def calcular_s(num: int):
    contador = 0
    soma = 0
    while contador < num:
        contador += 1
        soma += 1/contador 
    print(f'O valor de S é --> {soma: .2f}')
    uteis.linhas()

main()