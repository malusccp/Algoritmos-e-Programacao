# 18. Supondo-se que a população de uma cidade A seja de 200.000 habitantes, com uma taxa anual de
# crescimento na ordem de 3.5%, e que a população de uma cidade B seja de 800.000 habitantes,
# crescendo a uma taxa anual de 1.35%, Escreva um algoritmo que determine quantos anos serão
# necessários, para que a população da cidade A ultrapasse a população da cidade B.
import utils

def main():
    cidade_a = utils.get_decimal_number_min('População A: ', 0)
    cidade_b = utils.get_decimal_number_min('População B: ', (cidade_a+1))

    anos = 0

    while cidade_a <= cidade_b:
        cidade_a *= (1 + (3.5/100))
        cidade_b *= (1 + (1.35/100))

        anos += 1

    print(f'Serão necessários {anos} anos')

main()