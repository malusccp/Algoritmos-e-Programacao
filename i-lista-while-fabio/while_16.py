import uteis 

def main():
    qntd_num = uteis.get_integer_number_min("Escreva a quantidade de termos da sequência: ", 2)
    uteis.linhas()
    print(f"Os primeiros {qntd_num} termos da sequência de Fibonacci são:")
    escrever_sequencia_fibonacci(qntd_num)

def escrever_sequencia_fibonacci(qntd_num: int):
    contador = 2
    numero_a = 0
    numero_b = 1
    print(numero_a)
    print(numero_b)
    while qntd_num > contador:
        soma = numero_a + numero_b
        numero_a = numero_b
        numero_b = soma
        contador += 1
        print(f'{soma}')


       
    uteis.linhas()

main()