def main():
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite um número: '))
    numero3 = int(input('Digite um número: '))
    ordem_crescente(numero1, numero2, numero3)

def ordem_crescente(numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3 and numero2 > numero3:
        return print(f'A ordem crescente será {numero3}, {numero2}, {numero1}')
    if numero1 > numero2 and numero1 > numero3 and numero3 > numero2:
        return print(f'A ordem crescente será {numero2}, {numero3}, {numero1}')
    if numero2 > numero1 and numero2 > numero3 and numero1 > numero3:
        return print(f'A ordem crescente será {numero3}, {numero1}, {numero2}')
    if numero2 > numero1 and numero2 > numero3 and numero3 > numero1:
        return print(f'A ordem crescente será {numero1}, {numero3}, {numero2}')
    if numero3 > numero1 and numero3 > numero2 and numero1 > numero2:
        return print(f'A ordem crescente será {numero2}, {numero1}, {numero3}')
    if numero3 > numero1 and  numero3 > numero2 and numero2 > numero1:
        return print(f'A ordem crescente será {numero1}, {numero2}, {numero3}')



main()