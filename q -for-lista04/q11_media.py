# 11. Leia informações de alunos (matrícula, nota1, nota2, nota3) com o fim das informações indicado por
# matrícula = 0. Para cada aluno deve ser calculada a média final de acordo com a seguinte fórmula:

# Média Final = (2 * nota1) + (3 * nota2) + (5 * nota3)/10

# Se a média final for igual ou superior a 7, o aluno está aprovado; se a média final for inferior a 7, o
# aluno está reprovado. Ao final devem ser mostrados o total de aprovados, o total de reprovados e o total
# de alunos da turma.
import utils

def main():
    total_alunos = 0
    aprovados = 0
    reprovados = 0
    for i in range(999999999999999):
        matricula = utils.get_integer_number_min('Matrícula do aluno: ', 0)
        if matricula == 0: break
        else:
            nota1 = utils.get_decimal_in_range('Nota 1: ', 0, 10)
            nota2 = utils.get_decimal_in_range('Nota 2: ', 0, 10)
            nota3 = utils.get_decimal_in_range('Nota 3: ', 0, 10)

            media_final = ((2 * nota1) + (3 * nota2) + (5 * nota3))/ 10

            if media_final >= 7:
                aprovados += 1
            elif media_final < 7:
                reprovados += 1
            total_alunos += 1

    interface = f'''=== SITUAÇÃO DOS ALUNOS DE ADS ===
    > APROVADOS: {aprovados} alunos
    > REPROVADOS: {reprovados} alunos
    > TOTAL DE ALUNOS: {total_alunos} alunos
    '''
    print(interface)

main()