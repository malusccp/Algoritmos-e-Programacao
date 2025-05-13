import uteis 

def main():
    num = uteis.get_integer_number_min("Número: ", 1)
    uteis.linhas()
    calcular_s(num)


def calcular_s(num: int):
    contador = 0
    numerador = 1
    denominador = num
    soma = 0
    while contador < num :
        soma += numerador/denominador
        contador += 1
        numerador += 1
        denominador -= 1
    print(f'O valor de S é --> {soma: .2f}')
    uteis.linhas()

main()