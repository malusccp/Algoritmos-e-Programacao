def main():
    numero = int(input('Digite um número: '))
    eh_igual(numero)


def eh_igual(numero):
    if numero // 10 == numero % 10:
        return print(f'O número {numero} possui o algarismo da dezena igual ao algarismo da unidade')
    else:
        return print(f'O número {numero} possui o algarismo da dezena diferente do algarismo da unidade')
    
main()