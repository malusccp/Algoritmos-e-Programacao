# 5. Clima e Tempo: Monitoramento de Variações de Temperatura e Umidade
# ● Contexto/Problema: Um sistema de monitoramento climático registra a temperatura e a umidade a
# cada hora em um determinado local. O programa deve permitir que o usuário informe o número de
# horas para as quais os dados serão inseridos. Para cada hora, o usuário deve inserir a temperatura
# (°C) e a umidade (%). O programa deve identificar o maior pico de temperatura, o menor valor de
# umidade e a quantidade de vezes que a temperatura ultrapassou um limite predefinido pelo usuário.
# ● Entrada: O usuário deve informar a quantidade de horas para as quais os dados serão inseridos. Para
# cada hora, o usuário deve informar a temperatura e a umidade. O usuário também deve informar um
# limite de temperatura a ser monitorado.
# ● Saída Esperada: A maior temperatura registrada, a menor umidade registrada, e a contagem de vezes
# que a temperatura excedeu o limite predefinido.
import utils

def main():
    qtd_horas = utils.get_integer_number_min('Quantidade de horas: ', 0)
    maior_temp = None
    menor_umidade = None
    excedeu = 0
    for hora in range(1, qtd_horas+1, 1):
        limite_temp = utils.get_decimal_number('Limite de temperatura: ')
        temperatura = utils.get_decimal_number_min('Temperatura: ', 0)
        umidade = utils.get_integer_number_min('Umidade: ', 0)

        if limite_temp > temperatura: excedeu += 1

        if maior_temp == None or maior_temp < temperatura: maior_temp = temperatura
        if menor_umidade == None or menor_umidade > temperatura: menor_umidade = temperatura

    interface = f'''=== Monitoramento de Variações de Temperatura e Umidade ===
Maior temperatura: {maior_temp}°C
Menor umidade: {menor_umidade}%
Quantas vezes a temperatura excedeu o limite predefinido: {excedeu} vezes
'''
    print(interface)



main()