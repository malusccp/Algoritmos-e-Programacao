import utils
import vetor_funcionalidades
import vetor_utils

def main():
    lista = []
    while True:

        menu = ''' >>> PLAY NUMBERS <<< 
    1 - Inicializar Vetor Numérico
    2 - Mostrar todos os valores
    3 - Resetar Vetor
    4 - Ver quantidade de itens no vetor
    5 - Ver Menor e Maior valores e suas posições
    6 - Somatório dos Valores
    7 - Média dos Valores
    8 - Mostrar Valores Positivos e Quantidade
    9 - Mostrar Valores Negativos e Suas Quantidades
    10 - Atualizar todos os valores 
    11 - Adicionar Novos Valores
    12 - Remover Itens por Valor exato
    13 - Remover por Posição
    14 - Editar valor específico por Posição
    15 - Salvar valores em arquivo 
    0 - Sair
    '''
        opcao = utils.get_int_in_range(menu, 0, 15)

        if opcao == 1:
            utils.clear_screen()
            lista = vetor_funcionalidades.inicializar_vetor()
        elif opcao == 2:
            utils.clear_screen
            vetor_utils.mostrar_vetor(lista)
        elif opcao == 3:
            utils.clear_screen()
            vetor_utils.resetar_lista(lista)
        elif opcao == 4:
            utils.clear_screen()
            vetor_utils.tamanho_lista(lista)
        elif opcao == 5:
            utils.clear_screen()
            vetor_utils.maior_e_menor(lista)
        elif opcao == 6:
            utils.clear_screen()
            somatorio = vetor_funcionalidades.somatorio_lista(lista)
            print(f'Somatório = {somatorio}')
        elif opcao == 7:
            utils.clear_screen()
            vetor_funcionalidades.media_lista(lista, somatorio)
        elif opcao == 8:
            utils.clear_screen()
            vetor_funcionalidades.valores_positivos(lista)
        elif opcao == 9:
            utils.clear_screen()
            vetor_funcionalidades.valores_negativos(lista)
        elif opcao == 10:
            utils.clear_screen()
            lista = vetor_funcionalidades.atualizar_valores(lista)
        elif opcao == 11:
            utils.clear_screen()
            elemento = utils.get_integer_number('Qual valor deseja adicionar?: ')
            vetor_utils.adicionar_elemento(lista, elemento)
        elif opcao == 12:
            utils.clear_screen()
            elemento = utils.get_integer_number('Qual o valor que deseja remover?: ')
            vetor_utils.remover_por_valor(lista, elemento)
        elif opcao == 13:
            utils.clear_screen()
            indice = utils.get_integer_number('Qual o índice do valor que deseja remover?: ')
            vetor_utils.remover_por_indice(lista, indice)
        elif opcao == 14:
            utils.clear_screen()
            indice = utils.get_integer_number('Qual o índice do valor que deseja modificar?: ')
            novo_valor = utils.get_integer_number('Por qual valor deseja modificar?: ')
            vetor_funcionalidades.modificar_vetor(lista, indice, novo_valor)
        elif opcao == 15:
            utils.clear_screen()
            vetor_funcionalidades.salvar_valor_arquivo(lista)
        elif opcao == 0:
            utils.clear_screen()
            print("Salvando automaticamente os dados antes de sair...")
            vetor_funcionalidades.salvar_valor_arquivo(lista)
            break
   
main()