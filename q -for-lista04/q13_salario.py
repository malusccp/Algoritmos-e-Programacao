# Leia o salário de funcionários de uma empresa, calcule e escreva o novo salário (segundo os critérios
# descritos abaixo), a soma dos salários atuais, a soma dos salários reajustados e a diferença entre as 2
# somas. (Flag: salário=0)

# De              Até                     Acréscimo
# R$ 0,00         R$ 2.999,99                 25 %
# R$ 3.000,00     R$ 5.999,99                 20 %
# R$ 6.000,00     R$ 9.999,99                 15 %
# Acima de        R$ 10.000,00                10 %
import utils

def main():
    soma_salario_antigo = 0
    soma_novo_salario = 0
    contador = 1
    lista = ''' AUMENTOS:'''
    for i in range(999999999999999999):
        salario_antigo = utils.get_decimal_number_min('Salário: ', 0)
        if salario_antigo == 0:
            break
        soma_salario_antigo += salario_antigo

        novo_salario = calcular_aumento(salario_antigo)

        lista += f'\n {contador}- R${novo_salario:.2f}'
        contador += 1
        soma_novo_salario += novo_salario

    print(lista)
    utils.linhas()
    print(f'SOMA DOS SALÁRIOS ATUAIS: R$ {soma_salario_antigo:.2f}')
    print(f'SOMA DOS SALÁRIOS REAJUSTADOS: R$ {soma_novo_salario:.2f}')


def calcular_aumento(salario_antigo: float):
    if salario_antigo <= 2999.99:
        return salario_antigo * 1.25
    elif salario_antigo <= 5999.99:
        return salario_antigo * 1.20
    elif salario_antigo <= 9999.99:
        return salario_antigo * 1.15
    else:
        return salario_antigo * 1.10
    


    
main()