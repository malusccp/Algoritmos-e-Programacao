def main():
    velocidade = obter_numero_real('Digite a velocidade atual do carro: ')
    limite_permitido = obter_numero_real('Digite a velocidade permitida da via: ')
    clima_chuvoso = str(input('Está chovendo na estrada?: '))
    penalidade(velocidade, limite_permitido, clima_chuvoso)


def obter_numero_real(label: str):
    return float(input(label))

def limite_chuva(limite_permitido, clima_chuvoso):
    if clima_chuvoso == 'Sim' or clima_chuvoso == 'sim':
     return limite_permitido - (limite_permitido * 0.2)
    if clima_chuvoso == 'Não' or clima_chuvoso == 'não':
     return limite_permitido


def penalidade(velocidade, limite_permitido, clima_chuvoso):

    excesso = velocidade - limite_chuva(limite_permitido, clima_chuvoso)
    if excesso <= 0:
        print('Dentro da velocidade permitida.')
    elif excesso <= limite_permitido * 0.1:
        print('Infração leve: A multa a ser paga é de R$ 130.00')
    elif excesso <= limite_permitido * 0.3:
        print('Infração grave: A multa a ser paga é de R$ 195.00')
    else:
        print('Infração gravíssima: A multa a ser paga é de R$ 880.00')



main()

