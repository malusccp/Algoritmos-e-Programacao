
def main():
    sequencia = get_integer_number('Quantidade de sequências: ')

    while sequencia > 0:
        num = get_integer_number('Número (0 = PARAR): ')
    
        while True:
                soma_pares = 0
                soma_total = 0
                maior_num = None
                menor_num = None
                contador = 1

                if num % 2 == 0:
                    soma_pares += num
                
                soma_total += num
                if maior_num == None or num > maior_num:
                    maior_num = num
                if menor_num == None or num < menor_num:
                    menor_num = num
        sequencia -= 1
        print(f'Soma pares:{soma_pares}\nMédia números:{(soma_total/contador)}\nMaior número:{maior_num}\n Menor número:{menor_num} ')

        soma_pares = 0
        soma_total = 0
        maior_num = None
        menor_num = None
        contador = 0
        






def get_integer_number(label: str):
    entrada = input(label)

    try:
        numero_a = int(entrada)
        return numero_a
    except ValueError:
        print("Valor Inteiro Inválido")
        return get_integer_number(label)
    

main()