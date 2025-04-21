from minha_funcoes import obter_numero_inteiro 

def main():
    dia1 = obter_numero_inteiro('Digite uma data(dia): ')
    mes1 = obter_numero_inteiro('Digite uma data(mês): ')
    ano1 = obter_numero_inteiro('Digite uma data(dia): ')
    dia2 = obter_numero_inteiro('Digite outra data(dia): ')
    mes2 = obter_numero_inteiro('Digite outra data(mês): ')
    ano2 = obter_numero_inteiro('Digite outra data(dia): ')
    data_mais_recente(ano1, ano2, mes1, mes2, dia1, dia2)


def data1(dia1, mes1, ano1):
    return print(f'A data {dia1}/{mes1}/{ano1} é a mais recente')


def data2(dia2, mes2, ano2):
    return print(f'A data {dia2}/{mes2}/{ano2} é a mais recente')


def data_mais_recente(ano1, ano2, mes1, mes2, dia1, dia2):
    if ano1 > ano2:
        return data1(dia1, mes1, ano1)
    elif ano1 < ano2:
        return data2(dia2, mes2, ano2)
    
main()