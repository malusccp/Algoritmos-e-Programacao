import uteis

def main():
    a0 = uteis.get_integer_number_not_zero("Escreva o primeiro termo da P.G: ")
    razao_r = uteis.get_integer_number("Escreva a razão da P.G: ")
    limite = uteis.get_integer_number("Escreva o limite que os termos podem atingir: ")
    print('Os termos da P.G são iguais a: ')
    ler_menores_limites(a0, razao_r, limite)



def ler_menores_limites(a0:int, razao_r: int, limite: int):
    progressao = (a0 * razao_r)
    print(a0)
    while (progressao) < limite:
        print(progressao)
        (progressao) *= razao_r

main()