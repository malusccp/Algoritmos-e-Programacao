



def calcular_anos(ano_atual, ano_nasc, mes_atual, mes_nasc):
    anos = ano_atual - ano_nasc
    if mes_atual < mes_nasc:
        return anos - 1
    else:
        return anos
    
def main():
    dia_atual = int(input('Digite o dia atual: '))
    mes_atual = int(input('Digite o mês atual em numeral: '))
    ano_atual = int(input('Digite o ano atual: '))
    dia_nasc = int(input('Digite o dia de nascimento: '))
    mes_nasc = int(input('Digite o mês de nascimento: '))
    ano_nasc = int(input('Digite o ano de nascimento: '))
    anos = calcular_anos(ano_atual, ano_nasc, mes_atual, mes_nasc)
    print(f'A sua idade é igual a {anos} anos')

main()