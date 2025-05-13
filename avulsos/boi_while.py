from minhas_funcoes import obter_numero_inteiro
from minhas_funcoes import obter_numero_real
def main():
    boi_mais_magro_id = 0
    boi_mais_magro_peso = 0
    boi_mais_gordo_id = 0
    boi_mais_gordo_peso = 0
    
    while True:
     id_boi = obter_numero_inteiro('Digite o número de identificação do boi: ')
     if id_boi == 0:
      break 
     peso_boi = obter_numero_real('Digite o peso do boi: ')

     if boi_mais_magro_id == 0 or peso_boi < boi_mais_magro_peso:
       boi_mais_magro_peso = peso_boi
       boi_mais_magro_id = id_boi
     if peso_boi > boi_mais_gordo_peso:
       boi_mais_gordo_peso = peso_boi
       boi_mais_gordo_id = id_boi

       
    print(f'O boi mais magro é o de ID {boi_mais_magro_id} e peso {boi_mais_magro_peso} ')
    print(f'O boi mais gordo é o de ID {boi_mais_gordo_id} e peso {boi_mais_gordo_peso} ')

main()