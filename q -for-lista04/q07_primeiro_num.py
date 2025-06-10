# 7. Leia um número e, a seguir, leia uma lista de números até achar um igual ao primeiro número lido.

def main():
    num = int(input('Número: '))

    lista_num = int(input('Lista de números: '))
    for numero in range(1000):
        lista_num = int(input('Lista de números: '))
        if lista_num == num: break

main()