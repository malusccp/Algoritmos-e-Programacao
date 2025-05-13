# FUNÇÃO CDB
def CDB(valor_investido, taxa_anual, tempo_anos):
    montante_CDB = valor_investido * (1 + taxa_anual / 100) ** tempo_anos
    return montante_CDB
# FUNÇÃO CDC
def CDC(valor_emprestado, taxa_mensal, tempo_meses):
  montante_CDC = valor_emprestado * (1 + taxa_mensal / 100) ** tempo_meses
  parcelas_CDC = montante_CDC / tempo_meses 
  juros_emprestimo = montante_CDC - valor_emprestado
  return montante_CDC, parcelas_CDC, juros_emprestimo
# SIMULADOR CDB
print('SIMULADOR CDB')
valor_investido = float(input('Digite o valor a ser investido em R$: '))
taxa_anual = float(input('Digite a taxa de juros ao ano em %: '))
tempo_anos = int(input('Digite o tempo em anos: '))
montante_CDB = CDB(valor_investido, taxa_anual, tempo_anos)
print(f'O montante do investimento será igual a R${montante_CDB: .2f}')
# SIMULADOR CDC
print('SIMULADOR CDC')
valor_emprestado = valor_investido
taxa_mensal = float(input('Digite a taxa de juros mensal em %: '))
tempo_meses = int(input('Digite o tempo em meses: '))
montante_CDC, parcelas_CDC, juro_emprestimo = CDC(valor_emprestado, taxa_mensal, tempo_meses)
print(f'O montante do empréstimo será igual a R${montante_CDC: .2f}')
print(f'O cliente irá pagar ao banco correspondente a juros um total de R${juro_emprestimo: .2f}')
print(f'Cada parcela corresponderá a um valor de R${parcelas_CDC: .2f}')
# Lucro do Banco
print('LUCRO DO BANCO')
juro_investidores = montante_CDB - valor_investido
lucro_banco = juro_emprestimo - juro_investidores
print(f'O lucro do banco será igual a R${lucro_banco: .2f}')
