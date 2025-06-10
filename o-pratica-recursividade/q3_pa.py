def main():
    a0 = int(input('A0: '))
    limite = int(input('Limite: '))
    R = int(input('Razão: '))
    abaixo_do_limite(a0, limite, R)


def abaixo_do_limite(a0: int, limite: int, R: int):
    if a0 >= limite:
        return
    print(a0)
    abaixo_do_limite(a0+R, limite, R)

main()