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
    numero_prova = utils.get_integer_number_min('Número da prova: ', 0)
    qtd_de_nadadores = utils.get_integer_number_min('Quantidade de nadadores: ', 0)
    contador = 0
    pontos_a = 0
    pontos_b = 0
    while qtd_de_nadadores > contador:
        nome = str(input('Nome do nadador: '))
        classificacao = utils.get_int_in_range('Classificação do nadador: ', 1,4)
        tempo = utils.get_integer_number_min('Tempo: ', 0)
        clube = utils.get_int_in_range('Clube (0 = Clube A | 1 = Clube B): ', 0,1)
        contador += 1

        if classificacao == 1:
            if clube == 0:
                pontos_a += 9
            else:
                pontos_b += 9
        elif classificacao == 2:
            if clube == 0:
                pontos_a += 6
            else:
                pontos_b += 6
        elif classificacao == 3:
            if clube == 0:
                pontos_a += 4
            else:
                pontos_b += 4
        else:
            if clube == 0:
                pontos_a += 3
            else:
                pontos_b += 3
    contador_de_pontos(pontos_a, pontos_b)


def contador_de_pontos(pontos_a: int, pontos_b: int):
    if pontos_a > pontos_b:
        utils.linhas()
        print('=== COMPETIÇÃO DE NATAÇÃO ===')
        print(f'=== TOTAL DE PONTOS: ===\n> CLUBE A:{pontos_a}\n> CLUBE B: {pontos_b}')
        print('VENCEDOR : CLUBE A')
    else:
        utils.linhas()
        print('=== COMPETIÇÃO DE NATAÇÃO ===')
        print(f'=== TOTAL DE PONTOS: ===\n> CLUBE A: {pontos_a}\n> CLUBE B: {pontos_b}')
        print('VENCEDOR : CLUBE B')
        



    
main()