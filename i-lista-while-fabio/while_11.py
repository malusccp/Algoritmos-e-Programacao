import uteis


def main():
    limite_inferior = uteis.get_integer_number_min("Escreva o limite inferior: ", 0)
    limite_superior = uteis.get_integer_number_min("Escreva o limite superior: ", limite_inferior+1)
    uteis.linhas()
    print(f"Os algarismos primos dentro do intervalo de ({limite_inferior} - {limite_superior}) são iguais a: ")
    primos_entre_limites(limite_inferior, limite_superior)
    uteis.linhas()

def primos_entre_limites(limite_inferior: int, limite_superior: int):
    numero = limite_inferior
    while numero <= limite_superior:
        eh_primo(numero)
        numero += 1


def eh_primo(numero: int):
   if numero <= 1:
      return False
   for i in range (2, int(numero ** 0.5 ) + 1):
      if numero % i == 0:
         return False
   return print(numero)


main()