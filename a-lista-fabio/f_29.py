# Entrada
meses = int(input('Digite um número inteiro de meses: '))

# Processamento 
anos = meses // 12
meses_2 = meses % 12


# Saída
print(f'O valor de {meses} meses equivale a {anos} anos e {meses_2} meses')