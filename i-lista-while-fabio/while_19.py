import uteis

def main():
    num = uteis.get_integer_number_min("Número: ", 1)
    uteis.linhas()
    calcular_s(num)


def calcular_s(num: int):
    numerador = 1
    denominador = num
    soma = 0
    sinal = 1
    while numerador <= num :
        soma += (numerador/denominador) * sinal
        numerador += 1
        denominador -= 1
        sinal *= -1
 
            
    
    print(f'O valor de S é --> {soma}')
    uteis.linhas()

main()