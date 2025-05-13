# Entrada
idade_dias = int(input('Digite a idade em dias: '))
# Processamento
idade_anos = idade_dias // 365
idade_meses = (idade_dias % 365) // 30
idade_dias2 = (idade_dias % 365) % 30
# Saída
print(f'A idade de {idade_dias} dias quando convertida equivale a {idade_anos} anos, {idade_meses} meses e {idade_dias2} dias')