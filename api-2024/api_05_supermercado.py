
import utils

def main():
    somatorio = 0
    contador = 1
    lista = '''=== LISTA DE PRODUTOS ===
'''
    while True:
        menu_mercado()
        opcao = utils.get_intnumber_range('Digite sua opção: ', 0,3)

        if opcao == add_number:
            item = utils.string('Digite o nome do produto: ')
            especificacao = utils.string('Digite a especificação. Ex: (5kg): ')
            preço = utils.string('Digite o preço do produto: ')
            somatorio += float(preço)
            lista += f'\n{contador}- {item} {especificacao}     R${preço}\n'
            utils.clear_screen()
        elif opcao == payments:
            opcoes_de_pagamento(somatorio)
        elif opcao == list:
            utils.clear_screen()
            imprimir_lista(lista, somatorio)
        elif opcao == exit:
            utils.clear_screen()
            break
        else:
            print('Opção inválida!')
            enter_to_continue()

        contador += 1


def opcoes_de_pagamento(somatorio):
    parcelar = ''' === OPÇÕES DE PAGAMENTO === 
          1 - À vista
          Cartão de crédito:
          2 - Parcelar em até 3x sem juros - A partir de R$ 30,00 em compras
          3 - Parcelar em até 5x sem juros - A partir de R$ 100,00 em compras
          4- Parcelar em até 6x - Qualquer valor, mas com juros de 5% a.m

'''
    print(parcelar)
    print(f'Valor total: {somatorio: .2f}')
    utils.linhas()
    forma_de_pagamento = utils.get_intnumber_range('Escolha a opção de pagamento desejada: ', 1, 4)
    if forma_de_pagamento == 1:
        print(f'O valor a ser pago à vista é igual a R${somatorio: .2f}')
    else:
        qtd_parcelas = utils.get_intnumber_range('Deseja parcelar em quantas vezes?: ', 1, 6)
        if forma_de_pagamento == 2:
            if 30 < somatorio <= 100:
                if qtd_parcelas > 3:
                    input('Para esse valor, só é possível parcelar em até 3x\nAperte <Enter> para tentar novamente...')
                    utils.clear_screen()
                    return opcoes_de_pagamento(somatorio)
                else:
                    parcelas = somatorio/qtd_parcelas
                    print(f'Valor das parcelas: {parcelas: .2f}')
            else:
                input('Essa forma de pagamento só abrange valores entre R$ 30,00 e R$ 100,00 \nAperte <Enter> para tentar novamente...')
                utils.clear_screen()
                return opcoes_de_pagamento(somatorio)
        elif forma_de_pagamento == 3:
            if somatorio > 100:
                parcelas = somatorio/qtd_parcelas
                print(f'Valor das parcelas: {parcelas: .2f}')
            else:
                input('Essa forma de pagamento só abrange valores maiores que R$ 100,00 \nAperte <Enter> para tentar novamente...')
                utils.clear_screen()
                return opcoes_de_pagamento(somatorio)
        elif forma_de_pagamento == 4:
            parcelas = 0
            contador = 1
            contar_parcelas = qtd_parcelas

            somatorio = somatorio/qtd_parcelas

            while contar_parcelas >= 1:
                parcelas = ((somatorio*0.05) + somatorio)
                somatorio = parcelas
                print(f'{contador}° Parcela: R$ {parcelas: .2f}')
                contar_parcelas -= 1
                contador += 1
        utils.linhas()
        

def enter_to_continue():
    input('<Enter> to continue...')
    utils.clear_screen()


def imprimir_lista(lista, somatorio):
    print(lista)
    utils.linhas()
    print(f'Valor total:     R${str(somatorio)}')


def menu_mercado():
    menu =''' === PESQUISA DE PREÇOS ===
    
    > 1 - Adicionar novo item
    > 2 - Imprimir lista
    > 3 - Opções de pagamento
    > 0 - Sair
''' 
    utils.linhas()
    print(menu)
    utils.linhas()
# Constantes
add_number = 1
exit = 0
payments = 3
list = 2

enter_to_continue()
utils.clear_screen()

main()