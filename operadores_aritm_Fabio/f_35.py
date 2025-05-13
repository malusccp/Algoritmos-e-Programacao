# Entrada
numero = int(input('Digite um número inteiro de 4 dígitos: '))

# Processamento
milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = ((numero % 1000) % 100) // 10
unidade = ((numero % 100) % 100) % 10

soma_numero = milhar + centena + dezena + unidade

# Saída
print(f'A soma dos elementos do número {numero} é igual a {soma_numero}')