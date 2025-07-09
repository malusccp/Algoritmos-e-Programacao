import utils
import vetor_utils
import random

def inicializar_vetor():
    interface = ''' >>> Inicializar Vetor Numérico <<<
1 - Vetor com dados automáticos
2 - Vetor digitado manualmente
3 - Vetor a partir de um arquivo
'''
    lista = []
    opcao = utils.get_int_in_range(interface, 1, 3)
    if opcao == 1:
        return vetor_dados_automaticos()
    elif opcao == 2:
        return vetor_manual()
    elif opcao == 3:
        return vetor_arquivo()


def vetor_arquivo():
    lista_arquivo = []

    arquivo = input("Digite o nome do arquivo (ex: valores.txt): ")

    for valor in open(arquivo):
        valores = valor.strip()
        lista_arquivo.append(valores)

    return lista_arquivo


def vetor_dados_automaticos():
    tamanho = vetor_utils.pedir_tamanho('Qual o tamanho da lista?: ')
    valor_min = vetor_utils.pedir_valor_min('Qual o valor mínimo da lista?: ')
    valor_max = vetor_utils.pedir_valor_max('Qual o valor máximo da lista?: ')

    lista = [random.randint(valor_min, valor_max) for _ in range(tamanho)]

    return lista


def somatorio_lista(lista):
    somatorio = 0 
    for elemento in lista:
        somatorio += elemento

    return somatorio


def valores_positivos(lista):
    quantidade = 0
    for elementos in lista:
        if elementos > 0:
            print(elementos)
            quantidade += 1

    print(f'Quantidade: {quantidade} valores positivos')


def valores_negativos(lista):
    quantidade = 0
    for elementos in lista:
        if elementos < 0:
            print(elementos)
            quantidade += 1

    print(f'Quantidade: {quantidade} valores negativos')


def media_lista(lista, somatorio):
    media = somatorio / len(lista)

    print(f'Média = {media:.1f}')


def vetor_manual():
    lista = []
    tamanho = vetor_utils.pedir_tamanho('Qual o tamanho da lista?: ')
    valor_min = vetor_utils.pedir_valor_min('Qual o valor mínimo da lista?: ')
    valor_max = vetor_utils.pedir_valor_max('Qual o valor máximo da lista?: ')

    for elementos in range(1, tamanho+1):
        valor = utils.get_int_in_range(f'Item N° {elementos}: ',valor_min, valor_max)
        lista.append(valor)

    return lista

def atualizar_valores(lista):
    interface = ''' Inicializar Vetor Numérico
1. Multiplicar por um valor
2. Elevar a um valor 
3. Reduzir a uma fração 
4. Substituir valores negativos por um número aleatórios da uma faixa(min, max)
5. Ordenar valores (reverse?)
6. Embaralhar valores
'''
    opcao = utils.get_int_in_range(interface, 1, 6)
    if opcao == 1:
        valor = utils.get_integer_number('Digite o valor a ser multiplicado: ')
        return mapear_2(lista, multiplicar, valor)
    elif opcao == 2:
        valor = utils.get_integer_number('Digite o valor a ser elevado: ')
        return mapear_2(lista, exponenciacao, valor)
    elif opcao == 3:
        numerador, denominador = map(int, input('Digite a fração:').split('/'))
        fracao = numerador/denominador
        return reduzir_fracao(fracao, lista)
    elif opcao == 4:
        return substituir_valores(lista)
    elif opcao == 5:
        ordem = utils.get_int_in_range('Deseja que a ordenação seja feita na ordem crescente (0) ou descrescente? (1): ', 0, 1)
        return ordenar_valores(lista, ordem)
    elif opcao == 6:
        return embaralhar_valores(lista)

def embaralhar_valores(lista):
    random.shuffle(lista)
    return lista


def ordenar_valores(lista, ordem):
    if ordem == 0:
        lista.sort()
    elif ordem == 1:
        lista.sort(reverse=True)
    
    return lista

def substituir_valores(lista):
    for item in lista:
        if item < 0:
            min_value = utils.get_integer_positive('Digite o valor mínimo de substituição: ')
            max_value = utils.get_integer_positive('Digite o valor máximo de substituição: ')
            indice = lista.index(item)
            lista[indice] = random.randint(min_value, max_value)

    return lista
        

def reduzir_fracao(fracao, lista):
  return  mapear_2(lista, multiplicar, fracao)
    

def multiplicar(a, b):
    return a * b

def exponenciacao(a, valor):
    return a ** valor

def mapear_2(lista, funcao_transformadora, valor):
    nova_lista = []

    for elemento in lista:
        elemento_transformado = funcao_transformadora(elemento, valor)
        nova_lista.append(elemento_transformado)

    return nova_lista


def modificar_vetor(lista, indice, novo_valor):
    lista[indice] = novo_valor


def salvar_valor_arquivo(lista):
    nome_arquivo = input('Digite o nome do arquivo: ')
    with open(nome_arquivo, "w") as arquivo:
        for valor in lista:
            arquivo.write(str(valor) + "\n")
    print('Dados salvos !')