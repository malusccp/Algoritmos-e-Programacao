from minha_funcoes import obter_numero_inteiro

def main():
 opcao = obter_numero_inteiro('Digite uma opção (1/2/3): ')
 num1 = obter_numero_inteiro('Digite o número : ')
 num2 = obter_numero_inteiro('Digite o número : ')
 num3 = obter_numero_inteiro('Digite o número : ')
 verificar_numero(opcao, num1, num2, num3)

def verificar_numero(opcao, num1, num2, num3):
 if opcao == 1:
  return print(f'O número escolhido é igual a {num1}')
 elif opcao == 2:
  return print(f'O número escolhido é igual a {num2}')
 elif opcao == 3:
  return print(f'O número escolhido é igual a {num3}')
 

main()
 