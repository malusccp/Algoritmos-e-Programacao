# Entrada 
anos_fuma = int(input('Insira a quantos anos fuma: '))
cigarro_dia = int(input('Insira de cigarro que fuma por dia: '))
preço_carteira = float(input('Insira o preço de uma carteira de cigarros: '))
# Processamento 
dias_fuma = anos_fuma * 365
cigarro_ano = cigarro_dia * dias_fuma
preço_unid = preço_carteira / 20
gasto_total = cigarro_ano * preço_unid
# Saída
print(f'>>>> O valor que o fumante gastou é igual a {gasto_total}')

