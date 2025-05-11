import utils

def main():
    letra = utils.obter_resposta('Digite uma letra: ')
    utils.linhas()
    verificar_letra(letra)
    utils.linhas()


def verificar_letra(letra: str):
   if letra == 'F' or letra == 'f':
       print("F - FEMININO")
   elif letra == 'M' or letra == 'm':
       print("M - MASCULINO")
   else:
     print("SEXO INVÁLIDO. Tente novamente")
     letra = utils.obter_resposta("Digite uma letra: ")
     verificar_letra(letra)



main()  