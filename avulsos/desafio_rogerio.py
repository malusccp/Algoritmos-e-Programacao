def main():
    ano = obter_numero_real('Digite um ano: ')
    verificar_eventos(ano)

def obter_numero_real(label: str):
    return float(input(label))

def ano_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def verificar_eventos(ano):
    if ano_bissexto(ano):
        print('This is a leap year.')
        if ano % 55 == 0:
                print('This is bulukulu festival year.')
    if ano % 15 == 0:
        print('This is huluculu festival year.')
    else:
         print('This is an ordinary year.')

main()
