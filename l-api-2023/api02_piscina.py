# 2. [piscina.js] Uma piscina é algo muito legal de ter (...um amigo que
# tenha uma). Para evitar transbordar ao tomar banho na piscina é
# bom deixar o nível da água com no máximo 85% da capacidade.
# Assim uma piscina que comporta 20 mil litros de água é bom botar
# só 17 mil litros. Considere uma piscina estilo quadrada. Para
# encher a piscina ele usará água paga (o valor é cobrado por cada
# 1000 litros de água, em partes inteiras. Ou seja, se usar 1 litro já
# paga por 1000, ao usar 1002 já paga 2 mil litros)
# a. Calcule a capacidade máxima da piscina pedindo ao usuário as
# dimensões de largura, comprimento e profundidade (em cm). 1 litro é
# igual a 1000 cm3

# . Uma piscina por exemplo de capacidade →
# L=100cm x C=100cm x P=100cm → 1000 litros, e deve ser cheia até
# 850 litros apenas.
# b. Informe até quantos litros é recomendado encher a piscina.
# c. Peça ao usuário para informar o valor a ser pago por cada 1000 litros
# na concessionária de água de sua cidade, e informe quanto ele
# gastará para encher sua piscina;
# d. Mensalmente é necessário repor 10% da água devido a banho e
# evaporação, informe ao usuário também o gasto mensal para manter
# a piscina no nível ideal.
import utils

def main():
    largura = utils.get_decimal_number_min('Digite a largura da piscina(cm): ', 0)
    comprimento = utils.get_decimal_number_min('Digite o comprimento da piscina(cm): ', 0)
    profundidade = utils.get_decimal_number_min('Digite a profundidade da piscina(cm): ', 0)
    valor_litros = utils.get_decimal_number_min('Digite o valor a ser pago a cada 1000L: ', 0)

    capacidade = (largura * comprimento * profundidade)/1000
    nivel_de_agua_recomendado = capacidade* 0.85
    valor_encher_piscina = calcular_valor_piscina(nivel_de_agua_recomendado) * valor_litros
    reposiçao = nivel_de_agua_recomendado * 0.10
    valor_reposiçao = calcular_valor_piscina(reposiçao) * valor_litros

    interface = f''' === CÁLCULO GASTO DE PISCINA ===
    > CAPACIDADE DA PISCINA: {capacidade}CM³
    > NÍVEL DE ÁGUA RECOMENDADO: {nivel_de_agua_recomendado}CM³
    > VALOR PARA ENCHER A PISCINA: R${valor_encher_piscina: .2f}
    > VALOR PARA REPOR A ÁGUA MENSALMENTE: R${valor_reposiçao: .2f}
'''
    print(interface)


def calcular_valor_piscina(nivel_de_agua):
    contador = 0
    while nivel_de_agua > 0:
        nivel_de_agua -= 1000
        contador +=1

    return contador

main()