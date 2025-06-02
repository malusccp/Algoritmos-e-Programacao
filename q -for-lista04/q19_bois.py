# 19. Em um frigorífico, cada boi traz em seu pescoço um cartão contendo o seu n.o de identificação e seu
# peso. Escreva um algoritmo que leia um conjunto de cartões e escreva o n.o de identificação e o peso do
# boi mais magro e do boi mais gordo. (Flag: n.o identificação=0)

import utils

def main():
    n = utils.get_integer_number_min("Escreva a quantidade de bois: ", 0)
    utils.linhas()
    identificar_boi(n)


def identificar_boi(n: int):
    boi_mais_gordo = None
    numero_boi_gordo = 0
    boi_mais_magro = None
    numero_boi_magro = 0
    for i in range(1, n+1, 1):
        numero_boi = utils.get_integer_number_min("Escreva o número de identificação do boi: ", 0)
        peso_boi = utils.get_integer_number_min("Escreva o peso (kg) do boi: ", 1)

        if boi_mais_gordo == None or peso_boi > boi_mais_gordo:
            boi_mais_gordo = peso_boi
            numero_boi_gordo = numero_boi


        if boi_mais_magro == None or peso_boi < boi_mais_gordo :
            boi_mais_magro = peso_boi
            numero_boi_magro = numero_boi

    utils.linhas()
    print(f"N° de Identificação do boi mais gordo: {numero_boi_gordo}\nPeso boi mais gordo: {boi_mais_gordo} ")
    utils.linhas()
    print(f"N° de Identificação do boi mais magro: {numero_boi_magro}\nPeso boi mais magro: {boi_mais_magro} ")
    utils.linhas()


main()