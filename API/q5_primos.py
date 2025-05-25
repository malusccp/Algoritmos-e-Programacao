from q1_number_utils import get_integer_number_min
# TEMPO 
# INÍCIO 15:10 FIM: 15:36

def main():
    n = get_integer_number_min('Escreva um número de início: ', 0)
    m = get_integer_number_min('Escreva um número de fim: ', n+1)
    atual = n
    while atual <= m:
        divisores = 0
        verificador = 1
        while verificador <= atual:
            if atual % verificador == 0:
                divisores += 1
            verificador += 1
        if divisores == 2:
            print(atual)
        atual += 1
        
main()