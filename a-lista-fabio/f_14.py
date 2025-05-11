# Entrada 
nota1 = float(input('Insira a primeira nota '))
peso1 = int(input('Insira o peso da primeira nota '))
nota2 = float(input('Insira a segunda nota '))
peso2 = int(input('Insira o peso da segunda nota '))
nota3 = float(input('Insira a terceira nota '))
peso3 = int(input('Insira o peso da terceira nota '))
# Processamento 
media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

# Saída
print(f'>>>> Portanto a media ponderada das notas do aluno equivale a {media_ponderada}')