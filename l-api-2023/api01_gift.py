# 01. gift.py Uma loja presenteia suas clientes com descontos
# (cashback) progressivos de acordo com suas compras. Desta
# forma, para compras mensais de até R$ 250 reais, é feita a
# conversão (geração) de cashback de 5%; Para compras acima de
# R$ 250 até R$ 500, 7% de cashback; De R$ 500 até R$ 750, 8%
# de cashback; E para compras acima de R$ 750 é aplicado
# primeiramente as regras anteriores até R$ 750 do valor em cada
# faixa, e 25% sobre o valor acima de R$ 750. Operações de
# cashbacks progressivos têm o objetivo de incentivar as suas
# clientes a comprarem mais e ao mesmo tempo serem
# compensadas por isso.
# a. Implemente um software para auxiliar no cálculo do
# cashback mensal de suas clientes (devem ser lidos N
# compras Nome Cliente e Valor Compras).
# b. Informe quanto foi o faturamento total (soma das vendas);
# Quanto foi distribuído em cashback; Qual o valor em reais e
# percentual investido em cashback pela loja; Maior, menor e
# valor médio pago em cashback.
import utils

def main():
    nome_cliente = utils.string('Digite seu nome: ')
    numero_compras = utils.get_integer_number('Digite o número de compras realizadas pela cliente: ')
    
    contador = 0
    total_compras = 0
    cashback_total = 0
    cashback_maior = None
    cashback_menor = None
    while contador < numero_compras:
       valor_compras = utils.get_decimal_number_min('Digite o valor da compra: ', 0)
       total_compras += valor_compras
       cashback_total += cashback(valor_compras)
       contador += 1
       if cashback_maior == None or cashback(valor_compras) > cashback_maior:
          cashback_maior = cashback(valor_compras)
       if cashback_menor == None or cashback(valor_compras) < cashback_menor:
          cashback_menor = cashback(valor_compras)
    utils.limpar_tela()
    utils.linhas()
    faturamento = f''' === CÁLCULO DE CASHBACK MENSAL ===
    > CLIENTE: {nome_cliente}
    > NÚMERO DE COMPRAS: {numero_compras} compras
    > FATURAMENTO TOTAL: R${total_compras: .2f}
    > QUANTO FOI DISTRIBUÍDO EM CASHBACK: R${cashback_total: .2f}
    > PERCENTUAL DE CASHBACK INVESTIDO PELA LOJA: {(cashback_total/total_compras) * 100: .1f}%
    > MAIOR VALOR DE CASHBACK: R${cashback_maior: .2f}
    > MENOR VALOR DE CASHBACK: R${cashback_menor: .2f}
    > VALOR MÉDIO DE CASHBACK: R${media(cashback_total, numero_compras): .2f}'''
    print(faturamento)
    utils.linhas()


def cashback(valor_compras: float):
   if valor_compras <= 250:
    return valor_compras * 0.05
   elif valor_compras <= 500: 
      return valor_compras * 0.07
   elif valor_compras <= 750:
      return valor_compras * 0.08
   else:
      return (0.05 * 250) + (0.07 * 500) + (0.08 * 750) + ((valor_compras - 750) * 0.25)


def media(soma: float, n: int):
   return soma/n

main()