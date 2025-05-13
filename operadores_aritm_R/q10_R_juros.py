# Entrada
capital = int(input('Insira o valor do capital: '))
taxa_de_juros = float(input('Insira o valor do juros: '))
tempo = int(input('Insira o valor do tempo: '))
# Processamento
montante = capital * (1 + taxa_de_juros * tempo)
# Saída
print(f'O valor do montante final será R${montante}')
