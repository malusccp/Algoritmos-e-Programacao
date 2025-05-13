
from minha_funcoes import ano_bissexto

def main():
    dia = int(input('Digite o dia: '))
    mes = int(input('Digite o mês em numeral: '))
    ano = int(input('Digite o ano: '))
    if not validar_mes(mes):
        return main()
    elif not validar_dia(dia, mes, ano):
        return main()
    return print('A data inserida é válida')
  
def validar_dia(dia, mes, ano):
    if dia > 31:
        print('Dia inválido. Tente novamente.')
        return False
    if mes == 2:
        if ano_bissexto(ano) and dia > 29:
            print('Dia inválido. Tente novamente.')
            return False
        elif not ano_bissexto and dia > 28:
            print('Dia inválido. Tente novamente.')
            return False
        elif dia >= 30:
            print('Dia inválido. Tente novamente.')
            return False
    elif mes in [4, 6, 9, 11] and dia > 30:
        print('Dia inválido. Tente novamente.')
        return False
    return True

def validar_mes(mes):
    if mes > 12:
        print('Mês inválido. Tente novamente.')
        return False
    return True

main()

