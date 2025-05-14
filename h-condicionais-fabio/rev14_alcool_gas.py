import utils
# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# 1. Álcool:
# · até 20 litros, desconto de 3% por litro
# · acima de 20 litros, desconto de 5% por litro
# 2. Gasolina:
# · até 20 litros, desconto de 4% por litro
# · acima de 20 litros, desconto de 6% por litro.
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da
# seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que
# o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
def main():
    combustivel = utils.string('Qual o tipo de combustível? (A- ÁLCOOL | G - GASOLINA): ')
    litros = utils.get_decimal_number_min('Quantos litros deseja obter?: ', 0)
    utils.linhas()

    print(f'O valor do combustível a ser pago é igual a {preço_combustivel(combustivel, litros): .2f}')
    utils.linhas()



def preço_combustivel(combustivel: str, litros: float):
  if combustivel.upper() == 'A':
        if litros <= 20:
            return (1.90 * litros) * 0.97
        else:
            return (1.90 * litros) * 0.95
  elif combustivel.upper() == 'G':
        if litros <= 20:
            return (2.50 * litros) * 0.96
        else:
            return (2.50 * litros) * 0.94
        
main()


