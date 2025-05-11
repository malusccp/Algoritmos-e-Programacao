from minha_funcoes import obter_numero_inteiro

def main():
    num = obter_numero_inteiro('Digite um número de 4 dígitos: ')
    validando_propriedade(num)



def soma_dezenas(num):
    d1 = (num // 1000) * 10 
    d2 = ((num % 1000) // 100)
    d3 = (((num % 1000) % 100) // 10) * 10
    d4 = ((num % 100) % 100) % 10
    return (d1+d2) + (d3+d4)


def validando_propriedade(num):
    if soma_dezenas(num)**2 == num:
        return print(f'A propriedade é válida para {num}')
    else:
        return print(f'A propriedade não é válida para {num}')
    

main()