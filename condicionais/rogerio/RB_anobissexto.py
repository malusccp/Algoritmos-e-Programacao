def ano_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

 
def escolher_ano():
    try:
        ano = int(input('Digite o ano desejado: '))
        return ano
    except ValueError:
        print('O termo digitado não é um número inteiro')
        return escolher_ano()
    
def main():
    ano = escolher_ano()
    if ano_bissexto(ano):
        print(f'O ano {ano} é bissexto!!!')
    else:
        print(f'O ano {ano} NÃO é bissexto!!!!')

main()