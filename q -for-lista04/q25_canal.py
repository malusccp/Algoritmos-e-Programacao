# 25. Foi feita uma pesquisa de audiência de canal de TV em várias casas em Teresina, num certo dia. Para
# cada casa visitada, o entrevistado informou o número do canal (2, 4, 5, 7, 10) e o número de pessoas que
# estavam assistindo TV. Escreva um algoritmo que leia um número indeterminado de dados (terminando
# quando for lido um canal igual a zero) e calcule o percentual de audiência para cada emissora,
# mostrando ao final, o número de cada canal e sua respectiva audiência.
import utils

def main():

    publico = 0
    canal_dois = 0
    canal_quatro = 0
    canal_cinco = 0
    canal_sete = 0
    canal_dez = 0
    for i in range(999999999999999):
        canal = utils.get_integer_number_min('Número do canal: ', 0)
        if canal == 0:
            break
        qtd_pessoas = utils.get_integer_number_min('Número de pessoas: ', 0)
        publico += qtd_pessoas
        if canal == 2: canal_dois += qtd_pessoas
        elif canal == 4: canal_quatro += qtd_pessoas
        elif canal == 5: canal_cinco += qtd_pessoas
        elif canal == 7: canal_sete += qtd_pessoas
        else: canal_dez += qtd_pessoas

    interface = f'''=== AUDIÊNCIA DAS EMISSORAS ===
CANAL 2: {100 * (canal_dois/publico):.2f}%
CANAL 4: {100 * (canal_quatro/publico):.2f}%
CANAL 5: {100 * (canal_cinco/publico):.2f}%
CANAL 7: {100 * (canal_sete/publico):.2f}%
CANAL 10: {100 * (canal_dez/publico):.2f}% '''
    print(interface)

main()