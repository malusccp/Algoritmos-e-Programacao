import utils

def main():
    numero = utils.get_int_in_range('Número: ', 0 , 255)

    binario = converter_binario(numero)
    hexadecimal = converter_hexadecimal(numero)

    print(f'O número {numero} equivale a:\nBase Binária: {binario}\nBase Hexadecimal: {hexadecimal}')



def converter_binario(numero: int): 
    binario = ''
    while True:
        resto = numero % 2 
        binario = str(resto) + binario
        numero //= 2
        if not numero > 0: break
    return binario

def converter_hexadecimal(numero: int):
    hexadecimal = ''
    while True:
        resto = numero % 16 
        hexadecimal = str(resto) + hexadecimal
        numero //= 16
        if not numero > 0: break
    return hexadecimal
    
main()