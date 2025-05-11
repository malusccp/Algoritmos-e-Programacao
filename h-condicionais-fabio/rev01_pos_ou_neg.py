import utils

def main():
    num = utils.get_integer_number("Número: ")
    verificar_num(num)


def verificar_num(num: int):
    if num < 0:
        return print(f'{num} é um número NEGATIVO')
    else:
        return print(f"{num} é um número POSITIVO")

main()