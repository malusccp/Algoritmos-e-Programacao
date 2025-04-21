def main():
    dia_atual = int(input('Digite o dia atual: '))
    mes_atual = int(input('Digite o mês atual em numeral: '))
    ano_atual = int(input('Digite o ano atual: '))

    dia_nasc = int(input('Digite o dia de nascimento: '))
    mes_nasc = int(input('Digite o mês de nascimento: '))
    ano_nasc = int(input('Digite o ano de nascimento: '))
    anos, meses, dias = calcular_idade(dia_nasc, mes_nasc, ano_nasc, dia_atual, mes_atual, ano_atual)

    print(f'A idade será igual a {anos} anos, {meses} meses e {dias} dias')


def calcular_idade(dia_nasc, mes_nasc, ano_nasc, dia_atual, mes_atual, ano_atual):
    anos = ano_atual - ano_nasc 
    meses = mes_atual - mes_nasc
    dias = dia_atual - dia_nasc
    if dias < 0:
       meses = meses - 1
       dias = dias + 30

    
    if  meses < 0:
        anos = anos - 1
        meses = meses + 12

    return anos, meses, dias

main()
