import utils

def main():
    salario = utils.get_decimal_number_min('Escreva o salário (R$): ', 0)
    utils.linhas()
    interface = f''' ==== CALCULADORA DE AUMENTO ====
    > Salário antes do reajuste: R${salario: .2f}
    > Percentual de aumento aplicado: {percentual(salario)}
    > Valor do aumento: R${calcular_aumento(salario): .2f}
    > Novo salário: R${reajuste_salario(salario): .2f}

'''
    print(interface)
    
def percentual(salario):
    if salario <= 280:
       return '20%'
    if salario < 700:
        return '15%'
    if salario < 1500:
        return '10%'
    else:
        return '5%'
    

def reajuste_salario(salario):
    if salario <= 280:
       return salario * 1.2
    if salario < 700:
        return salario * 1.15
    if salario < 1500:
        return salario * 1.10
    else:
        return salario * 1.05
    

def calcular_aumento(salario):
    novo_salario = reajuste_salario(salario)
    aumento = novo_salario - salario
    return aumento


main()



