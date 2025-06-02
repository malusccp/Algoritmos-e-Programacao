import utils

def main():
    pessoas = 100
    qtd_hom = 0
    soma_idade_hom = 0
    soma_idade_mulher = 0
    qtd_mulher = 0
    mulher_solteira = 0
    hom_solteiro = 0
    mulher_divorc_30_anos = 0
    for i in range(1, pessoas+1, 1):
        sexo = utils.get_int_in_range('Sexo(1 = MASCULINO | 2 = FEMININO): ', 1, 2)
        idade = utils.get_integer_number_min('Idade: ', 0)
        estado_civil = utils.get_int_in_range('Estado Civil: ', 1, 4)

        if sexo == 1:
            qtd_hom +=1
            soma_idade_hom += idade
            if estado_civil == 2: hom_solteiro +=1
        if sexo == 2:
            qtd_mulher += 1
            soma_idade_mulher += idade
            if estado_civil == 2: mulher_solteira += 1
            if estado_civil == 3 and idade > 30: mulher_divorc_30_anos += 1
        

    interface = f''' === PESQUISA ===
> MÉDIA DE IDADE DOS HOMENS: {media(soma_idade_hom, qtd_hom):.0f} anos
> MÉDIA DE IDADE DAS MULHERES: {media(soma_idade_mulher, qtd_mulher):.0f} anos
> PERCENTUAL DE HOMENS SOLTEIROS: {(hom_solteiro/qtd_hom) * 100:.2f}%
> PERCENTUAL DE MULHERES SOLTEIRAS: {(mulher_solteira/qtd_mulher) * 100:.2f}%
> QUANTIDADE DE MULHERES DIVORCIADAS ACIMA DE 30 ANOS: {mulher_divorc_30_anos} mulheres

'''
    print(interface)
def media(soma: int, n: int):
    return soma/n

main()

