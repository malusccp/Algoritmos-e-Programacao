# 17. Em um concurso de beleza, cada candidata tem um cartão contendo nome, altura e peso. Escreva um
# algoritmo que leia um conjunto de cartões e escreva o nome e a altura da candidata mais alta e da mais
# baixa; o nome e o peso da candidata mais magra e da mais gorda. (Flag: nome = 'FIM').
import utils

def main():
    qtd_cartoes = utils.get_integer_number_min('Número de cartões: ', 1)
    candidata_alta = ''
    candidata_baixa = ''
    candidata_magra = ''
    candidata_gorda = ''
    mais_alta = None
    mais_baixa = None
    mais_magra = None
    mais_gorda = None
    for i in range(qtd_cartoes, 0, -1):
        nome = utils.get_text('Nome da candidata: ')
        if nome == ('fim').upper:
            break
        altura = utils.get_decimal_number_min('Altura da candidata (m): ', 0)
        peso = utils.get_decimal_number_min('Peso da candidata (kg): ', 0)


        if mais_alta == None or mais_alta < altura:
            mais_alta = altura
            candidata_alta = nome
        if mais_baixa == None or mais_baixa > altura:
            mais_baixa = altura
            candidata_baixa = nome

        if mais_magra == None or mais_magra > peso:
            mais_magra = peso
            candidata_magra = nome
        if mais_gorda == None or mais_gorda < peso:
            mais_gorda = peso
            candidata_gorda = nome
        qtd_cartoes -= 1
    cartoes = f'''=== CONCURSO DE BELEZA: ===
> CANDIDATA MAIS GORDA:
Nome: {candidata_gorda}
Peso: {mais_gorda} kg
> CANDIDATA MAIS MAGRA:
Nome: {candidata_magra}
Peso: {mais_magra}
> CANDIDATA MAIS ALTA :
Nome: {candidata_alta}
Altura: {mais_alta} m
> CANDIDATA MAIS BAIXA :
Nome: {candidata_baixa}
Altura: {mais_baixa} m
    '''

    print(cartoes)

main()
