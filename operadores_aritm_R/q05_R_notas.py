# Entrada 
valor_dinheiro = int(input('Escreva o valor desejado em reais: '))
# Processamento
notas_50 = valor_dinheiro // 50
notas_10 = valor_dinheiro % 50
#Saída 
print(f'O valor de {valor_dinheiro} reais equivale a {notas_50} de 50.00 e {notas_10} de 10.00 reais')