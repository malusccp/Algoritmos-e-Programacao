

def main():
    peso = float(input('Digite seu peso (kg): '))
    altura = float(input('Digite sua altura (m): '))
    imc = calcular_imc(peso, altura)
    classificar = niveis_imc(imc)

 

def calcular_imc(peso, altura):
    imc = peso/(altura)**2
    return imc
    

def niveis_imc(imc):
    if imc < 18.5:
        print(f'CUIDADO. Seu imc é {imc: .1f} e você está abaixo do peso!')
    elif imc <= 24.9:
        print(f'Seu imc é {imc: .1f} e seu peso está normal !')
    elif imc <= 34.9:
        print(f'CUIDADO. Seu imc é {imc: .1f} e você está com Obesidade grau 1')
    elif imc <= 39.9:
        print(f'CUIDADO. Seu imc é {imc: .1f} e você está com Obesidade grau 2')
    else:
        print(f'CUIDADO. Seu imc é {imc: .1f} e você está com Obesidade grau 3')





main()