import utils


def main():
    contador = 0
    maior_nota = 0
    menor_nota = -1
    soma_das_nota = 0
    qtd_masc = 0
    qtd_fem = 0
    nota_fem = 0
    nota_masc = 0


    while True:
     sexo = utils.string('Digite seu sexo (MASCULINO = M | FEMININO = F): ')
     if sexo != 'M' and sexo != 'F' :
        break
     nota = utils.get_intnumber_range('Digite a sua nota: ', 1, 10)

     
     if sexo == 'M':
        qtd_masc += 1
        nota_masc += nota
     if sexo == 'F':
        qtd_fem += 1
        nota_fem += nota
    

     if nota > maior_nota:
        maior_nota = nota
     if nota < menor_nota:
        menor_nota = nota
     contador += 1
     soma_das_nota += nota

    
    media_turma = soma_das_nota/(qtd_fem+qtd_masc)
    media_mulher = nota_fem/qtd_fem
    media_homem = nota_masc/qtd_masc
    print(f'''               ==== RESULTADO ====
            > QUANTIDADES DE ALUNOS DA TURMA: {qtd_masc + qtd_fem}
            > ALUNOS DO SEXO MASCULINO: {qtd_masc}
            > ALUNOS DO SEXO FEMININO: {qtd_fem}
            > DESEMPENHO DA TURMA: {escala_notas(media_turma)}
            > DESEMPENHO DAS MULHERES: {escala_notas(media_mulher)}
            > DESEMPENHO DOS HOMENS: {escala_notas(media_homem)}
''')
 
   
def escala_notas(media: float):
   if media <= 2:
      return 'Péssimo'
   elif media <= 4:
       return "Ruim"
   elif media < 7:
       return "Regular"
   elif media < 8:
       return "Bom"
   elif media <= 10:
       return "Excelente"
      
   
main()