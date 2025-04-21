from minha_funcoes import obter_numero_inteiro

def main():
    num1 = obter_numero_inteiro('Digite um número: ')
    num2 = obter_numero_inteiro('Digite um número: ')
    operacao = obter_numero_inteiro('Digite a operação a ser executada: ')
    escolher_operacao(num1, num2, operacao)


def escolher_operacao(num1, num2, operacao):
    if operacao == 1:
        return print(f'A soma entre {num1} e {num2} é igual a {num1 + num2}')
    elif operacao == 2:
        return print(f'A diferença entre {num1} e {num2} é igual a {num1 - num2}')
    elif operacao == 3:
        return print(f'O produto de {num1} e {num2} é igual a {num1 * num2}')
    elif operacao == 4:
        return print(f'A divisão entre {num1} e {num2} é igual a {num1 / num2}')

  
main()