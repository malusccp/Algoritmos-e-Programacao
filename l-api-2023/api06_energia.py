# [energia.js] Em 2021 o Brasil voltou a enfrentar crise na matriz energética devido ao baixo nível das águas nos reservatórios das hidrelétricas
# brasileiras. Devido a isso os consumidores deverão arcar com custos extras (bandeira) para bancar outras matrizes energéticas, como usinas
# termoelétricas. Neste mês de Junho a bandeira estabelecida pelo governo federal foi a Vermelha Patamar 2, que significa que a cada 100 KWh de
# consumo será acrescido uma taxa extra de R$ 8,00.
# O Cálculo da energia elétrica para o consumidor final é feito baseado em KWh e em faixas.
# Valores hipotéticos:
# ● Consumo de até 30KWh isento de tarifa.
# ● Até 100 KWh será cobrado R$ 0,59 por cada um cada de todo os KWh consumidos;
# ● acima de 100KWh o valor de R$ 0,75 por cada um de todos os KWh consumidos.

# Sobre o valor tarifado/apurado são 25% de ICMS e 15% de PIS/CONFIS.
# A taxa de iluminação pública é cobrada apenas para os consumidores que passarem de 80 KWh por mês, e custa 6% do valor tarifado (antes do
# impostos).
# Considerando os dados acima construa um software que receba dois dados:
# Leitura Atual e Leitura Anterior do medidor de energia e faça todo o cálculo do "Talão de Energia" conforme detalhado acima.
# Como saída apresente os dados que compõem assim como o valor total a ser pago.
# Exemplo:
# Consumo 000 KWh
# Valor Faturado R$ 0,00
# Bandeira R$ 0,00 (x bandeiras)
# ICMS R$ 0,00
# PIS/CONFIS
# Taxa Iluminação R$ 0,00

import utils

def tarifa(leitura: float):
    if leitura <= 30:
        return 0
    elif leitura <= 100:
        return 0.59 * leitura
    else:
        return 0.75 * leitura


def taxa_iluminacao(leitura: float, leitura_anterior: float):
    if leitura > 80:
        return tarifa(leitura_anterior) * 0.06
    else:
        return 0


def taxa_extra(leitura: float):
    contador = 0
    while leitura > 0 and leitura >= 100:
        leitura -= 100
        contador += 1
    return contador 


def main():
    leitura_atual = utils.get_decimal_number_min('Digite a leitura atual do medidor de energia: ', 0)
    leitura_anterior = utils.get_decimal_number_min('Digite a leitura anterior do medidor de energia: ', 0)

    valor_faturado = taxa_extra(leitura_atual) + taxa_iluminacao(leitura_atual, leitura_anterior) + (tarifa(leitura_atual) * 8)

    talao = f'''=== TALÃO DE ENERGIA ===
> Consumo: {leitura_atual} KWh
> Valor Faturado: R${valor_faturado:.2f}
> Bandeira: R${(8*taxa_extra(leitura_atual)):.2f} ({taxa_extra(leitura_atual)} bandeiras)
> ICMS: R${tarifa(leitura_atual)*0.25:.2f}
> PIS/CONFIS: R${tarifa(leitura_atual)*0.15:.2f}
> Taxa Iluminação: R${taxa_iluminacao(leitura_atual, leitura_anterior):.2f}'''
    print(talao)



main()

