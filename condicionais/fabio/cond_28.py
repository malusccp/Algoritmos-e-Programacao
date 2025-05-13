from minha_funcoes import obter_numero_inteiro

def main():
    x1 = obter_numero_inteiro('Escreva a coordenada x: ')
    y1 = obter_numero_inteiro('Escreva a coordenada y: ')
    x2 = obter_numero_inteiro('Escreva a coordenada x: ')
    y2 = obter_numero_inteiro('Escreva a coordenada y: ')
    area_retangulo(x1,x2,y1,y2)


def base_retangulo(x2, x1):
    if x2 < x1:
        return (x2 - x1) * (-1)
    else:
        return x2 - x1
    
def altura_retangulo(y1, y2):
    if y2 < y1:
        return (y2 - y1) * (-1)
    else:
        return y2 - y1
    
def area_retangulo(x1,x2,y1,y2):
    area = altura_retangulo(y1,y2) * base_retangulo(x2,x1)
    return print(f'A área do retângulo é igual a {area}')

main()
