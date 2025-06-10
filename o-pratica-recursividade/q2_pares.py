
def main():
    N = int(input('Número: '))
    contar_pares(N)



def contar_pares(N: int, atual=1):
    if atual > N:
        return
    
    if atual % 2 == 0:
        print(atual)
    contar_pares(N, atual + 1)

main()