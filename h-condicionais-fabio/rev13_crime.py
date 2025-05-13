import utils

#     13. Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a) "Telefonou para a vítima ?"
# b) "Esteve no local do crime ?"
# c) "Mora perto da vítima ?"
# d) "Devia para a vítima ?"
# e) "Já trabalhou com a vítima ?"
# O algoritmo deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa
# responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
# "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def main():
    telefonou = utils.get_int_in_range("Telefonou para a vítima? (0 = NÃO | 1 = SIM ): ", 0,1)
    local_crime = utils.get_int_in_range("Esteve no local do crime? (0 = NÃO | 1 = SIM ): ", 0, 1)
    mora_perto = utils.get_int_in_range("Mora perto da vítima? (0 = NÃO | 1 = SIM ): ", 0, 1)
    devia = utils.get_int_in_range("Devia para a vítima? (0 = NÃO | 1 = SIM ): ", 0, 1)
    trabalhou = utils.get_int_in_range("Já trabalhou com a vítima? (0 = NÃO | 1 = SIM ): ", 0, 1)
    utils.linhas()
    soma = telefonou + local_crime + mora_perto + devia + trabalhou
    if soma == 2:
        print('Você foi classificado como: Suspeita')
    elif soma == 3 or soma == 4:
        print('Você foi classificado como: Cúmplice')
    elif soma == 5:
        print('Você foi classificado como: Assasino')
    else: 
        print('Você foi classificado como: Inocente')
    utils.linhas()
 
main()