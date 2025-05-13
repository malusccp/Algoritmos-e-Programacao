import utils

def main():
    nota1 = utils.get_decimal_number_min('Nota 1: ', 0)
    nota2 = utils.get_decimal_number_min('Nota 2: ', 0)

    media = calcular_media(nota1, nota2)
    interface = f''' ==== CALCULO APROVAÇÃO
    > NOTA 1: {nota1}
    > NOTA 2: {nota2}
    > MÉDIA: {media: .1f}
    > {conceitos(media)}
    > {aprovacao(media)}
'''
    print(interface)

def conceitos(media: float):
    if media >= 9:
       return 'CONCEITO A'
    if media >= 7.5:
        return 'CONCEITO B'
    if media >= 6:
        return 'CONCEITO C'
    if media >= 4:
        return 'CONCEITO D'
    else:
        return 'CONCEITO E'


def calcular_media(nota1: float, nota2: float):
    return (nota1+nota2)/2


def aprovacao(media):
    if media >= 6:
        return 'APROVADO'
    if media < 6:
        return 'REPROVADO'
    
main()