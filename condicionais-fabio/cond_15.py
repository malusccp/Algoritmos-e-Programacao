from minha_funcoes import obter_numero_real
from minha_funcoes import obter_numero_inteiro

def main():
    print('Professor A:')
    hora_aula_A = obter_numero_real('Digite o valor de sua hora-aula(R$): ')

    print('Professor B:')
    hora_aula_B = obter_numero_real('Digite o valor de sua hora-aula(R$): ')
    quantidade_aulas = obter_numero_inteiro('Digite a quantidade de aulas: ')

    maior_salario(quantidade_aulas, hora_aula_A, hora_aula_B)


def salario_A(quantidade_aulas, hora_aula_A):
    return quantidade_aulas * hora_aula_A

def salario_B(quantidade_aulas, hora_aula_B):
    return quantidade_aulas * hora_aula_B

def maior_salario(quantidade_aulas, hora_aula_A, hora_aula_B):
   if salario_A(quantidade_aulas, hora_aula_A) > salario_B(quantidade_aulas, hora_aula_B):
       return print('O professor A possui o maior salário')
   else:
       return print('O professor B possui o maior salário')
       
main()