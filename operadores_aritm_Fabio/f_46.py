def principal ():
    mercadoria = float(input('Digite o valor da mercadoria: '))
    parcelas = calcular_parcela(mercadoria)
    entrada = mercadoria - (2 * parcelas)
    print(f'O valor da entrada será R${entrada: .2f} e o valor das duas prestações será igual a R${parcelas: .2f}')

def calcular_parcela(mercadoria):
    parcela = mercadoria // 3
    return parcela

principal ()