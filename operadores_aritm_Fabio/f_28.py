# Entrada
horas = int(input('Digite um número inteiro de horas: '))

# Processamento 
semana = horas // 168
resto = horas % 168
dias = resto // 24
horas_2 = resto % 24

# Saída
print(f'O valor de {horas}h equivale a {semana} semanas, {dias}dias e {horas_2}h')