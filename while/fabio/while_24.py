import uteis

def main():
    n = uteis.get_integer_number("Digite o número de habitantes que deseja consultar: ")
    print('>>>>>>> AVALIAÇÃO SOCIOECONÔMICA <<<<<<<<')
    uteis.linhas()
    ler_informacoes(n)
    

def ler_informacoes(n: int):
    contador = 0
    soma_salarios = 0
    salario_maior_mil = 0
    soma_filhos = 0
    while contador < n:
        salario_hab = uteis.get_decimal_number_min("Digite o salário do habitante: ", 0)
        numero_filhos = uteis.get_integer_number_min("Digite o número de filhos do habitante: ", 0)
        uteis.linhas()
        contador += 1
        soma_filhos += numero_filhos
        
        if salario_hab <= 1000:
         salario_maior_mil += 1
        else:
         soma_salarios += salario_hab


    media_salarios = calcular_media(soma_salarios, n)
    media_filhos = calcular_media(soma_filhos, n)
    percentual = calcular_percentual(salario_maior_mil, n)
    
    print(f"MÉDIA DE SALÁRIOS DA POPULAÇÃO: {media_salarios: .1f}\nMÉDIA DOS FILHOS DA POPULAÇÃO: {media_filhos: .0f}\nPERCENTUAL DE SALÁRIOS >= 1000: {percentual: .1f}")
    uteis.linhas()


def calcular_percentual(parte: int, total:int) -> float:
    return (parte/total) * 100


def calcular_media(soma: int, n: int):
    return soma/n


main()