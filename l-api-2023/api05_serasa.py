

def main():
    criterio_a = get_int_in_range('Digite o valor em relação ao critério A: ', 0, 100)
    criterio_b = get_int_in_range('Digite o valor em relação ao critério B: ', 0, 100)
    criterio_c = get_int_in_range('Digite o valor em relação ao critério C: ', 0, 100)
    
    score_antigo = (260 * (criterio_a/100)) + (570 * (criterio_b/100)) + (170 * (criterio_c/100)) 
    score_novo = (620 * (criterio_a/100)) + (190 * (criterio_b/100)) + (190 * (criterio_c/100))

    calculadora_serasa = f''' === CALCULADORA SERASA ===
> CRITÉRIO A: {criterio_a}
> CRITÉRIO B: {criterio_b}
> CRITÉRIO C: {criterio_c}
-----------------------------------
> SCORE 1.0: {score_antigo:.0f} -> {classificar_score_antigo(score_antigo)}
> SCORE 2.0: {score_novo:.0f} -> {classificar_score_novo(score_novo)}
'''
    print(calculadora_serasa)


def classificar_score_antigo(score: int):
    if score <= 400:
        return 'Baixo'
    elif score <= 600:
        return 'Regular'
    elif score <= 800:
        return 'Bom'
    else:
        return 'Muito bom'


def classificar_score_novo(score: int):
    if score < 301:
        return 'Baixo'
    elif score < 501:
        return 'Regular'
    elif score < 701:
        return 'Bom'
    else:
        return 'Muito Bom'


def get_int_in_range(label: str, min_value: int, max_value: int):
    numero = get_integer_number(label)

    while numero > max_value or numero < min_value:
        print(f'Valor fora da faixa ({min_value}-{max_value})')
        numero = get_integer_number(label)
    return numero


def get_integer_number(label: str):
    entrada = input(label)

    try:
        numero_a = int(entrada)
        return numero_a
    except ValueError:
        print('Valor Inteiro Inválido!')
        return get_integer_number(label)
    

main()