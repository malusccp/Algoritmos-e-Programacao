# 9. Imobiliário: Simulação de Pagamento de Financiamento Habitacional
# ● Contexto/Problema: Um comprador em potencial deseja simular o pagamento de um financiamento
# imobiliário. O programa deve solicitar o valor do imóvel, o valor da entrada, a taxa de juros mensal (fixa)
# e o número de parcelas. O programa deve calcular e exibir o valor de cada parcela (considerando juros
# compostos sobre o saldo devedor) e o saldo devedor restante após o pagamento de cada parcela.
# ● Entrada: O usuário deve informar o valor do imóvel, o valor da entrada, a taxa de juros mensal (em
# porcentagem) e o número total de parcelas.
# ● Saída Esperada: Para cada parcela, o número da parcela, o valor da parcela, o valor dos juros daquela
# parcela e o saldo devedor após o pagamento.
import utils
def main():
    valor_imovel = utils.get_decimal_number_min('Valor do imóvel: ', 0)
    valor_entrada = utils.get_decimal_number_min('Valor da entrada: ', 0)
    taxa_juros = utils.get_integer_number_min('Taxa de juros: ', 0)/100
    qtd_parcelas = utils.get_integer_number_min('Número de parcelas: ', 0)

    saldo_devedor = valor_imovel - valor_entrada 
    juros_parcela = taxa_juros * saldo_devedor
    for parcela in range(1, qtd_parcelas+1):
        amortizacao = saldo_devedor / (qtd_parcelas - parcela+1)
        print(f'Parcela {parcela}')
        print(f'Valor da parcela: R${(juros_parcela + amortizacao):.2f}')
        saldo_devedor -= amortizacao
        print(f'Juros da parcela: R${saldo_devedor * taxa_juros:.2f}')
        print(f'Saldo devedor após o pagamento: R${saldo_devedor:.2f}')



main()