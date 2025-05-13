from minhas_funcoes import obter_numero_inteiro
from minhas_funcoes import obter_resposta


def main():
    idade = obter_numero_inteiro('Digite a sua idade: ')
    convite = obter_resposta('Você possui convite?: ')
    nome_lista = obter_resposta('Você possui o nome na lista?: ')
    verificar_entrada(idade, convite, nome_lista)


def verificar_entrada(idade, convite, nome_lista):
   if verificar_nome_lista(nome_lista) and verificar_idade(idade) and verificar_convite(convite):
      print('Entrada liberada. Aproveite!')
   else:
      if not verificar_idade(idade):
         print('Entrada negada: Menor de idade')
      if not verificar_nome_lista(nome_lista):
         print('Entrada negada: Nome não consta na lista')
      if not verificar_convite(convite):
         print('Entrada negada: Não possui convite ')


def verificar_idade(idade):
   if idade > 18:
      return True
   

def verificar_convite(convite):
   if convite == 'sim' or convite == 'Sim':
      return True


def verificar_nome_lista(nome_lista):
   if nome_lista == 'sim' or nome_lista =='Sim':
      return True
   

main()
    
