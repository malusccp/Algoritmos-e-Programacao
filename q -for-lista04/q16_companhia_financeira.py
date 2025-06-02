# 16. Uma companhia financeira debita um juro de 0.85% diário sobre o saldo não pago de um empréstimo.
# Com um empréstimo de R$ 3.000,00, um pagamento de R$ 200,00 é feito todo dia útil. Escreva um
# algoritmo que calcule quantos dias úteis são necessários para se concluir o pagamento do empréstimo.
import utils

def main():
    emprestimo = utils.get_decimal_number_min('Valor do empréstimo: ', 0)
    pagamento_diario = utils.get_decimal_number_min('Valor do pagamento diário: ', 0)

    dias = 0
    juros = emprestimo * ((1+(0.85/100))**1) - emprestimo
    for i in range(int(emprestimo), 0, int(-pagamento_diario)):
        emprestimo += juros
        dias += 1 
    print(f'{dias - (dias//5) * 2} dias úteis para a conclusão do pagamento ')

main()

    
