# Entrada
comprimento = int(input('Digite o comprimento da área: '))
altura = int(input('Digite a altura da área: '))
# Processamento
latas_tinta = comprimento / altura 
# Saída 
print(f'A quantidade de latas de tinta necessária para pintar essa área é {latas_tinta:.0f}')