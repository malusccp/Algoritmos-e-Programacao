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

    for i in range(9999999):
        numero_prova = utils.get_integer_number_min('Número da prova: ', 0)
        qtd_nadadores = utils.get_integer_number_min('Número de nadadores: ', 0)


        if numero_prova == 0 and qtd_nadadores == 0: break

        for i in range(1, qtd_nadadores+1, 1):
            nome_nadador = str(input('Nome do nadador: '))
            classificacao = utils.get_int_in_range('Classificação do nadador: ', 1, 4)
            tempo = utils.get_integer_number_min('Tempo: ', 1)
            clube = str(input('Clube: '))

            if classificacao == 1: 
                if clube.upper() == 'A': pontos_clube_a += 9 
                else: pontos_clube_b += 9
            elif classificacao == 2: 
                if clube.upper() == 'A': pontos_clube_a += 6
                else: pontos_clube_b += 6
            elif classificacao == 3: 
                if clube.upper() == 'A': pontos_clube_a += 4
                else: pontos_clube_b += 4
            elif classificacao == 4: 
                if clube.upper() == 'A': pontos_clube_a += 3
                else: pontos_clube_b += 3

    print(f''' === COMPETIÇÃO DE NATAÇÃO ===
> CLUBE A: {pontos_clube_a} pontos
> CLUBE B: {pontos_clube_b} pontos
--------------------------------------------------------
> VENCEDOR: {vencedor(pontos_clube_a, pontos_clube_b)}
''')

def vencedor(pontos_a: int, pontos_b: int):
    if pontos_a > pontos_b: return 'Clube A'
    else: return 'Clube B'

main()