import utils

def main():
    letra = utils.obter_resposta('Digite uma letra: ')
    utils.linhas()
    verificar_letra(letra)
    utils.linhas()


def verificar_letra(letra: str):
   if letra == "A" or letra == 'a' or letra == 'E' or letra == 'e' or letra == 'i' or letra == 'I' or letra == 'o' or letra == 'O' or letra == 'U' or letra == 'u':
      print(f"A letra '{letra}' é vogal") 
   else:
     print(f"A letra '{letra}' é consoante")



main()  