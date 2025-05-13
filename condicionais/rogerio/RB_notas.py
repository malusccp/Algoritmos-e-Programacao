


def main():
    nota1 = float(input('Digite a primeira nota do aluno:'))
    nota2 = float(input('Digite a segunda nota do aluno:'))
    nota3 = float(input('Digite a terceira nota do aluno:'))
    media = calcular_media(nota1, nota2, nota3)
    if nota1 == 0 or nota2 == 0 or nota3 == 0:
        print('Você está reprovado.')
    else: 
        situacao_aluno(media)


def calcular_media(nota1, nota2, nota3):
   media = (nota1 + nota2 + nota3) / 3
   return media

def situacao_aluno(media):
    if media >= 7:
        print('Parabéns!! Você foi aprovado.')
    elif media >= 5:
        print('Você está de recuperação.')
    else:
        print('Você está reprovado.')


    
main()