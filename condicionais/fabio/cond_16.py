
from minha_funcoes import obter_numero_real

def main():
    nota1 = float(input('Digite a primeira nota do aluno:'))
    nota2 = float(input('Digite a segunda nota do aluno:'))
    media_inicial = calcular_media_inicial(nota1, nota2) 
    if media_inicial >= 7:
       return print('Parabéns!! Você foi aprovado.')
    if not media_inicial >= 7:
      nota_final = nota_exame_final()
      media_final = calcular_media_final(nota1, nota2, nota_final)
    if media_final >= 5:
       return print('Parabéns!! Você foi aprovado.')
    else:
       return print('Você foi reprovado.')

def calcular_media_inicial(nota1, nota2):
   media_inicial = (nota1 + nota2) / 2
   return media_inicial
        

def nota_exame_final():
 return obter_numero_real('Digite a nota do exame final: ')

def calcular_media_final(nota1, nota2, nota_exame_final):
   return (nota1 + nota2 + nota_exame_final)/3

main()