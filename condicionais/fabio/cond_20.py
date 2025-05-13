from minha_funcoes import obter_numero_inteiro


def main():
    angulo = obter_numero_inteiro('Digite um ângulo em graus: ')
    qual_quadrante(angulo)


def qual_quadrante(angulo):
    if angulo <= 90:
        return print(f'O ângulo {angulo} pertence ao 1° quadrante')
    elif angulo <= 180:
        return print(f'O ângulo {angulo} pertence ao 2° quadrante')
    elif angulo <= 270:
        return print(f'O ângulo {angulo} pertence ao 3° quadrante')
    else:
        return print(f'O ângulo {angulo} pertence ao 4° quadrante')
    
main()