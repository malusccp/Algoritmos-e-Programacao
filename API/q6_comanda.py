import os
from q1_number_utils import get_int_in_range
from q1_number_utils import get_integer_number_min

# TEMPO
# 25/05/2025
# INÍCIO: 14:49 FIM: 15:53

def main():
    somatorio = 0
    qtd_cerveja = 0
    comanda = ''' === COMANDA === 
'''
    contador = 1
    while True:
        menu_comanda()
        opcao = get_int_in_range('Escolha a opção desejada: ', 1, 3)
        if opcao == adicionar_produto:
            limpar_tela()
            qtd_item, item = map(str, input('Digite sua escolha: ').split())
            qtd_item = int(qtd_item)
            if item.upper() == 'C':
                somatorio += qtd_item * 9
                qtd_cerveja += qtd_item
                comanda += f'\n{contador}- {qtd_item}x Cerveja\n'
            elif item.upper() == 'A':
                somatorio += qtd_item * 5
                comanda += f'\n{contador}- {qtd_item}x Água\n'
            elif item.upper() == 'T':
                somatorio += qtd_item * 39
                comanda += f'\n{contador}- {qtd_item}x Tira-gosto\n'
            else:
                print('Opção inválida!')
                enter_to_continue()
        elif opcao == imprimir_conta:
            limpar_tela()
            total = calcular_total(somatorio, qtd_cerveja)
            qtd_pessoas = get_integer_number_min('Digite a quantidade de pessoas: ', 0)
            valor_pessoa = total/qtd_pessoas
            taxa = total - somatorio
            print(comanda)
            linhas()
            print(f'Valor da conta R${somatorio:.2f}')
            print(f'Taxa de serviço (10%): R${taxa:.2f}')
            print(f'O valor total: R${total:.2f}')
            print(f'Valor por pessoa: R${valor_pessoa:.2f}')
            linhas()
        elif opcao == confirmar_pagamento:
            pagar = get_int_in_range('Digite "1" para pagar: ', 1, 1)
            if pagar == 1:
                somatorio = 0
        contador += 1

        
def calcular_total(somatorio: float, qtd_cerveja: int) -> float:
    if (somatorio > 200) or (qtd_cerveja > 10):
        return somatorio
    else:
        return somatorio * 1.10


def menu_comanda():
    comanda = f'''=== BAR DA LORA E DO RÔ S2 ===
> 1 = Inserir produtos
> 2 = Imprimir conta
> 3 = Confirmar pagamento
> 4 = Sair

'''
    print(comanda)
# Constantes
adicionar_produto = 1
imprimir_conta = 2
confirmar_pagamento = 3
sair = 4

def limpar_tela():
    os.system('cls')

def enter_to_continue():
    input('<Enter> to continue...')
    limpar_tela()

def linhas():
    print('-' * 30)

enter_to_continue()
limpar_tela()

main()