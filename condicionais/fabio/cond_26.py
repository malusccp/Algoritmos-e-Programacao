from minha_funcoes import obter_numero_inteiro

def main():
    a = obter_numero_inteiro('Digite um lado do triângulo: ')
    b = obter_numero_inteiro('Digite um lado do triângulo: ')
    c = obter_numero_inteiro('Digite um lado do triângulo: ')
    encontrar_hipotenusa(a,b,c)


def encontrar_hipotenusa(a,b,c):
    if a > b and a > c:
        return print(f'O lado {a} é a hipotenusa e {b} e {c} são os catetos')
    if b > a and b > c:
        return print(f'O lado {b} é a hipotenusa e {a} e {c} são os catetos')
    if c > a and c > b:
        return print(f'O lado {c} é a hipotenusa e {a} e {b} são os catetos')
    
main()
