import utils

def main():
    eleitores = utils.get_integer_number_min('Número de eleitores: ', 0)


    voto_xama = 0
    voto_petroquimico = 0
    voto_mourao = 0
    voto_nulo = 0
    voto_branco = 0
    for i in range(1, eleitores+1):
        voto = utils.get_integer_number_min('Voto: ', 0)

        if voto == 1: voto_xama += 1
        elif voto == 2: voto_petroquimico += 1
        elif voto == 3: voto_mourao += 1
        elif voto == 0: voto_branco
        else: voto_nulo += 1


    eleicoes = f'''==== ELEIÇÕES ADS 2025 ====
> TOTAL DE VOTOS DE CADA CANDIDATO:
Petroquímico: {voto_petroquimico} votos
Xamã: {voto_xama} votos
Mourão: {voto_mourao} votos
> VOTOS NULOS: {voto_nulo} votos
> VOTOS BRANCOS: {voto_branco} votos
E O VENCEDOR DA ELEIÇÃO É..... {vencedor(voto_xama, voto_petroquimico, voto_mourao)}

'''
    print(eleicoes)
utils.linhas()


def vencedor(voto_xama, voto_petroquimico, voto_mourao):

    if max(voto_xama, voto_mourao, voto_petroquimico) == voto_xama:
        return 'Xamã'
    elif max(voto_xama, voto_mourao, voto_petroquimico) == voto_mourao:
        return 'Mourão'
    else:
        return 'Petroquímico'

main()