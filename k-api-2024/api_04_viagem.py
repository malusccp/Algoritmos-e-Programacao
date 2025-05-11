import utils

def main():
    print('=== COMPARATIVO DE PASSAGENS AÉREAS ===')
    utils.linhas()
    origem = utils.string('Origem: ')
    destino = utils.string('Destino: ')
    valor_passagem_reais = utils.get_decimal_number_min('Valor da passagem do site: ', 0)
    valor_milhas = utils.get_decimal_number_min('Valor da passagem em milhas: ', 0)
    utils.linhas()

    valor_milhas_padrao = (valor_milhas * 70) / 1000
    porcentagem_milhas_padrao = (valor_milhas_padrao / valor_passagem_reais) * 100
    valor_milhas_baratas = (valor_milhas * 14.50) / 1000
    porcentagem_milhas_baratas = (valor_milhas_baratas / valor_passagem_reais) * 100

    print(f'''  ========== COMPARATIVO DE PASSAGENS ==========
    VALOR EM MILHAS PADRÃO = R${valor_milhas_padrao: .2f}
    PORCENTAGEM EM RELACÃO AO VALOR EM REAL --> {porcentagem_milhas_padrao: .1f}%
    VALOR EM MILHAS ACUMULADAS BARATAS = R${valor_milhas_baratas: .2f}
    PORCENTAGEM EM RELAÇÃO AO VALOR EM REAL --> {porcentagem_milhas_baratas: .1f}%''')
    utils.linhas()
    melhor_escolha(valor_milhas_baratas, valor_milhas_padrao, valor_passagem_reais, origem, destino)


def melhor_escolha(valor_milhas_baratas: float, valor_milhas_padrao: float, valor_passagem_reais: float, origem, destino):
    if valor_milhas_baratas < valor_milhas_padrao and valor_milhas_baratas < valor_passagem_reais:
        print(f'A melhor opção para ir de {origem} para {destino} é por meio de: Milhas Acumuladas Baratas')
    if valor_milhas_padrao < valor_milhas_baratas and valor_milhas_padrao < valor_passagem_reais:
        print(f'A melhor opção para ir de {origem} para {destino} é por meio de: Milhas Padrão')
    if valor_passagem_reais < valor_milhas_padrao and valor_passagem_reais < valor_milhas_baratas:
        print(f'A melhor opção para ir de {origem} para {destino} é por meio de: Valor em R$ no site')

main()