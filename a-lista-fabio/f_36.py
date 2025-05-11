# Entrada
idade_anos = int(input('Digite a idade em anos: '))
idade_meses = int(input('Digite a idade em meses: '))
idade_dias = int(input('Digite a idade em dias: '))
# Processamento
dias = idade_anos * 365 + idade_meses * 30 + idade_dias
# Saída
print(f'A idade quando convertida equivale a {dias} dias')