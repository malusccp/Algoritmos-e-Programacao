import utils

def main():
    numero = utils.get_integer_number_min('Escreva um número: ', 1)

    if numero == 1:
        print('Domingo')
    if numero == 2:
        print('Segunda')
    if numero == 3:
        print('Terça')
    if numero == 4:
        print('Quarta')
    if numero == 5:
        print('Quinta')
    if numero == 6:
        print('Sexta')
    if numero == 7:
        print('Sábado')
    if numero > 7:
     print('Valor Inválido!')

main()