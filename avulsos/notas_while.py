from minhas_funcoes import obter_numero_inteiro
from minhas_funcoes import obter_numero_real

def main():
    matricula = 0
    alunos_aprovados = 0
    alunos_reprovados = 0
    total_de_alunos = 0

    while True:
        matricula = obter_numero_inteiro('Digite a matrícula do aluno: ')
        if matricula == 0:
            break
        nota1 = obter_numero_real('Digite a nota 1 do aluno: ')
        nota2 = obter_numero_real('Digite a nota 2 do aluno: ')
        nota3 = obter_numero_real('Digite a nota 3 do aluno: ')
        media_final = ((2*nota1) + (3*nota2) + (5*nota3))/10
        if media_final >= 7:
            alunos_aprovados += 1
            total_de_alunos += 1
        if media_final < 7:
            alunos_reprovados += 1
            total_de_alunos += 1
    print(f'O total de alunos da turma é {total_de_alunos}')
    print(f'O total de alunos aprovados é {alunos_aprovados}')
    print(f'O total de alunos reprovados é {alunos_reprovados}')

main()