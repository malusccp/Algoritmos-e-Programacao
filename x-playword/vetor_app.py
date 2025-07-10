import utils
import vetor_funcionalidades
import vetor_utils
from teste import exibir_menu 
from rich.prompt import Prompt
from time import sleep

def main():
    lista = []
    while True:
        exibir_menu(lista) 
        
        try:
            opcao = int(Prompt.ask("[bold green]Digite uma opção[/bold green]", default="0"))
        except ValueError:
            print("[red]❌ Opção inválida. Tente um número entre 0 e 15.[/red]")
            sleep(1.5)
            continue

        if opcao == 1:
            utils.clear_screen()
            lista = vetor_funcionalidades.inicializar_vetor()
        elif opcao == 2:
            utils.clear_screen()
            vetor_utils.mostrar_vetor(lista)
        elif opcao == 3:
            utils.clear_screen()
            lista = vetor_utils.resetar_lista(lista)
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
            nome_arquivo = input('Digite o nome do arquivo: ')
            vetor_funcionalidades.salvar_arquivo_com_progresso(lista, nome_arquivo)
        elif opcao == 0:
            utils.clear_screen()
            print("💾 Salvando automaticamente os dados antes de sair...")
            vetor_funcionalidades.salvar_valor_arquivo(lista)
            print("👋 Saindo... Até logo!")
            break

main()
