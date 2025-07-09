# Crie um arquivo vetor_utils com funções específicas para manipulação de vetores, para operações como:
# adicionar, remover, map, filter, mostrar vetor
import utils
def mapear(lista, funcao_transformadora):
    nova_lista = []

    for elemento in lista:
        elemento_transformado = funcao_transformadora(elemento)
        nova_lista.append(elemento_transformado)

    return nova_lista


def pedir_tamanho(label):
    tamanho = utils.get_integer_number(label)
    return tamanho

def pedir_valor_min(label):
    valor_min = utils.get_integer_number(label)
    return valor_min

def pedir_valor_max(label):
    valor_max = utils.get_integer_number(label)
    return valor_max

def filtrar(lista, funcao_criterio):
    nova_lista = []

    for elemento in lista:
        if funcao_criterio(elemento):
            nova_lista.append(elemento)
    return nova_lista


def mostrar_vetor(lista):
    for elemento in lista:
        print(elemento)


def adicionar_elemento(lista, elemento):
    lista.append(elemento)
    return lista

def remover_por_valor(lista, elemento):
    for item in lista:
        if item == elemento:
            lista.pop(lista.index(item))
    return lista

def remover_por_indice(lista, indice):
    lista.pop(indice)
    print('Valor removido com sucesso!')
    return lista

def resetar_lista(lista):
    while len(lista) > 0:
        lista.pop()
    print('Deletado com sucesso!')

def tamanho_lista(lista):
    print(f'O tamanho da lista é {len(lista)}')


def maior_e_menor(lista):
    maior = None
    menor = None
    for valor in lista:
        if maior == None or maior < valor:
            maior = valor

        if menor == None or menor > valor:
            menor = valor

    print(f'Maior valor da lista: {maior} - index = {lista.index(maior)}')
    print(f'Menor valor da lista: {menor} - index = {lista.index(menor)}')


def reduzir(lista, funcao_redutora, inicial):
    acumulado = inicial

    for item in lista:
        acumulado = funcao_redutora(acumulado, item)

    return acumulado
