# Entrada
minutos = int(input('Escreva o valor em minutos: '))

# Processamento
horas = minutos // 60
minutos_restantes = minutos % 60

# Saída
print(f'{minutos}min equivalem a {horas}h e {minutos_restantes}min')