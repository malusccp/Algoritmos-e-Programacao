import uteis

def main():
    qtd_numero = uteis.get_integer_number_min("Digite quantos números deseja adicionar a lista: ", 1)
    validar_valores(qtd_numero)

   
def validar_valores(qtd_numero: int):
    contador = 1 
    soma = 0 
    while contador <= qtd_numero:
        numero = uteis.get_integer_number_min("Digite um número:  ", 0)
        soma += numero
        contador += 1
    
    media = calcular_media(soma, qtd_numero)

    uteis.linhas()
    print(f'Soma dos valores: {soma}\nMédia dos valores: {media: .2f}')
    uteis.linhas()


def calcular_media(soma: int, qtd_numero: int):
    return soma/qtd_numero


main()