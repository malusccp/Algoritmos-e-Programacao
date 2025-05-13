import utils

def main():
    valor_hora = utils.get_decimal_number_min('Escreva o valor da hora trabalhada: ', 0)
    horas = utils.get_integer_number_min('Escreva a quantidade de horas trabalhadas no mês: ', 0)
    utils.linhas()
    salario_bruto = valor_hora * horas

    interface = f'''=== FOLHA DE PAGAMENTO ===
            > Salário bruto: {salario_bruto: .2f}
            > (-) IR (5%): {desconto_IR(salario_bruto): .2f}
            > (-) INSS (10%): {desconto_inss(salario_bruto): .2f}
            > FGTS (11%): {desconto_fgts(salario_bruto): .2f}
            > Total de descontos: {total_descontos(salario_bruto): .2f}
            > Salário líquido: {salario_bruto - total_descontos(salario_bruto): .2f}
''' 
    print(interface)


def desconto_IR(salario_bruto):
    if salario_bruto <= 900:
        return 0
    if salario_bruto <= 1500:
        return salario_bruto*(5/100)
    if salario_bruto <= 2500:
        return salario_bruto*(10/100)
    else:
        return salario_bruto*(20/100)
    
def desconto_inss(salario_bruto):
    return salario_bruto * (10/100)

def desconto_fgts(salario_bruto):
    return salario_bruto * (11/100)

def total_descontos(salario_bruto: float):
    return desconto_inss(salario_bruto) + desconto_IR(salario_bruto)


main()

