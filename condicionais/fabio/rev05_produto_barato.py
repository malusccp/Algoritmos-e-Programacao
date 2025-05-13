import utils

def main():
    produto1 = utils.get_decimal_number_min("Preço: ", 0)
    produto2 = utils.get_decimal_number_min("Preço: ", 0)
    produto3 = utils.get_decimal_number_min("Preço: ", 0)

def verificar_mais_barato(produto1: float, produto2: float, produto3: float):
    if produto1 < produto2 and produto1 < produto3:
        print("O produto escolhido deve ser o 1")
    if produto2 < produto1 and produto2 < produto3:
        print("O produto escolhido deve ser o 2")
    if produto3 < produto1 and produto3 < produto2:
        print("O produto escolhido deve ser o 3")


