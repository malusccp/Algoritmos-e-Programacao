
def main():
    N = int(input('Número: '))
    contador_ate_n(N)


def contador_ate_n(N: int, atual=1):
    if atual > N:
        return
    print(atual)
    contador_ate_n(N, atual + 1)

main()