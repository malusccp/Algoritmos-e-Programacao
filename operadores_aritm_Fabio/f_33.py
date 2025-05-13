# Entrada
numero = int(input('Digite o número desejado: '))

# Processamento
centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 100) % 10

inverso = (unidade * 100) + (dezena * 10) + centena

soma = numero + inverso
#Saída
print(f'O número {numero} quando invertido é igual a {inverso} e a soma entre eles é igual a {soma}')