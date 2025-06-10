import utils
# 7. Alimentação: Inventário de Estoque de Alimentos com Validade
# ● Contexto/Problema: Um pequeno restaurante precisa gerenciar seu estoque de alimentos, registrando
# a data de compra e a data de validade de cada item. O programa deve permitir que o usuário insira
# vários itens no estoque. Para cada item, o usuário deve informar o nome do alimento, a quantidade, a
# data de compra e a data de validade (ambas no formato DD/MM/AAAA). O programa deve identificar e
# listar para cada alimento quantos dias ainda de validade próxima ou já está vencido. (Considerar 12
# meses de 30 dias exatos cada ano)
# ● Entrada: O usuário deve informar a quantidade de itens a serem cadastrados no estoque. Para cada
# item, o usuário deve informar o nome, a quantidade, a data de compra e a data de validade.
# ● Saída Esperada: Uma lista de alimentos que estão com a validade próxima ou vencidos, informando o
# nome do alimento e a data de validade.

def main():
    qtd_itens = utils.get_integer_number_min('Quantidade de itens: ', 0)
    lista = '=== Inventário de Estoque de Alimentos com Validade ==='

    for item in range(1, qtd_itens+1):
        nome = utils.get_text('Alimento: ')
        qtd_alimento = utils.get_integer_number_min('Quantidade do alimento: ', 0)
        dia_compra, mes_compra, ano_compra = map(int, input('Digite a data de compra: ').split('/'))
        dia_validade, mes_validade, ano_validade = map(str, input('Digite a data de validade: ').split('/'))

        total_compra = (ano_compra * 360) + (mes_compra * 30) + dia_compra
        total_validade = (int(ano_validade) * 360) + (int(mes_validade) * 30) + int(dia_validade)

        validade = verificar_validade(total_compra, total_validade)

        lista += f'\n{item}- {nome}:\n{dia_validade}/{(mes_validade)}/{ano_validade}\nSituação do alimento: {validade}'
    
    utils.clear_screen()
    print(lista)

def verificar_validade(total_compra, total_validade):
    if total_validade < total_compra:
        return 'Alimento vencido'
    else:
        dias_restantes = total_validade - total_compra
        return f'Alimento dentro do prazo de validade (Vence em {dias_restantes} dias)'
    
main()