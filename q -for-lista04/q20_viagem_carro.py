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
    distancia_total = 0
    combustivel_total = 0
    while True:
        distancia_percorrida = utils.get_decimal_number_min('Distância percorrida: ', 0)
        litros_consumidos = utils.get_decimal_number_min('Litros consumidos: ', 0)

        distancia_total += distancia_percorrida
        combustivel_total += litros_consumidos

        if combustivel_total >= 50:
            print('O carro parou antes de chegar por falta de combustível')
            print(f'Consumo (km/l): {distancia_percorrida/50:.2f}')
            break

        elif distancia_total >= 600:
            print('O carro chegou ao destino')
            print(f'Consumo (km/l): {distancia_percorrida/combustivel_total:.2f}')
            break
    

main()