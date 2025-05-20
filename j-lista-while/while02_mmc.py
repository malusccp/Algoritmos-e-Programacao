# 2. Leia 2 (dois) números, calcule e escreva o mmc (mínimo múltiplo comum) entre os números lidos.

def main():
    num1 = get_integer_number_min('Número: ', 0)
    num2 = get_integer_number_min('Número: ', 0)

    maior = num1 if num1 > num2 else num2
    
    mmc = maior
    while not (mmc % num2 == 0 and mmc % num1 == 0):
        mmc = mmc + maior

    print(f'O MMC dos números {num1} e {num2} é -> {mmc}')


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

def linhas():
    print('-' *  30)




main()


