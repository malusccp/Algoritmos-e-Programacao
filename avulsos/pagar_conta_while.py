 

def main():
    saldo_devedor = 0 
    tempo = 0
    while saldo_devedor < 3000:
        saldo_devedor += 200
        tempo += 1
        juros = (saldo_devedor * (1 +0.85/100)** tempo) - 3000
        if saldo_devedor == 0:
         break 
    print(f'O número de meses para o pagamento equivale a {tempo} e foi cobrado um total de R${juros:.2f} em juros')

main()