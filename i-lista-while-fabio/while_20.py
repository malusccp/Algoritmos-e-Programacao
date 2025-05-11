import uteis

def main():
    num = uteis.get_integer_number_min("Número: ", 1)
    uteis.linhas()
    calcular_s(num)


def calcular_s(num: int) -> float:
    denominador = num
    sinal = 1
    soma = 1 - (1/denominador) * sinal
    while denominador <= num :
        soma += (1/denominador) * sinal
        denominador += 1
        sinal *= -1
 
            
    print(f'O valor de S é --> {soma: .2f}')
    uteis.linhas()

main()