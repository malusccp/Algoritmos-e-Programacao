import uteis

def main():
    qtd_numeros = uteis.get_integer_number_min('Digite quantos números deseja adicionar a lista: ', 0)
    contador = 1
    maior = 0

    uteis.linhas()
    
    verificar_maior_numero(qtd_numeros)


def verificar_maior_numero(qtd_numeros:int):
    contador = 1
    maior = 0
    while contador <= qtd_numeros:
        numero = uteis.get_integer_number_min('Digite um número: ', 0)
        if numero > maior:
            maior = numero
        contador += 1

    uteis.linhas()
    print(f'O maior valor é: {maior}')
    uteis.linhas

    




main()




