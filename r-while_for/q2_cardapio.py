import utils
# 2. Alimentação: Otimização de Cardápio para Múltiplas Pessoas
# ● Contexto/Problema: Um planejador de refeições precisa calcular os valores nutricionais de um
# cardápio específico para um grupo de pessoas. Para cada pessoa, o programa deve permitir que o
# usuário informe vários alimentos consumidos e suas respectivas quantidades (em gramas). O programa
# deve ser capaz de consultar uma lista de alimentos e seus valores calóricos/nutricionais por 100g (a ser
# embutida no código, ou seja, não precisa ser uma entrada do usuário). O objetivo é calcular o total de
# calorias e proteínas ingeridas por cada pessoa e, ao final, determinar a pessoa com o maior e menor
# consumo de calorias totais.
# ● Dados Iniciais (Exemplo de estrutura a ser embutida no código, adicione pelo menos 10
# alimentos mais comuns, indicando sempre calorias e proteínas por 100f):
# alimentos = {
# "arroz": {"calorias": 130, "proteinas": 2.7},
# "frango": {"calorias": 165, "proteinas": 31},
# ...,
# }
# ○ Exemplo, como obter valores (por 100g).
# ○ valor_calorico = alimentos[‘frango’][‘calorias’]
# ○ valor_proteico = alimentos[‘frango’][‘proteinas’]
# ● Entrada: O usuário deve informar a quantidade de pessoas para análise. Para cada pessoa, o usuário
# deve informar a quantidade de alimentos que serão adicionados ao cardápio e, para cada alimento, seu
# nome (correspondente aos dados iniciais) e a quantidade em gramas. Valide o nome do alimento, se
# inválido pedir novamente.
# ● Saída Esperada: Para cada pessoa, o total de calorias e proteínas consumidas. Ao final, indicar qual
# pessoa teve o maior e o menor consumo calórico total.
alimentos = {
    'amendoim_japones': {'calorias': 500, 'proteinas': 14},
    'banana_nanica': {'calorias': 89, 'proteinas': 1.1},
    'frango_grelhado': {'calorias': 165, 'proteinas': 31},
    'arroz_integral': {'calorias': 111, 'proteinas': 2.6},
    'feijao_preto': {'calorias': 132, 'proteinas': 8.9},
    'ovo_cozido': {'calorias': 77, 'proteinas': 6.3},
    'abacate': {'calorias': 160, 'proteinas': 2},
    'batata_doce': {'calorias': 86, 'proteinas': 1.6},
    'salmão_grelhado': {'calorias': 208, 'proteinas': 20},
    'iogurte_natural': {'calorias': 61, 'proteinas': 3.5}
}

def main():
    pessoas = int(input('Insira a quantidade de pessoas: '))
    menor_consumo = None
    maior_consumo = None
    for pessoa in range(1, pessoas + 1, 1):
        print(f'Pessoa {pessoa}')
        qtd_produto = int(input('Qtd de produtos: '))

        total_calorias = 0
        total_proteinas = 0

        for produto in range(1, qtd_produto+1):
            nome = obter_alimento()
            gramas = float(input('Peso (g): '))


            calorias = (alimentos[nome]['calorias'] * gramas) / 100
            proteinas =  (alimentos[nome]['proteinas'] * gramas) / 100

            total_calorias += calorias
            total_proteinas += proteinas

            if maior_consumo == None or total_calorias > maior_consumo:
                maior_consumo = total_calorias
            if menor_consumo == None or total_calorias < menor_consumo:
                menor_consumo = total_calorias
        print(f'Consumo calórico: {total_calorias:.2f} calorias\nConsumo proteico: {total_proteinas:.2f}g de proteína')

    print(f'Maior consumo calórico: {maior_consumo}\nMenor consumo: {menor_consumo}')

def obter_alimento():
    while True:
        nome = (input('Insira o produto: ')).lower()
        if nome in alimentos:
            return nome
        else:
            print('Alimento Inválido. Tente novamente')
            obter_alimento()
main()


            
            


