# 5. Leia dois números X e N. A seguir, escreva o resultado das divisões de X por N onde, após cada
# divisão, X passa a ter como conteúdo o resultado da divisão anterior e N é decrementado de 1 em 1, até
# chegar a 2.
 

def main(): 
    X = int(input('X: '))
    N = int(input('N: '))

    for i in range(N, 2-1, -1):
        divisao = X/i
        X = divisao
        print(divisao)

main()