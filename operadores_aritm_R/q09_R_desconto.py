# Entrada
valor_inicial = int(input('Digite o preço inicial: '))
desconto = int(input('Digite o desconto: '))
# Processamento
valor_desconto = valor_inicial * (1-(desconto/100))
# Saída 
print(f'Logo, o valor de R${valor_inicial} quando aplicado um desconto de {desconto}% passa a custar R${valor_desconto}')