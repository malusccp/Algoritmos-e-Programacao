import uteis
import math
def main():
    numero = uteis.get_decimal_number('Digite um número: ')
    uteis.linhas()
    verificar_quadrado_perfeito(numero)
    


def verificar_quadrado_perfeito(numero: int):
    contador = 1 
    maior = 0 

    while (contador ** 2) <= numero:
        quadrado = contador ** 2
        if quadrado > maior:
            maior = quadrado
        contador += 1
    print(f"O maior quadrado menor que {numero} é:\n--> {quadrado} (quadrado de {math.sqrt(quadrado)})")
    uteis.linhas()




main()