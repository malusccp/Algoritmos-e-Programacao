import utils 

def main():
    num_container = utils.get_integer_number_min('Número de containers: ', 0)
    contador = 0
    peso_carga = 0
    while contador < num_container:
        peso_container = utils.get_decimal_number_min('Digite o peso do container: ', 0)
        peso_carga += peso_container
        contador += 1

    # Dados dos passageiros:
    bagagem = 0
    passageiros = 0
    while True:
        num_bilhete = utils.get_integer_number_min('Digite o número do bilhete (Para parar, digite 0): ', 0)
        if num_bilhete == 0:
            break

        qtd_bagagens = utils.get_integer_number_min('Digite o número de bagagens: ', 0)
        bagagem += qtd_bagagens
        passageiros += 1

    peso_total_combustivel = 1.5 * 10.000
    peso_passageiros = (num_bilhete * 70) + (bagagem * 10)
    peso_decolagem = peso_total_combustivel + peso_carga + peso_passageiros
    

    interface = f'''=== AERONAVE DO MEMPHIS DEPAY ===
> QUANTIDADE DE PASSAGEIROS: {passageiros}
> QUANTIDADE TOTAL DE VOLUME DE BAGAGENS: {bagagem}
> PESO DOS PASSAGEIROS: {peso_passageiros}
> PESO DA CARGA: {peso_carga}
> COMBUSTÍVEL: {peso_total_combustivel}
> SITUAÇÃO DA DECOLAGEM: {validar_decolagem(peso_decolagem)}

    '''
    print(interface)

def validar_decolagem(peso_decolagem):
    if peso_decolagem <= 500.000:
        return 'DECOLAGEM LIBERADA'
    else:
        return f'DECOLAGEM NEGADA (O peso {peso_decolagem}kg não é permitido )'


main()