from minhas_funcoes import obter_numero_real
from minhas_funcoes import obter_resposta

def main():
    preço = obter_numero_real('Digite o preço do produto desejado: ')
    saldo_cliente = obter_numero_real('Digite o valor que possui: ')
    desconto = obter_resposta('Possui cupom de desconto?: ')
    validar_compra(preço, saldo_cliente, desconto)



def validar_compra(preço, saldo_cliente, desconto):
    if preço <= saldo_cliente and (desconto == 'sim' or desconto == 'Sim'):
        return print('Compra aprovada com desconto')
    if preço > saldo_cliente and (desconto == 'sim' or desconto == 'Sim'):
        if (preço * 0.8) <= saldo_cliente:
            print('Compra aprovada com desconto')
        elif (preço * 0.8) > saldo_cliente:
            print('Compra negada: Saldo insuficiente')
    if preço <= saldo_cliente and (desconto == 'não' or desconto == 'Não'):
        print('Compra aprovada sem desconto')
    if preço > saldo_cliente and (desconto == 'não' or desconto == 'Não'):
        print('Compra negada: Saldo insuficiente')

main()