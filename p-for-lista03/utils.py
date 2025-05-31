

def get_integer_number(label: str):
    entrada = input(label)

    try:
        entrada = int(entrada)
        return entrada
    except ValueError:
        print('Valor Inteiro Inválido')
        return get_integer_number(label)



def get_integer_number_min(label: str, min_value: int):
    numero = get_integer_number(label)

    while numero < min_value:
        print(f'O valor deve ser no mínimo {min_value}')
        
    return numero





def linhas():
    print('-' * 30)