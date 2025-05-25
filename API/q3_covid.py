# TEMPO
# 25/05/2025
# INÍCIO: 14:56 FIM: NÃO CONCLUÍDA

from q1_number_utils import get_integer_number

def main():
    total_casos = 0
    em_alta = 0
    em_estabilidade = 0
    em_queda = 0
    dias = 0
    casos_dia_anterior = 0
    while True:
        qtd_casos = get_integer_positive("Número de casos: ")
        if qtd_casos == 'fim':
            break
        else:
            casos_dia_anterior = qtd_casos
            dias += 1
            total_casos += qtd_casos
            variacao = ((qtd_casos - casos_dia_anterior)/casos_dia_anterior) * 100
            if variacao > -15/100 or variacao < 15/100:
                em_estabilidade += 1
            elif variacao >= 15/100:
                em_alta += 1
            else:
                em_queda +=1


    interface = f''''=== CASOS DE COVID ===
>TOTAL DE CASOS: {total_casos}
> MÉDIA DE CASOS: {total_casos/dias:.2f}
    '''
    print('')

def determinar_conceito(em_estabilidade, em_alta, em_queda):
    conceito = max(em_alta, em_estabilidade, em_queda)

    if conceito == em_alta:
        return 'Em alta'
    elif conceito == em_estabilidade:
        return 'Em estabilidade'
    else:
        return 'Em queda'

def get_integer_positive(label: str):
    numero = get_integer_number(label)

    while numero < 0:
        print('Valor não computado')
        numero = get_integer_number(label)
    return numero

main()