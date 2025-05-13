from minhas_funcoes import obter_numero_inteiro
from minhas_funcoes import obter_resposta

def main():
    idade_passageiro = obter_numero_inteiro('Digite sua idade: ')
    acompanhante = obter_resposta('O passageiro está acompanhado?: ')
    velocidade_onibus = obter_numero_inteiro('Digite a velocidade(km/h): ')
    multa_velocidade(velocidade_onibus)
    multa_passageiro(idade_passageiro, acompanhante)


def multa_velocidade(velocidade_onibus):
    limite = 90
    if (velocidade_onibus - limite) <= 10:
        return print('Multa leve')
    if (velocidade_onibus - limite) <= 30:
        return print('Multa grave')
    if (velocidade_onibus - limite) > 30:
        return print('Multa gravíssima')
    else:
        return print('Sem multa')
    

def multa_passageiro(idade_passageiro, acompanhante):
    if idade_passageiro < 12:
        return print('Autorização necessária')
    if idade_passageiro <= 17 and (acompanhante == 'sim' or acompanhante == 'Sim'):
        return print('Autorização dispensada')
    if idade_passageiro <= 17 and (acompanhante == 'não' or acompanhante == 'Não'):
        return print('Autorização necessária')
    else:
        return print('Autorização dispensada')
    
main()