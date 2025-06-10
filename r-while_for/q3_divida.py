# 3. Financeiro: Projeção de Dívida com Pagamentos Variáveis
# ● Contexto/Problema: Um indivíduo possui uma dívida com juros compostos mensais e deseja projetar
# como ela se comportará ao longo do tempo, considerando pagamentos variáveis. O programa deve
# permitir que o usuário insira o valor inicial da dívida, a taxa de juros mensal e o número de meses para
# projeção. Para cada mês, o usuário deve informar o valor do pagamento realizado. O programa deve
# mostrar o saldo da dívida após cada pagamento e indicar em qual mês a dívida foi quitada (se for o
# caso), ou o saldo remanescente.
# ● Entrada: O usuário deve informar o valor inicial da dívida, a taxa de juros mensal (em porcentagem) e
# a quantidade de meses para a projeção. Para cada mês, o usuário deve informar o valor do pagamento
# realizado.
# ● Saída Esperada: O saldo da dívida ao final de cada mês. Uma mensagem indicando se a dívida foi
# quitada, em qual mês isso ocorreu, ou o saldo remanescente ao final da projeção.
import utils
def main():
    valor_inicial = utils.get_decimal_number_min('Valor inicial dívida (R$): ', 0)
    taxa_juros = utils.get_decimal_number_min('Taxa de juros mensal (%): ', 0)/100
    meses = utils.get_integer_number_min('Número de meses: ', 0)
    
    divida = valor_inicial
    mes_quitada = None
    for mes in range(1, meses+1):
        divida *= ((1 + taxa_juros)**mes)
        pagamento = utils.get_decimal_number_min('Informe quanto será pago da dívida (R$): ', 0)
        divida -= pagamento
        if divida <= 0:
            mes_quitada = mes
            break
        else:
            utils.linhas()
            print(f'Pagamento do mês {mes}')
            print(f'R$ {divida+pagamento:.2f} - {pagamento:.2f}')
            print(f'Saldo a pagar: R${divida:.2f}') 
            utils.linhas()


    if mes_quitada == None:
        print(f'A dívida não foi quitada! Faltou R$ {divida:.2f}')
    else:
        print(f'A dívida foi quitada no mês {mes_quitada}')
    utils.linhas()
main()
