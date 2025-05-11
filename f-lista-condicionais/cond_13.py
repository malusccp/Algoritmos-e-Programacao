from minha_funcoes import obter_numero_inteiro

def main():
    num1 = obter_numero_inteiro('Digite um número: ')
    num2 = obter_numero_inteiro('Digite um número: ')
    num3 = obter_numero_inteiro('Digite um número: ')
    num4 = obter_numero_inteiro('Digite um número: ')
    num5 = obter_numero_inteiro('Digite um número: ')
    eh_maior(num1, num2, num3, num4, num5)
    eh_menor(num1, num2, num3, num4, num5)


def eh_maior(num1, num2, num3, num4, num5):
    if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
        return print(f'O número {num1} é o maior número')
    if num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
        return print(f'O número {num2} é o maior número')
    if num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
        return print(f'O número {num3} é o maior número')
    if num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
        return print(f'O número {num4} é o maior número')
    if num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
        return print(f'O número {num5} é o maior número')
    
def eh_menor(num1, num2, num3, num4, num5):
    if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
        return print(f'O número {num1} é o menor número')
    if num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
        return print(f'O número {num2} é o menor número')
    if num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5:
        return print(f'O número {num3} é o menor número')
    if num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5:
        return print(f'O número {num4} é o menor número')
    if num5 < num1 and num5 < num2 and num5 < num3 and num5 < num4:
        return print(f'O número {num5} é o menor número')
    
main()