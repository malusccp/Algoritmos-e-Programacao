import utils

def main():
        menu_word() 
        choose = int(input('Choose a option: '))
        while choose != 0:
            if choose == size_of_word: 
                tamanhos_palavra()
            elif choose == char_proibido:
                caractere_proibido()
            elif choose == letra_proibida:
                letras_proibidas = input('Digite as letras proibidas: ')
                mostrar_palavra_sem_letras_proibidas(letras_proibidas)
            elif choose == letra_permitida:
                letras_permitidas = input('Digite as letras permitidas: ')
                mostrar_palavra_com_letras_permitidas(letras_permitidas)
            elif choose == letra_obrigatoria:
                letras_obrigatorias = input('Digite as letras obrigatórias: ')
                mostrar_palavra_com_letras_obrigatorias(letras_obrigatorias)
            elif choose == ordem_alfabetica:
                mostrar_palavra_em_ordem_alfabetica()

            input('<Enter to continue>')
            utils.clear_screen
            choose = int(input('Choose a option: '))

        



def tamanhos_palavra():
    tamanho = int(input('Qual é o tamanho desejado? '))
    file = open("br-sem-acentos.txt")
    contador = 0
    contador_palavras = 0
    for linha in file:
        contador += 1
        palavra = linha.strip()
        if len(palavra) >= tamanho:
            print(palavra)
            contador_palavras += 1
    porcentagem = (contador_palavras / contador) * 100
    print(f'A porcentagem de palavras é: {porcentagem:.3f}%')


def caractere_proibido():
    file = open("br-sem-acentos.txt")
    caractere = input('Caractere proibido: ')
    contador = 0
    contador_palavras = 0
    for linha in file:
        contador += 1
        palavra = linha.strip()
        if utils.has_no_x(palavra, caractere):
            contador_palavras += 1
            print(palavra)
    porcentagem = (contador_palavras / contador) * 100
    print(f'A porcentagem de palavras é: {porcentagem:.3f}%')


def mostrar_palavra_sem_letras_proibidas(letras_proibidas):
    file = open("br-sem-acentos.txt")
    contador = 0
    contador_palavras = 0
    for linha in file:
        contador += 1
        palavra = linha.strip()
        if utils.avoids(palavra, letras_proibidas):
            print(palavra)
            contador_palavras += 1
    porcentagem = (contador_palavras / contador) * 100
    print(f'A porcentagem de palavras é: {porcentagem:.3f}%')


def mostrar_palavra_com_letras_permitidas(letras_permitidas):
    file = open("br-sem-acentos.txt")
    contador = 0
    contador_palavras = 0

    for linha in file:
        contador += 1
        palavra = linha.strip()
        if utils.uses_only(palavra, letras_permitidas):
            print(palavra)
            contador_palavras +=1
    porcentagem = (contador_palavras / contador) * 100
    print(f'A porcentagem de palavras é: {porcentagem:.3f}%')

def mostrar_palavra_com_letras_obrigatorias(letras_obrigatorias):
    file = open("br-sem-acentos.txt")
    contador = 0
    contador_palavras = 0

    for linha in file:
        contador += 1
        palavra = linha.strip()
        if utils.uses_all(palavra, letras_obrigatorias):
            print(palavra)
            contador_palavras += 1
    porcentagem = (contador_palavras / contador) * 100
    print(f'A porcentagem de palavras é: {porcentagem:.3f}%')           

def mostrar_palavra_em_ordem_alfabetica():
    file = open("br-sem-acentos.txt")
    contador = 0
    contador_palavras = 0
    for linha in file:
        contador += 1
        palavra = utils.to_lower(linha.strip())
        if utils.is_abecedarian(palavra):
            print(palavra)
            contador += 1


def menu_word():
    interface = '''
>>> Words Play <<< 
1 - Palavras com N+ letras
2 - Palavras sem caractere proibido
3 - Palavras sem letras proibidas
4- Palavra com letras permitidas
5- Palavra com letras obrigatórias
6- Palavras em ordem alfabética


0 - Exit
'''
    print(interface)

# Constantes
size_of_word = 1
char_proibido = 2
letra_proibida = 3
letra_permitida = 4
letra_obrigatoria = 5
ordem_alfabetica = 6
exit = 0

main()