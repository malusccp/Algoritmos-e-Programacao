# Confira o resultado de uma competição de natação entre dois clubes. O programa deve ler o número da
# prova e a quantidade de nadadores. O fim dos dados é indicado pelo número da prova igual a 0 e
# quantidade de nadadores igual a 0. A seguir, para cada nadador deverá ler nome, classificação, tempo,
# clube (“a” ou “b”) e determinar os pontos obtidos por cada clube, de acordo com o seguinte critério:

# Lugar Pontos
# 1       9
# 2       6
# 3       4
# 4       3


# Ao final, o algoritmo deve escreva os totais de pontos de cada clube, indicando o clube vencedor.
import utils

def main():

    pontos_clube_a = 0
    pontos_clube_b = 0

    numero_prova = utils.get_integer_number_min('Número da prova: ', 0)
    qtd_nadadores = utils.get_integer_number_min('Número de nadadores: ', 0)

    while numero_prova != 0 or qtd_nadadores != 0:
        for i in range(1, qtd_nadadores+1, 1):
            nome_nadador = str(input(f'Nome do nadador {i}: '))
            classificacao = utils.get_int_in_range('Classificação do nadador: ', 1, 4)
            tempo = utils.get_integer_number_min('Tempo: ', 1)
            clube = str(input('Clube: '))

            pontos = calcular_pontos(classificacao)

            if clube.upper() == 'A': pontos_clube_a += pontos
            else: pontos_clube_b += pontos

        numero_prova = utils.get_integer_number_min('Número da prova: ', 0)
        qtd_nadadores = utils.get_integer_number_min('Número de nadadores: ', 0)

    vencedor = 'Empate'
    if pontos_clube_a > pontos_clube_b:
        vencedor = 'Clube A venceu'
    elif pontos_clube_b > pontos_clube_a: 
        vencedor = 'Clube B venceu'


    print(f''' === COMPETIÇÃO DE NATAÇÃO ===
> CLUBE A: {pontos_clube_a} pontos
> CLUBE B: {pontos_clube_b} pontos
--------------------------------------------------------
> VENCEDOR: {vencedor}
''')


def calcular_pontos(classificacao: int):
     if classificacao == 1: return 9
     elif classificacao == 2: return 6
     elif classificacao == 3: return 4
     elif classificacao == 4: return 3
     else: return 0
     


main()