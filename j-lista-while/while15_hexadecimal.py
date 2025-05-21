# 15. Leia um número (entre 0 e 255) na base decimal, calcule e escreva este número na base binária
# e na base hexadecimal.
import utils

def main():
    numero = utils.get_int_in_range('Número: ', 0 , 255)

    binario = converter_binario(numero)
    hexadecimal = converter_hexadecimal(numero)

    print(f'O número {numero} equivale a:\nBase Binária: {binario}\nBase Hexadecimal: {hexadecimal}')



def converter_binario(numero: int): 
    binario = ''
    while numero > 0:
        resto = numero % 2 
        binario = str(resto) + binario
        numero //= 2
    return binario

def converter_hexadecimal(numero: int):
    hexadecimal = ''
    while numero > 0:
        resto = numero % 16 
        hexadecimal = str(resto) + hexadecimal
        numero //= 16
    return hexadecimal
    
main()