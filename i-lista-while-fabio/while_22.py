import uteis 

def main():
    n = uteis.get_integer_number_min("Escreva a quantidade de bois: ", 0)
    uteis.linhas()
    identificar_boi(n)


def identificar_boi(n: int):
    contador = 0
    boi_mais_gordo = None
    numero_boi_gordo = 0
    boi_mais_magro = None
    numero_boi_magro = 0
    while contador < n:
        numero_boi = uteis.get_integer_number_min("Escreva o número de identificação do boi: ", 0)
        peso_boi = uteis.get_integer_number_min("Escreva o peso (kg) do boi: ", 1)
        contador += 1

        if boi_mais_gordo == None or peso_boi > boi_mais_gordo:
            boi_mais_gordo = peso_boi
            numero_boi_gordo = numero_boi


        if boi_mais_magro == None or peso_boi < boi_mais_gordo :
            boi_mais_magro = peso_boi
            numero_boi_magro = numero_boi


    print(f"N° de Identificação do boi mais gordo: {numero_boi_gordo}\nPeso boi mais gordo: {boi_mais_gordo} ")
    uteis.linhas()
    print(f"N° de Identificação do boi mais magro: {numero_boi_magro}\nPeso boi mais magro: {boi_mais_magro} ")
    uteis.linhas()


main()