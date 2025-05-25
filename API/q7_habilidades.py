from q1_number_utils import get_integer_number_min
# TEMPO
# 25/05/2025
# INÍCIO: 15:12 FIM: 15:29
def main():
    entrada = get_integer_number_min('Digite o número de entradas: ', 0)
    contador = 0
    backend = 0
    frontend = 0
    mobile = 0
    total = 0
    dados = 0

    while contador < entrada:
        n, tipo = map(str, input('Digite sua escolha: ').split())
        n = int(n)

        contador += 1

        if tipo.upper() == 'B':
            backend += n
        elif tipo.upper() == 'F':
            frontend += n
        elif tipo.upper() == 'M':
            mobile += n
        elif tipo.upper() == 'D':
            dados += n

        total += n

    interface = f'''
Total: {total} alunos
Total de Backend: {backend} alunos
Total de Frontend: {frontend} alunos
Total de Mobile: {mobile} alunos
Total de Dados: {dados} alunos
Percentual de Backend: {backend/total:.2f} %
Percentual de Frontend: {frontend/total:.2f} %
Percentual de Mobile: {mobile/total:.2f} %
Percentual de Dados: {dados/total:.2f} %
'''
    print(interface)

main()


