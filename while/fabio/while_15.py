import uteis

def main():
    qtd_sequencia = uteis.get_integer_number_min("Número: ", 1)
    uteis.linhas()
    print(f"Os primeiros {qtd_sequencia} termos da sequência são:")
    escrever_sequencia(qtd_sequencia)


def escrever_sequencia(qtd_sequencia: int):
    contador = 0
    sequencia = 0
    while qtd_sequencia > contador:
       sequencia += 1 + contador
       contador += 1
       print(f'{sequencia}')
    uteis.linhas()

    

main()