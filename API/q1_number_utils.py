
# TEMPO
# 25/05/2025
# INÍCIO 14:05 FIM: 14:17

def get_integer_number(label: str):
    entrada = input(label)

    try:
        numero_a = int(entrada)
        return numero_a
    except ValueError:
        print("Valor Inteiro Inválido")
        return get_integer_number(label)


def get_integer_positive(label: str):
    numero = get_integer_number(label)

    while numero < 0:
        print('O número deve ser maior ou igual a 0!')
        numero = get_integer_number(label)
    return numero

def get_integer_negative(label: str):
    numero = get_integer_number(label)

    while numero > 0:
        print('O número deve ser menor que 0!')
        numero = get_integer_number(label)
    return numero


def get_integer_number_min(label: str, min_value: int):
    numero = get_integer_number(label)

    while numero < min_value:
        print(f'O valor deve ser no mínimo {min_value}')
        numero = get_integer_number(label)
    return numero

def get_integer_number_max(label: str, max_value: int):
    numero = get_integer_number(label)

    while numero > max_value:
        print(f'O valor deve ser no máximo {max_value}')
        numero = get_integer_number(label)
    return numero

def get_int_in_range(label: str, min_value: int, max_value: int):
    numero = get_integer_number(label)

    while numero > max_value or numero < min_value:
        print(f'Valor fora da faixa ({min_value}-{max_value}) ')
        numero = get_integer_number(label)
    return numero
