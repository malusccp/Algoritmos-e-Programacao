# 8. Financeiro: Balanço de Fluxo de Caixa Mensal Detalhado
# ● Contexto/Problema: Para um controle financeiro mais rigoroso, é necessário registrar todas as
# receitas e despesas de um mês. O programa deve permitir que o usuário insira múltiplas receitas e
# múltiplas despesas. Para cada transação (seja receita ou despesa), o usuário deve informar uma
# descrição e o valor. Ao final, o programa deve apresentar o total de receitas, o total de despesas, o
# saldo final do mês e categorizar a despesa de maior valor e a receita de maior valor.
# ● Entrada: O usuário deve informar a quantidade de receitas a serem cadastradas e, para cada uma, a
# descrição e o valor. Em seguida, o usuário deve informar a quantidade de despesas a serem
# cadastradas e, para cada uma, a descrição e o valor.
# ● Saída Esperada: O total de receitas, o total de despesas, o saldo final do mês. A descrição e o valor da
# maior receita e da maior despesa.
import utils
def main():

    total_receitas = 0
    maior_receita = 0
    maior_receita_desc = 0
    total_despesas = 0
    maior_despesa = 0 
    maior_despesa_desc = 0

    qtd_receitas = utils.get_integer_number_min('Quantidade de receitas: ', 0)
    for receita in range(1, qtd_receitas+1):
        print(f'Receita {receita}')
        descricao = utils.get_text('Descrição da receita: ')
        valor = utils.get_decimal_number_min('Valor da receita (R$): ', 0)

        total_receitas += valor

        if maior_receita < valor:
            maior_receita = valor
            maior_receita_desc = descricao


    qtd_despesas = utils.get_integer_number_min('Quantidade de despesas: ', 0)
    for despesa in range(1, qtd_despesas+1):
        print(f'Despesa {despesa}')
        descricao = utils.get_text('Descrição da despesa: ')
        valor = utils.get_decimal_number_min('Valor da despesa (R$): ', 0)

        total_despesas += valor

        if maior_despesa < valor:
            maior_despesa = valor
            maior_despesa_desc = descricao
    
    saldo_final = total_receitas - total_despesas

    interface = f''' === Balanço de Fluxo de Caixa Mensal Detalhado ===
Total de receitas: R${total_receitas:.2f}
Total de despesas: R${total_despesas:.2f}
Saldo final do mês: R${saldo_final:.2f}
Maior receita: R${maior_receita:.2f} - {maior_receita_desc}
Maior receita: R${maior_despesa:.2f} - {maior_despesa_desc}
'''
    print(interface)
main()
