# Entrada
custo_fabrica = float(input('Digite o custo de fábrica: '))
impostos = float(input('Digite a porcentagem de impostos: '))
percentagem = float(input('Digite a percentagem do distribuidor: '))
# Processamento
custo_consumidor = custo_fabrica + (custo_fabrica * (percentagem/100)) + (custo_fabrica * (impostos/100))
# Saída
print(f'O custo ao consumidor será igual a R$ {custo_consumidor}')