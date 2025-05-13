from minhas_funcoes import obter_numero_inteiro
from minhas_funcoes import obter_numero_real

def main():
    distancia_percorrida = 0
    tanque = 0

    while distancia_percorrida < 600 or tanque < 50:
        distancia_percorrida = obter_numero_real('Digite a distância percorrida: ')
        tanque = obter_numero_inteiro('Digite a quantidade gasta em litros: ')
        
