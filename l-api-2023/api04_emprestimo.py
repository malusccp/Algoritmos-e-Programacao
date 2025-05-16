
# Porém a taxa de juros aplicada é calculada de acordo com o prazo
# de parcelamento (vide tabela) e à SELIC, atualmente em 13,75%
# (abril/2023). O usuário só pode parcelar o empréstimo em até 24x
# (min. 2 parcelas). Valor mínimo de empréstimo é de um salário
# mínimo. Valor máximo de parcela é 40% da Renda Mensal do
# Cliente.
# Antes de calcular os juros é necessário calcular o IOF (Imposto sobre
# Operações Financeiras) pago ao Governo Federal antes de aplicar
# os Juros. O IOF é calculado da seguinte forma: 0,38% sobre valor
# total (independente do prazo) + 0,0082% por cada dia do prazo do
# empréstimo. Considere todos os meses com 30 dias. Os juros são
# aplicados sobre o valor a ser recebido pelo Cliente + IOF

# Prazo         Taxa
# Até 6x        50% da SELIC
# de 7x a 12x   75% da SELIC
# de 12x a 18x  100% da SELIC
# Acima de 18x  130% da SELIC

# ● Peça ao usuário Renda Mensal, Valor Empréstimo e Prazo
# desejados, valide os dados a serem recebidos.
# ● Calcule e escreva na tela:
# a. Valor Pedido
# b. Valor do IOF
# c. Valor dos Juros a pagar
# d. Valor Total a pagar (ex.: "R$ 5148,00")
# e. Valor da Parcela Mensal (ex.: "16x de R$ 321,75")
# f. Comprometimento da Renda Mensal (%)
# g. Se Empréstimo APROVADO ou NEGADO (se a
# renda mensal suporta a parcela)

import utils

def main():
    renda_mensal = utils.get_decimal_number_min('Qual sua renda mensal(R$)?: ', 0)
    valor_emprestimo = utils.get_decimal_number_min('Qual o valor do empréstimo(R$)?: ', 1.518)
    prazo = utils.get_int_in_range('Qual o prazo desejado para o empréstimo?: ', 2, 24)

    iof = (valor_emprestimo * (0.38/100)) + ((0.0082/100) * (30 * prazo) * valor_emprestimo)


    juros = (valor_emprestimo + iof) * ((1 + selic(prazo))**prazo) - valor_emprestimo
    valor_total_pagar = valor_emprestimo + juros 
    parcela = valor_total_pagar/prazo
    comprometimento_da_renda = (100 * parcela) / renda_mensal

    interface = f'''=== CALCULADORA DE EMPRÉSTIMOS ===
> VALOR PEDIDO: R${valor_emprestimo:.2f}
> VALOR DO IOF: R${iof:.2f}
> VALOR DOS JUROS A PAGAR: R${juros:.2f}
> VALOR TOTAL A PAGAR: R${valor_total_pagar:.2f}
> VALOR DA PARCELA MENSAL: {prazo}x de {parcela:.2f}
> COMPROMETIMENTO DA RENDA MENSAL: {comprometimento_da_renda:.2f}%
> STATUS DO EMPRÉSTIMO: {avaliar_emprestimo(renda_mensal, parcela)}'''
    print(interface)


def avaliar_emprestimo(renda_mensal: float, parcela: float):
    if renda_mensal * 0.40 < parcela:
        return 'EMPRÉSTIMO NEGADO: A sua renda mensal não suporta a parcela'
    else:
        return 'EMPRÉSTIMO APROVADO'
    

def selic(prazo: int):
    if prazo <= 6:
       return (13.75/100) * 0.5
    elif prazo <= 12:
       return (13.75/100) * 0.75
    elif prazo <= 18:
        return (13.75/100)
    else:
        return (13.75/100) * 1.30
    
main()

