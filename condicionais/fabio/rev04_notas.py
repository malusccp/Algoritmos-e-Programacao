# Leia 2 (duas) notas parciais de um aluno, calcule a média e escreva a mensagem:
# o "Aprovado", se a média alcançada for maior ou igual a sete;
#o "Reprovado", se a média for menor do que sete;
#o "Aprovado com Distinção", se a média for igual a dez.

import utils

print("==== CALCULADORA DE APROVAÇÃO (OU NÃO) ====")
def main():
    nota1 = utils.get_decimal_in_range("Nota 1: ", 0, 10)
    nota2 = utils.get_decimal_in_range("Nota 2: ", 0, 10)
    utils.linhas()
    media = media_notas(nota1, nota2)
    verificar_aprovacao(media)
    utils.linhas()


def media_notas(nota1, nota2):
    media = (nota1 + nota2)/2
    return media

def verificar_aprovacao(media):
    if media >= 7 and media != 10:
        print("Você foi aprovado")
    if media == 10:
        print("Você foi aprovado com distinção")
    if media < 7:
        print("Você foi reprovado")

main()