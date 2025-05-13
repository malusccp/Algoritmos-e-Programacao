# Entrada
numero = int(input('Digite o número binário desejado: '))

# Processamento
milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = ((numero % 1000) % 100) // 10
unidade = ((numero % 100) % 100) % 10


decimal = (milhar * 2**3) + (centena * 2**2) + (dezena * 2**1) + (unidade * 2**0)
#Saída
print(f'O número binário {numero} quando convertido em base decimal é igual a {decimal} ')