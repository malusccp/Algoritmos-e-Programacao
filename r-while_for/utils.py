import os

def get_integer_number(label: str):
    entrada = input(label)

    try:
        numero_a = int(entrada)
        return numero_a
    except ValueError:
        print("Valor Inteiro Inválido")
        return get_integer_number(label)
    
def clear_screen():
    os.system('cls')
    

def get_text(label: str):
  return str(input(label))


def get_integer_number_min(label: str, min_value: int):
    numero = get_integer_number(label)

    while numero < min_value:
        print(f'O valor deve ser no mínimo {min_value}')
        numero = get_integer_number(label)
    return numero


def get_int_in_range(label: str, min_value: int, max_value: int):
    numero = get_integer_number(label)

    while numero > max_value or numero < min_value:
        print(f'Valor fora da faixa ({min_value}-{max_value}) ')
        numero = get_integer_number(label)
    return numero

def linhas():
    print('-' * 30)


def get_decimal_number(label: str):
    entrada = input(label)

    try:
        numero_a = float(entrada)
        return numero_a
    except:
        print('Valor Decimal Inválido!')
        return get_decimal_number(label)
    

def get_decimal_number_min(label: str, min_value: float):
    numero = get_decimal_number(label)

    while numero < min_value:
        print(f'O valor deve ser no mínimo {min_value}')
        numero = get_decimal_number(label)
    return numero



def get_decimal_in_range(label: str, min_value: float, max_value: float):
    numero = get_decimal_number(label)

    while numero < min_value or numero > max_value:
        print(f'Valor fora da faixa! ({min_value}-{max_value})')
    return numero