# 26. Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião
# em relação ao filme (1=ótimo, 2=bom, 3=regular, 4=péssimo). Escreva um algoritmo que leia a idade e
# a opinião das pessoas, calcule e mostre ao final: (FLAG: idade = -1).
# · a média das idades das pessoas que responderam ótimo;
# · a quantidade de pessoas que respondeu regular;
# · o percentual de pessoas que respondeu bom entre os entrevistados.

import utils

def main():

    pessoas_total = 0
    otimo = 0
    soma_idade_otimo = 0
    bom = 0
    regular = 0
    pessimo = 0
    while True:
        idade = utils.get_integer_number_min('Idade: ', -1)
        if idade == -1:
            break
        opiniao = utils.get_int_in_range('Opinião: ', 1, 4)
        pessoas_total += 1
        if opiniao == 1: 
            otimo += 1
            soma_idade_otimo += idade
        elif opiniao == 2:bom += 1
        elif opiniao == 3: regular += 1 
        elif opiniao == 4: pessimo += 1
    interface = f'''=== CINEMA ===
MÉDIA DAS IDADES DAS PESSOAS QUE RESPONDERAM ÓTIMO: {soma_idade_otimo/otimo:.2f} anos
QUANTIDADE DE PESSOAS QUE RESPONDEU REGULAR: {regular} pessoas
PERCENTUAL DE PESSOAS QUE RESPONDEU BOM ENTRE OS ENTREVISTADOS: {100 * (bom/pessoas_total):.2f}%
    
      '''
    print(interface)

main()