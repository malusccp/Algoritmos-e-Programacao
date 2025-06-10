import utils


def main():
    qtd_imoveis = utils.get_integer_number_min("Quantidade de imóveis: ", 0)

    
    maior_anual = 0
    retorno_total = 0
    retorno_anual = 'Retorno Anual de cada imóvel:\n '
    maior_total = 0
    for imovel in range(1, qtd_imoveis+1):
        print(f'Imóvel {imovel}')
        valor_compra = utils.get_decimal_number_min("Valor de compra do imóvel: ", 0)
        valor_aluguel = utils.get_decimal_number_min("Valor de aluguel mensal: ", 0)
        tempo_aluguel = utils.get_integer_number_min("Tempo de aluguel do imóvel: ", 0)

        aluguel_anual = valor_aluguel * 12
        aluguel_total = (valor_aluguel * 12 * (tempo_aluguel)) - valor_compra
        retorno_total += aluguel_total
        retorno_anual += f'Imóvel {imovel}:\nR${aluguel_anual:.2f}\n'

        if aluguel_anual > maior_anual:
            maior_anual = aluguel_anual
        if aluguel_total > maior_total:
            maior_total = aluguel_total
    
    print('=== Análise de Retorno de Investimento em Aluguéis ===')
    print(retorno_anual)
    print(f'''
Retorno total: R${retorno_total:.2f}
Maior retorno anual: R${maior_anual:.2f}
Maior retorno total: R${maior_total:.2f}

''')

main()