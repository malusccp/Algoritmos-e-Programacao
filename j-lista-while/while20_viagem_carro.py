# 20. Considere que um carro vai fazer uma viagem entre duas cidades e que a distância a ser percorrida é de
# 600 km. No início da viagem, o carro está com o tanque cheio (50 litros). Durante o percurso foi usado
# um aparelho para medir o desempenho do carro, que mostrava, quando acionado, duas informações:
# · Distância percorrida desde a última medição;
# · Quantidade de litros consumidos para percorrer a distância indicada.
# Escreva um algoritmo que leia estas informações e escreva:
# · se o carro chegou ao seu destino (distância percorrida maior ou igual a 600 km);
# · se o carro parou antes de chegar por falta de combustível (consumo igual a 50 litros);
# · o consumo em km/l do carro.
import utils

def main():
    distancia_percorrida = utils.get_decimal_number_min('Distância percorrida desde a última medição(km): ', 600)
    litros_usados = utils.get_decimal_number_min('Quantidade de litros consumidos para percorrer a distância indicada(L): ')

    consumo = distancia_percorrida/litros_usados
    while not distancia_percorrida >= 600 or litros_usados == 50:




