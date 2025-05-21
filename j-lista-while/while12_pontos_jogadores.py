# 12. Leia vários códigos do jogador (1 ou 2) que ganhou o ponto, em uma partida de pingue-pongue, e
# responda quem ganha a partida. A partida chega ao final se:
# · Um dos jogadores chega a 21 pontos e a diferença de pontos entre os jogadores é maior ou igual a 2.
# · Se a primeira não for atendida, ganha aquele que, com mais de 21 pontos, consiga colocar uma
# diferença de 2 pontos sobre o adversário.
import utils

def main():
    pontos_um = 0
    pontos_dois = 0
    while True:
        jogador_um = utils.get_integer_number_min('Pontos Jogador 1: ', 0)
        jogador_dois = utils.get_integer_number_min('Pontos Jogador 2: ', 0)

        pontos_um += jogador_um
        pontos_dois += jogador_dois

        if (pontos_um == 21 and pontos_um - pontos_dois >= 2) or (pontos_dois == 21 and pontos_dois - pontos_um >= 2):
            break
        elif pontos_dois > 21 or pontos_um > 21:
            if pontos_um > pontos_dois and (pontos_um - pontos_dois) >= 2:
                break
            elif pontos_dois > pontos_um and (pontos_dois - pontos_um >= 2):
                break
            break

    if pontos_um > pontos_dois:
        print(f'O ganhador é o jogador de número 1 com {pontos_um} pontos !')
    else:
        print(f'O ganhador é o jogador de número 2 com {pontos_dois} pontos ! ')
        
main()