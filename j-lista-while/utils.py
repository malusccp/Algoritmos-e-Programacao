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


def get_int_in_range(label: str, min_value: int, max_value: int):
    numero = get_integer_number(label)

    while numero > max_value or numero < min_value:
        print(f'Valor fora da faixa ({min_value}-{max_value}) ')
        numero = get_integer_number(label)
    return numero

def linhas():
    print('-' * 30)