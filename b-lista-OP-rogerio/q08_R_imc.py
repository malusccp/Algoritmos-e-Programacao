# Entrada 
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
# Processamento 
imc = peso / altura ** 2 
# Saída
print(f'O IMC é igual a {imc:.2f}')