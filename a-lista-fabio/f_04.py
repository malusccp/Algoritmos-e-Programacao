# 04. Leia o valor do dólar e um valor em dólar, calcule e escreva o equivalente em real (R$) 

#Entrada 
dolar_hoje = float(input('Cotação do dólar hoje: '))
dolar = float(input('Dólar: '))

#Processamento
reais = dolar * dolar_hoje

# Saída 
print(f'{dolar} dólares equivalem a {reais:.2f} reais')