import os

def get_integer_number(label: str):
    entrada = input(label)

    try:
        numero_a =  int(entrada)
        return numero_a
    except ValueError:
        print("Valor inteiro inválido! ")
        return get_integer_number(label)
    

def get_intnumber_range(label: str, min_value: int, max_value: int):
    numero = get_integer_number(label)

    while numero < min_value or numero > max_value:
        print(f'Valor fora da faixa ({min_value}-{max_value})')
        numero = get_intnumber_range(label, min_value, max_value)
    return numero

def get_decimal_number(label: str):
    entrada = input(label)

    try:
        numero_a =  float(entrada)
        return numero_a
    except ValueError:
        print("Valor decimal inválido! ")
        return get_decimal_number(label)
    
def string(label):
    return input(str(label))

def get_integer_number_min(label: str, min_value: int):
    numero = get_integer_number(label)

    while numero < min_value:
        print(f"O valor deve ser no mínimo {min_value}")
        numero = get_integer_number_min(label, min_value)
    return numero


def get_decimal_number_min(label: str, min_value: float):
    numero = get_decimal_number(label)

    while numero < min_value:
        print(f"O valor deve ser no mínimo {min_value}")
        numero = get_decimal_number_min(label, min_value)
    return numero


def get_decimal_number_max(label: str, max_value: float):
    numero = get_decimal_number(label)

    while numero > max_value:
        print(f"O valor deve ser no máximo {max_value}")
        numero = get_decimal_number_min(label, max_value)
    return numero

def linhas():
    return print('-' * 30)


def clear_screen():
    os.system('cls')
