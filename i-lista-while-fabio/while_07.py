import uteis


def main():
    n = uteis.get_integer_number_min("Escreva um número 'N': ", 1)
    uteis.linhas()
    print(f'A soma dos números de 1 até {n} é igual a {soma_numeros_1_a_N(n)}')
    uteis.linhas()


def soma_numeros_1_a_N(n: int):
    soma = 0
    contador = 1  
    while contador <= n:
        soma += contador
        contador += 1
    return soma
    
main()