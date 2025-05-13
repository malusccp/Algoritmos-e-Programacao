def main():
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite um número: '))
    menor_e_maior(numero1, numero2)

def menor_e_maior(numero1, numero2):
    if numero1 > numero2:
        return print(f'{numero1} é o maior e {numero2} é o menor')
    elif numero2 > numero1:
        return print(f'{numero2} é o maior e {numero1} é o menor')
    elif numero1 == numero2:
        return print(f'Os números {numero1} e {numero2} possuem o mesmo valor')
    

main()