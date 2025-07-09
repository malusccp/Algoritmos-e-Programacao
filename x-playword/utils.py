import os 

def get_integer_number(label: str):
    entrada = input(label)

    try:
        numero = int(entrada)
    except ValueError:
        print('Valor inteiro inválido!')
        numero = get_integer_number(label)

    return numero

def get_integer_positive(label: str):
    numero = get_integer_number(label)

    while numero < 0:
        print('O valor deve ser maior que 0 !')
        numero = get_integer_number(label)
    return numero


def get_integer_negative(label: str):
    numero = get_integer_number(label)

    while numero > 0:
        print('O valor deve ser menor que 0 !')
        numero = get_integer_number(label)
    return numero

def get_int_in_range(label: str, min_value: int, max_value: int):
    numero = get_integer_number(label)

    while numero < min_value or numero > max_value:
        print(f'Opção inválida! Valor fora da faixa ({min_value}-{max_value})')
        numero = get_integer_number(label)
    return numero

def clear_screen():
    os.system('cls')