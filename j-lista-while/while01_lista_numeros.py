

def main():
    numero = get_integer_number_min('Digite um número (Quando quiser parar, digite 0): ', 0)
    validar_divisores(numero)


def validar_divisores(numero: int):
    while numero != 0:
        print(f'Divisores do número {numero}')
        contador = 1
        while contador <= numero :
            if numero % contador == 0:
                print(contador)
            contador += 1
        numero = get_integer_number_min('Digite um número (Quando quiser parar, digite 0): ', 0)
        return validar_divisores(numero)
    
    

def get_integer_number(label: str):
    entrada = input(label)

    try:
        numero_a = int(entrada)
        return numero_a
    except ValueError:
        print("Valor Inteiro Inválido")
        return get_integer_number(label)
    

def get_integer_number_min(label: str, min_value: int):
    numero = get_integer_number(label)

    while numero < min_value:
        print(f'O valor deve ser no mínimo {min_value}')
        numero = get_integer_number(label)
    return numero


main()