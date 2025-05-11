import uteis

def main():
    n = uteis.get_integer_number("Escreva um número 'N': ")
    limite_inferior = uteis.get_integer_number("Escreva o limite inferior: ")
    limite_superior = uteis.get_integer_number_min("Escreva o limite superior: ", limite_inferior+1)
    uteis.linhas()
    print(f"Os múltiplos de {n} dentro do intervalo de ({limite_inferior} - {limite_superior}) são iguais a: ")
    multiplos_de_N(n, limite_inferior, limite_superior)
    uteis.linhas()

def multiplos_de_N(n: int, limite_inferior:int, limite_superior:int):
    candidato = limite_inferior
    while candidato <= limite_superior:
        if candidato % n == 0:
            print(candidato)
        candidato += 1

main()
