# 6. Saúde e Bem-estar: Análise de Progresso de Exercícios
# ● Contexto/Problema: Um treinador pessoal precisa monitorar o progresso de seus clientes em um
# determinado exercício ao longo de várias sessões. Para cada sessão de treino, o programa deve
# registrar o número de repetições realizadas e o peso levantado. O programa deve ser capaz de calcular
# o volume total (peso * repetições) para cada sessão e, ao final, identificar a sessão com o maior volume
# e a tendência de melhora (se o volume médio da segunda metade das sessões é maior que o da
# primeira metade).

# ● Entrada: O usuário deve informar a quantidade de sessões de treino para análise. Para cada sessão, o
# usuário deve informar o número de repetições e o peso levantado.
# ● Saída Esperada: Para cada sessão, o volume total. Ao final, indicar a sessão (pelo seu número ou
# identificador) com o maior volume e uma mensagem sobre a tendência de melhora (por exemplo,
# "Tendência de melhora observada" ou "Não houve melhora significativa").
import utils

def main():
    qtd_sessoes = utils.get_integer_number_min('Quantidade de sessões: ', 0)
    maior_volume = 0
    sessao_maior = 0
    primeiras_sessoes = 0
    ultimas_sessoes = 0
    metade = qtd_sessoes // 2
    for sessao in range(1, qtd_sessoes+1):
        print(f"Sessão {sessao}")
        repeticoes = utils.get_integer_number_min('Repetições: ', 0)
        peso = utils.get_decimal_number_min('Peso levantado: ', 0)

        volume_total = repeticoes * peso
        print(f'Volume total = {volume_total} ')
        if volume_total > maior_volume: 
            maior_volume =  volume_total
            sessao_maior = sessao

        if sessao <= metade:
            primeiras_sessoes += volume_total
        else: 
            ultimas_sessoes += volume_total
    qtd_ultimos = qtd_sessoes - metade
    media_primeiras = primeiras_sessoes / metade
    media_ultimas = ultimas_sessoes / qtd_ultimos
    
    interface = f''' === ANÁLISE DE TREINO ===
> Sessão de maior volume: Sessão {sessao_maior} com volume de {maior_volume} kg
> Tendência: {tenderia_melhora(media_primeiras, media_ultimas)}

'''
    print(interface)

def tenderia_melhora(media_primeiras, media_ultimas):
    if media_ultimas > media_primeiras:
        return 'Tendência de melhora'
    else:
        return 'Não houve melhora significativa'

main()