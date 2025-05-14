# [investimento.js] Mariana resolveu investir de parte de seu salário
# (um pedaço(R$) inferior a 30%) de forma fixa mensal; O investimento
# escolhido rende mensalmente a uma taxa de juros de 0,01% até 1,00
# % sobre o saldo do mês. Mariana tem um dado objetivo com este
# investimento. Pergunte a ela qual o objetivo e de quanto ela precisa
# para realizá-lo. Além disso, peça o salário, quanto(%) ela pretende
# investir mensalmente e qual a taxa de juros do investimento
# escolhido. Em seguida mostre em quantos meses ela atingirá o
# objetivo. Se for acima de 12 meses mostre-o em anos e meses. A
# cada mês você deve atualizar o saldo primeiro com o aporte
# (depósito de valor do salário) e depois aplicar os créditos dos juros
# sobre esse novo saldo. Faça isso enquanto o objetivo não for
# alcançado, contando os meses para serem exibidos como se pede.

import utils

def main():
    objetivo = utils.string('Qual o seu objetivo?: ')
    valor_do_objetivo = utils.get_integer_number_min('Quanto você precisa para realizar o objetivo?(R$): ', 0)
    salario = utils.get_decimal_number_min('Qual o valor do seu salário?(R$): ', 0)
    taxa_investimento = utils.get_decimal_number_max('Quanto deseja investir? (%): ', 29)/100
    taxa_juros = utils.get_decimal_in_range('Qual a taxa de juros do investimento escolhido?(%): ', 0.01, 1)/100

    print('=== INVESTIMENTO ===')
    print(f'OBJETIVO: {objetivo}')
    print(f'VALOR DO OBJETIVO R${valor_do_objetivo: .2f}')
    utils.linhas()
    tempo = 0
    saldo = 0
    while saldo < valor_do_objetivo:
        saldo += (salario * taxa_investimento)
        tempo +=1
        novo_saldo = saldo * (1+taxa_juros)
        valor_do_objetivo -= novo_saldo
        print(f'Mês {tempo}')
        utils.linhas()
        print(f'SALDO DO MÊS: R${novo_saldo: .2f}')
        utils.linhas
        print(f'Quanto falta?: R${valor_do_objetivo: .2f}')
        utils.linhas()
    print(f'TEMPO TOTAL PARA ALCANÇAR O OBJETIVO: {tempo_obj(tempo)}')


def tempo_obj (tempo):
    if tempo > 12:
        return f'{tempo//12} anos e {tempo % 12} meses'
    else:
        return f'{tempo} meses'
       # m = c * (1 + i * t)


main()



