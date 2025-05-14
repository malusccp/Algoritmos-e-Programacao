# 15. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#            Até 5 Kg | Acima de 5 Kg
# Morango R$ 2,50 por Kg  R$ 2,20 por Kg
# Maçã R$ 1,80 por Kg R$   1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá
# ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de
# morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
import utils

def main():
    kg_morangos = utils.get_decimal_number_min('Quantos kg de morango deseja comprar?: ', 0)
    kg_maçãs = utils.get_decimal_number_min('Quantos kg de maçã deseja comprar?: ', 0)
    utils.linhas()
    interface = f''' === FEIRA DO MATSKI ===
    > KG DE MAÇÃS: {kg_maçãs}kg
    > KG DE MORANGOS: {kg_morangos}kg
    > TOTAL = {desconto_total(kg_morangos, kg_maçãs): .2f}
'''
    print(interface)
    utils.linhas()

def preço_morango(kg_morangos: float):
    if kg_morangos <= 5:
        return kg_morangos * 2.5
    else: 
       return kg_morangos * 2.20
    

def preço_maçãs(kg_maçãs: float):
    if kg_maçãs <= 5:
        return kg_maçãs * 1.80
    else:
        return kg_maçãs * 1.50
    

def total_frutas(kg_morangos: float, kg_maçãs: float):
    return preço_maçãs(kg_maçãs) + preço_morango(kg_morangos)


def desconto_total(kg_morangos: float, kg_maçãs: float):
    if (kg_maçãs + kg_morangos > 8) or total_frutas > 25:
        return total_frutas(kg_morangos, kg_maçãs) * 0.9
    else:
        return total_frutas(kg_morangos, kg_maçãs)

main()

