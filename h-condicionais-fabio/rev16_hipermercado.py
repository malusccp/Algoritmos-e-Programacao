# 16. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#        Até 5 Kg   |    Acima de 5 Kg
# File R$ 4,90 por Kg R$ 5,80 por Kg
# Alcatra R$ 5,90 por Kg R$ 6,80 por Kg
# Picanha R$ 6,90 por Kg R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
# cliente receberá ainda um desconto de 5% sobre o total a compra. Escreva um programa que peça o tipo
# e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da
# compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

import utils

def main():
    tabela_carne = ''' === HIPERMERCADO TABAJARA ===
    > Filé = 0
    > Alcatra = 1
    > Picanha = 2

'''
    print(tabela_carne)
    tipo_carne = utils.get_int_in_range('Digite o tipo de carne que deseja comprar: ', 0, 2)
    kg_carne = utils.get_decimal_number_min('Digite quantos kg de carne deseja comprar: ', 0)
    metodo_de_pagamento = utils.get_int_in_range('Deseja pagar usando o cartão Tabajara?(0 = NÃO | 1 = SIM): ', 0, 1)
    utils.limpar_tela()
    cupom_fiscal = f''' === CUPOM FISCAL ===
    > TIPO DE CARNE: {carne(tipo_carne)}
    > QUANTIDADE DE CARNE: {kg_carne}kg
    > PREÇO TOTAL: R${preço_carne(tipo_carne, kg_carne): .2f}
    > USOU CARTÃO TABAJARA?: {cartao(metodo_de_pagamento)}
    > DESCONTO: R${desconto_cartao(tipo_carne, kg_carne, metodo_de_pagamento): .2f}
    > VALOR A PAGAR: R${desconto_total(tipo_carne, kg_carne, metodo_de_pagamento)}
'''
    utils.linhas()
    print(cupom_fiscal)
    utils.linhas()

def preço_carne(tipo_carne: int, kg_carne: float ):
    if tipo_carne == 0:
        if kg_carne <= 5:
            return 4.90 * kg_carne
        elif kg_carne > 5:
            return 5.80 * kg_carne
    if tipo_carne == 1:
       if kg_carne <= 5:
            return 5.90 * kg_carne
       elif kg_carne > 5:
            return 6.80 * kg_carne
    if tipo_carne == 2:
       if kg_carne <= 5:
            return 6.90 * kg_carne
       elif kg_carne > 5:
            return 7.80 * kg_carne

def desconto_cartao(tipo_carne:int, kg_carne: float, metodo_de_pagamento: int):
    if metodo_de_pagamento == 1:
        return preço_carne(tipo_carne, kg_carne) * 0.05
    else:
        return 0


def desconto_total(tipo_carne: int, kg_carne: float, metodo_de_pagamento: int):
    if metodo_de_pagamento == 1:
        preço_final = preço_carne(tipo_carne, kg_carne) - desconto_cartao(tipo_carne, kg_carne, metodo_de_pagamento)
        return preço_final
    else:
        return preço_carne(tipo_carne, kg_carne)


def carne(tipo_carne):
    if tipo_carne == 0:
        return 'Filé'
    elif tipo_carne == 1:
        return 'Alcatra'
    else:
        return 'Picanha'


def cartao(metodo_de_pagamento):
    if metodo_de_pagamento == 1:
        return 'SIM'
    else:
        return 'NÃO'
main()
    



