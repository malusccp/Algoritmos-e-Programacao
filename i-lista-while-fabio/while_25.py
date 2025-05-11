import uteis

def main():
    eleitores = uteis.get_integer_number_min("N° de Eleitores: ", 1)
    print(">>>> ELEIÇÕES NEOQUÍMICA ARENA <<<<")
    ler_votos(eleitores)


def ler_votos(eleitores: int):
    contador = 0
    voto_1 = 0
    voto_2 = 0
    voto_3 = 0
    voto_branco = 0
    voto_nulo = 0
    while contador < eleitores:
        voto = uteis.get_integer_number('Digite o candidato em que deseja votar: ')

        if voto == 1:
         voto_1 += 1
        elif voto == 2:
         voto_2 += 1
        elif voto == 3:
         voto_3 += 1
        elif voto == 0:
           voto_branco += 1
        elif voto == 9:
           voto_nulo += 1
        else:
           print("Candidato Inexistente. Verifique novamente o código de votação.")
           uteis.linhas()
           voto = uteis.get_integer_number('Digite o candidato em que deseja votar: ')
           uteis.linhas
           return resultado(voto_1, voto_2, voto_3)
        
        contador += 1
    resultado(voto_1, voto_2, voto_3)


def resultado(voto_1: int, voto_2: int, voto_3:int):
    if voto_1 > voto_2 and voto_1 > voto_3:
       uteis.linhas()
       print(f"Fabrizio Angileri ganha com {voto_1} votos")
    if voto_2 > voto_1 and voto_2 > voto_3:
       uteis.linhas()
       print(f"Memphis Depay ganha com {voto_2} votos")
       uteis.linhas()
    if voto_3 > voto_1 and voto_3 > voto_2:
       uteis.linhas()
       print(f"Yuri Alberto ganha com {voto_3} votos")
       uteis.linhas()
    

    
main()