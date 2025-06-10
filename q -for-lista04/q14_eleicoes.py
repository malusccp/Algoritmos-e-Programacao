# 14. Emita o resultado de uma pesquisa de opinião pública a respeito das eleições presidenciais. O
# entrevistado deverá escolher entre 3 candidatos (Serra=45, Dilma=13 ou Ciro Gomes=23), ou então
# responder: indeciso=99, outros=98, nulo/branco=0. O algoritmo deve ler a opinião de voto de cada
# entrevistado, encerrando-se a pesquisa com a opinião sendo igual a –1. Ao final, devem ser mostrados:
# · a porcentagem de cada candidato;
# · a porcentagem dos outros candidatos;
# · a porcentagem de eleitores indecisos;
# · a porcentagem de votos nulos/brancos;
# · o total de entrevistados;
# · uma mensagem indicando a possibilidade ou não de haver 2o turno.
import utils
def main():
    ciro = 0
    dilma = 0
    serra = 0
    outros = 0
    nulo = 0
    indeciso = 0
    total_eleitores = 0
    while True:
        voto = pedir_voto('Voto: ')
        if voto == -1:
            break
            
        if voto == 13: dilma += 1
        elif voto == 23: ciro += 1
        elif voto == 45: serra += 1
        elif voto == 99: indeciso += 1
        elif voto == 98: outros += 1
        else: nulo += 1


        total_eleitores += 1

    porcentagem_dilma = (dilma/total_eleitores)*100
    porcentagem_ciro = (ciro/total_eleitores)*100
    porcentagem_serra = (serra/total_eleitores)*100

    urna = f''' === CABINE ELEITORAL ===
> PORCENTAGEM DE VOTOS PARA DILMA (13): {porcentagem_dilma: .1f}%
> PORCENTAGEM DE VOTOS PARA O CIRO GOMES (23): {porcentagem_ciro: .1f}%
> PORCENTAGEM DE VOTOS PARA O SERRA (45): {porcentagem_serra: .1f}%
> PORCENTAGEM DE VOTOS PARA OUTROS CANDIDATOS: {(outros/total_eleitores)*100: .1f}%
> PORCENTAGEM DE ELEITORES INDECISOS: {(indeciso/total_eleitores)*100: .1f}%
> PORCENTAGEM DE VOTOS NULOS {(nulo/total_eleitores)*100: .1f}%
> TOTAL DE ELEITORES: {total_eleitores}
> TERÁ SEGUNDO TURNO?: {segundo_turno(porcentagem_dilma, porcentagem_serra, porcentagem_ciro)}
''' 
    print(urna)

def pedir_voto(label: str):
    voto = utils.get_integer_number(label)
    while not ((voto == 13) or (voto == 45) or (voto == 23) or (voto == -1) or (voto == 99) or (voto == 98) or (voto == 0)):
        print('Número de voto inválido. Tente novamente.')
        voto = utils.get_integer_number(label)
    return voto

def segundo_turno(porcentagem_dilma: float, porcentagem_serra: float, porcentagem_ciro: float):
    if porcentagem_dilma > 50 or porcentagem_serra > 50 or porcentagem_ciro > 50:
       return 'NÃO'
    else:
        return 'SIM'


main()