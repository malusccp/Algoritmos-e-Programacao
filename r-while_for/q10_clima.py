# 10. Clima e Tempo: Análise de Tendências de Temperatura ao Longo de Anos
# ● Contexto/Problema: Um pesquisador climático deseja analisar as tendências de temperatura máxima
# anual ao longo de uma série de anos. O programa deve permitir que o usuário insira o número de anos
# para os quais os dados serão registrados. Para cada ano, o usuário deve informar a temperatura
# máxima média anual. O programa deve identificar o ano com a maior temperatura, o ano com a menor
# temperatura, e calcular a média das temperaturas anuais. Além disso, deve indicar se houve uma
# tendência de aquecimento (se a média dos últimos anos for maior que a média dos primeiros anos).

# ● Entrada: O usuário deve informar a quantidade de anos para análise. Para cada ano, o usuário deve
# informar a temperatura máxima média anual.

# ● Saída Esperada: O ano (ou índice do ano) com a maior temperatura, o ano (ou índice do ano) com a
# menor temperatura, e a média geral das temperaturas anuais. Uma mensagem indicando se há uma
# tendência de aquecimento ou resfriamento baseada na comparação das médias da primeira e segunda
# metades dos anos.
import utils



def main():
    anos = utils.get_integer_number_min('Anos: ', 0)

    soma_total = 0
    soma_primeiros = 0
    soma_ultimos = soma_total - soma_primeiros
    maior_temp = None
    menor_temp = None
    metade = anos // 2
    for ano in range(1, anos+1):
        temperatura = utils.get_decimal_number('Temperatura: ')
        soma_total += temperatura

        if maior_temp == None or maior_temp < temperatura:
            maior_temp = temperatura
        if menor_temp == None or menor_temp > temperatura:
            menor_temp = temperatura

        if ano <= metade:
            soma_primeiros += temperatura
        else:
            soma_ultimos += temperatura

    qtd_ultimos = anos - metade
    media_primeiros = media(soma_primeiros, metade) if metade > 0 else 0
    media_ultimos = media(soma_ultimos, qtd_ultimos) if qtd_ultimos > 0 else 0
    resultado = f'''
MAIOR TEMPERATURA: {maior_temp}
MENOR TEMP: {menor_temp}
Média de temperatura: {media(soma_total, anos):.2f}
Tendência: {tendencia_aquecimento(media_primeiros, media_ultimos)}

'''
    print(resultado)
def media(soma, n):
    return soma/n

def tendencia_aquecimento(media_primeiros, media_ultimos):
    if media_ultimos > media_primeiros:
        return 'Tendência de aquecimento'
    else:
        return 'Tendência de resfriamento'

main()