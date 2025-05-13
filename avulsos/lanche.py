from minhas_funcoes import obter_numero_inteiro

def main():
    codigo_do_lanche = obter_numero_inteiro('Digite o código do lanche desejado: ')
    quantidade_lanche = obter_numero_inteiro('Digite a quantidade desejada: ')
    preços_lanche(codigo_do_lanche, quantidade_lanche)



def preços_lanche(codigo_do_lanche, quantidade_lanche):
    if codigo_do_lanche == 1:
        return print(f'O valor da conta será igual a --> R${(4 * quantidade_lanche): .2f}')
    if codigo_do_lanche == 2:
        return print(f'O valor da conta será igual a --> R${(4.5 * quantidade_lanche): .2f}')
    if codigo_do_lanche == 3:
        return print(f'O valor da conta será igual a --> R${(5 * quantidade_lanche): .2f}')
    if codigo_do_lanche == 4:
        return print(f'O valor da conta será igual a --> R${(2 * quantidade_lanche): .2f}')
    if codigo_do_lanche == 5:
        return print(f'O valor da conta será igual a --> R${(1.50 * quantidade_lanche): .2f}')

main()