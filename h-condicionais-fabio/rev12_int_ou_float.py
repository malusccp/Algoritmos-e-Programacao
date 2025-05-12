import utils
# 12. Leia um número e escreva se o número é inteiro ou decimal.

def main():
    numero = utils.get_decimal_number('Número: ')

    if numero % 1 == 0:
        return print('É inteiro')
    else:
        return print('É decimal')
    

main()