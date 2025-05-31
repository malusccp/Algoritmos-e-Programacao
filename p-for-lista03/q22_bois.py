import utils

def main():
    fichas = utils.get_integer_number_min('Fichas: ', 0)

    peso_boi_magro = None
    peso_boi_gordo =  None 
    numero_boi_gordo = 0
    numero_boi_magro = 0
    for i in range(1, fichas+1):
        numero_identif = utils.get_integer_number_min('N° Identificação do Boi: ', 0)
        peso_boi = utils.get_integer_number_min('Peso Boi (kg): ', 0)

        if (peso_boi_gordo == None) or (peso_boi > peso_boi_gordo): 
            peso_boi_gordo = peso_boi
            numero_boi_gordo = numero_identif
        if (peso_boi_magro == None) or (peso_boi < peso_boi_magro):
            peso_boi_magro = peso_boi
            numero_boi_magro = numero_identif



    utils.linhas()
    print(f'N° BOI MAIS GORDO: {numero_boi_gordo}\nPESO BOI MAIS GORDO: {peso_boi_gordo} kg\nN° BOI MAIS MAGRO: {numero_boi_magro}\nPESO BOI MAIS MAGRO: {peso_boi_magro} kg')
    utils.linhas()

main()