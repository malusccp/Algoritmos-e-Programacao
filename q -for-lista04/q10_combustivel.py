# 10. Calcule a quantidade de combustível que pode ser colocada em uma aeronave e verifique se a aeronave
# pode levantar vôo ou não. Considere os seguintes critérios:
# · O peso de decolagem da aeronave é sempre igual a 500.000 kg;
# · O peso de decolagem é composto pela soma do peso do combustível, do peso da carga, do peso dos
# passageiros;
# · O peso do combustível é a quantidade do combustível (em litros) multiplicada pelo fator 1.5kg/l;
# · A quantidade mínima de combustível para que a aeronave decole é de 10000 l;
# · O peso da carga é o somatório do peso dos “containers” de cargas em quilogramas.
# · O peso dos passageiros é o somatório do peso de cada passageiro e de todos os volumes da sua
# bagagem; cada passageiro tem o peso estimado de 70kg e cada volume de bagagem tem o peso
# estimado de 10kg.
# O algoritmo deve ler o números de containers e a seguir ler o peso de cada container. A seguir devem
# ser lidos os dados dos passageiros (número do bilhete, quantidade de bagagens) até que o número do
# bilhete seja igual a 0. Devem ser mostrados, a quantidade de passageiros, a quantidade total de volume
# de bagagem, o peso dos passageiros, o peso da carga, a quantidade possível de combustível, e uma
# mensagem indicando a liberação da decolagem ou não.

import utils 

def main():
    num_container = utils.get_integer_number_min('Número de containers: ', 0)
    peso_carga = 0
    for i in range(1, num_container+1, 1):
        peso_container = utils.get_decimal_number_min('Digite o peso do container: ', 0)
        peso_carga += peso_container

    # Dados dos passageiros:
    bagagem = 0
    passageiros = 0
    num_bilhete = utils.get_integer_number_min('Digite o número do bilhete (Para parar, digite 0): ', 0)
    qtd_bagagens = utils.get_integer_number_min('Digite o número de bagagens: ', 0)
    while not num_bilhete != 0:
        bagagem += qtd_bagagens
        passageiros += 1
        num_bilhete = utils.get_integer_number_min('Digite o número do bilhete (Para parar, digite 0): ', 0)
        qtd_bagagens = utils.get_integer_number_min('Digite o número de bagagens: ', 0)

    peso_total_combustivel = 1.5 * 10.000
    peso_passageiros = (num_bilhete * 70) + (bagagem * 10)
    peso_decolagem = peso_total_combustivel + peso_carga + peso_passageiros
    

    interface = f'''=== AERONAVE DO MEMPHIS DEPAY ===
> QUANTIDADE DE PASSAGEIROS: {passageiros} passageiros
> QUANTIDADE TOTAL DE VOLUME DE BAGAGENS: {bagagem} bagagens
> PESO DOS PASSAGEIROS: {peso_passageiros} kg
> PESO DA CARGA: {peso_carga} kg
> COMBUSTÍVEL: {peso_total_combustivel} L
> SITUAÇÃO DA DECOLAGEM: {validar_decolagem(peso_decolagem)}

    '''
    print(interface)

def validar_decolagem(peso_decolagem):
    if peso_decolagem <= 500.000:
        return 'DECOLAGEM LIBERADA'
    else:
        return f'DECOLAGEM NEGADA (O peso {peso_decolagem}kg não é permitido )'


main()