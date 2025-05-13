def main():
    distancia_total = int(input('Informe a distância total percorrida em km na viagem: '))
    litro_gasolina = float(input('Informe o valor do litro da gasolina: '))
    rendimento_gasolina = int(input('Informe o rendimento de gasolina em km/L: '))
    litro_alcool = float(input('Informe o valor do litro do álcool: '))
    rendimento_alcool = int(input('Informe o rendimento de álcool em km/L: '))
    percentual_motor = float(input('Informe o percentual da viagem que usará o motor elétrico (%): '))
    

    print(f'Para abastecer com gasolina precisará de {litro_combustivel (distancia_total, percentual_motor, rendimento_gasolina):}L')
    print(f'E ele pagará de gasolina R${calcular_combustivel(distancia_total, litro_gasolina, percentual_motor, rendimento_gasolina): .2f}')
    print(f'Para abastecer com álcool precisará de {litro_combustivel (distancia_total, percentual_motor,rendimento_alcool):}L')
    print(f'E com álcool ele pagará R${calcular_combustivel(distancia_total, litro_alcool, percentual_motor, rendimento_alcool): .2f}')

def calcular_combustivel (distancia_total, litro, percentual_motor, rendimento):
    distancia_combustivel = distancia_total - (distancia_total * (percentual_motor/100))
    litros_combustivel = distancia_combustivel / rendimento
    valor_combustivel = litros_combustivel * litro
    return valor_combustivel


def litro_combustivel (distancia_total, percentual_motor, rendimento):
    distancia_combustivel = distancia_total - (distancia_total * (percentual_motor/100))
    litros_combustivel = distancia_combustivel / rendimento
    return litros_combustivel
    

main()