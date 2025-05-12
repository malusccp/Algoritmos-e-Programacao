
# 11. Leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
# número. Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplos:
# o 326 = 3 centenas, 2 dezenas e 6 unidades
# o 12 = 1 dezena e 2 unidades

import utils

def main():
    numero = utils.get_intger_number('Digite um número: ')
    verificar(numero)

def verificar (numero):
    if numero <= 99:
        if dezena_dois(numero) <= 1 and unidade_dois(numero) >= 2:
         print(f'O {numero} = {dezena_dois(numero)} dezena e {unidade_dois(numero)} unidades ')
        if dezena_dois(numero) >= 2 and unidade_dois(numero) >= 2:
         print(f'O {numero} = {dezena_dois(numero)} dezenas e {unidade_dois(numero)} unidades ')
        if dezena_dois(numero) <= 1 and unidade_dois(numero) <= 1:
         print(f'O {numero} = {dezena_dois(numero)} dezena e {unidade_dois(numero)} unidade ')
        if dezena_dois(numero) >= 2 and unidade_dois(numero) <= 1:
         print(f'O {numero} = {dezena_dois(numero)} dezenas e {unidade_dois(numero)} unidade ')
    if numero > 99:
       if centena(numero) <= 1 and unidade_tres(numero) >= 2 and dezena_tres(numero) >= 2:
          print(f'O {numero} = {centena(numero)} centena, {dezena_tres(numero)} dezenas e {unidade_tres(numero)} unidades ')
       if centena(numero) >= 2 and unidade_tres(numero) <= 1 and dezena_tres(numero) >= 2:
          print(f'O {numero} = {centena(numero)} centenas, {dezena_tres(numero)} dezenas e {unidade_tres(numero)} unidade ')
       if centena(numero) >= 2 and unidade_tres(numero) <= 1 and dezena_tres(numero) <= 1:
          print(f'O {numero} = {centena(numero)} centenas, {dezena_tres(numero)} dezena e {unidade_tres(numero)} unidade ')
       if centena(numero) <= 1 and unidade_tres(numero) <= 1 and dezena_tres(numero) <= 1: 
         print(f'O {numero} = {centena(numero)} centena, {dezena_tres(numero)} dezena e {unidade_tres(numero)} unidade ')

def centena(numero):
    return (numero // 100) * (100)

def dezena_tres (numero):
    return ((numero % 100) // 10 )* (10)

def unidade_tres(numero):
  return (numero % 100) % 10 

def dezena_dois(numero):
    return (numero // 10) * (10)

def unidade_dois(numero):
    return numero % 10
    



main()