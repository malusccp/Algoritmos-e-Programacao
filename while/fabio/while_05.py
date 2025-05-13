import uteis

def main():
    numero = uteis.get_integer_number_min("Escreva o número para calcular seu fatorial: ", 0)
    uteis.linhas()
    print(f"O valor de {numero}! é igual a {calcular_fatorial(numero)} ")
    uteis.linhas()

def calcular_fatorial(numero: int):
    contador = numero
    while contador > 1:
        contador -= 1
        numero *= contador
    return numero


main()