# Entrada
segundo = int(input('Digite um número inteiro de segundos: '))

# Processamento 
horas = segundo // 3600
resto = segundo % 3600
minutos = resto // 60
segundos = resto % 60 

# Saída
print(f'O valor de {segundo}s equivale a {horas}h, {minutos}min e {segundos}s')