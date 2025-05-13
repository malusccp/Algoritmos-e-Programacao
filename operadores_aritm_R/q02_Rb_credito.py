


def main():
# Entrada
 valor_fatura = float(input('Digite o valor da fatura: '))
 pagamento1 = float(input('Digite o valor do pagamento1: '))
 pagamento2 = float(input('Digite o valor do pagamento2: '))
 meses1 = int(input('Digite o tempo até o próximo pagamento1: '))
 meses2 = int(input('Digite o tempo até o próximo pagamento2: '))
 print(f'O valor da fatura P1 de R${valor_fatura} gerou uma dívida de {calcular_fatura(valor_fatura, pagamento1, meses1): .2f}')
 print(f'O valor da fatura P2 de R$ {valor_fatura} gerou uma dívida de {calcular_fatura(valor_fatura, pagamento2, meses2): .2f}')
 print (f'O crescimento percentual em P1 foi de {crescimento(calcular_fatura(valor_fatura, pagamento1, meses1), valor_fatura, pagamento1): .2f} %')
 print (f'O crescimento percentual em P2 foi de {crescimento(calcular_fatura(valor_fatura, pagamento2, meses2), valor_fatura, pagamento2): .2f} %')


def calcular_fatura (valor_fatura, pagamento, meses):
 saldo_devedor = valor_fatura - pagamento
 juros_rotativo = saldo_devedor * (1+0.12)**meses - saldo_devedor
 juros_mora = saldo_devedor * (1+0.01)**meses - saldo_devedor
 multa = saldo_devedor * 0.02
 saldo_final = saldo_devedor + juros_mora + multa + juros_rotativo
 return saldo_final
 
 
def crescimento(saldo_devedor, valor_fatura, pagamento):
 crescimento = ((saldo_devedor - (valor_fatura - pagamento)) / (valor_fatura - pagamento)) * 100
 return crescimento

main ()