

def main():
    peso = float(input('Digite seu peso (kg): '))
    altura = float(input('Digite sua altura (m): '))
    imc = calcular_imc(peso, altura)
    classificar = niveis_imc(imc)

 

def calcular_imc(peso, altura):
    imc = peso/(altura)**2
    return imc
    

def niveis_imc(imc):
    if imc < 25:
        print(f'Seu imc é {imc: .1f} e seu peso está normal !')
    elif imc <= 30:
        print(f'CUIDADO. Seu imc é {imc: .1f} e você está com Obeso')
    else:
        print(f'CUIDADO. Seu imc é {imc: .1f} e você está com Obesidade mórbida')

main()