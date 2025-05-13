


def principal():
 dinheiro = int(input('Digite o valor do saque: '))
 notas_50 = dinheiro // 50
 notas_10 = (dinheiro % 50) // 10
 notas_5 = ((dinheiro % 50 ) % 10) // 5
 notas_1 = ((dinheiro % 50 ) % 10) % 5 
 print(f'O valor de R${dinheiro} renderá {notas_50} notas de 50, {notas_10} notas de 10, {notas_5} notas de 5 e {notas_1} notas de 1')

principal()


