# TEMPO
# 25/05/2025
# INÍCIO: 14:19 FIM: 14:43

from q1_number_utils import get_integer_number

def main():
    sequencia = get_integer_number('Quantidade de sequências: ')
    soma_pares = 0
    soma_total = 0
    maior_num = None
    menor_num = None
    qtd_numeros = 0

    while sequencia > 0:
        while True:
            num = get_integer_number('Número (0 = PARAR): ')
            if num == 0:
                break
            else:
                qtd_numeros += 1

                if num % 2 == 0:
                    soma_pares += num
                                
                soma_total += num
                if maior_num == None or num > maior_num:
                    maior_num = num
                if menor_num == None or num < menor_num:
                    menor_num = num

        sequencia -= 1
    print(f'Soma pares:{soma_pares}\nMédia números:{(soma_total/qtd_numeros)}\nMaior número:{maior_num}\nMenor número:{menor_num} ')




main()