# Leia um numero X e, a seguir, leia e escreva uma lista de números com o término da lista ocorrendo
# quando a soma de dois números consecutivos da lista for igual a X.

def main():
    X = int(input('Número: '))

    numero_anterior = 0
    for i in range(1000):
        soma = 0
        numero = int(input('Número: '))
        soma += numero + numero_anterior
        
        if soma == X: break

        numero_anterior = numero
main()




