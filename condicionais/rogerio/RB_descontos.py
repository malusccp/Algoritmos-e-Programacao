
def main ():
    preço = float(input('Digite o valor do produto: '))
    vip = str(input('Você é cliente vip?(sim/não): '))
    aniversario = str(input('Hoje é seu aniversário?(sim/não): '))
    calcular_desconto(preço)
    calcular_desconto_adicional(vip, aniversario)
    calcular_preço_final(preço, vip, aniversario)


def calcular_desconto(preço):
    if preço > 500:
       return (0.15)
    elif preço >= 200:
        return  (0.10)
    else:
        return (0.05)

def calcular_desconto_adicional(vip, aniversario):
    desconto = 0
    if vip == 'sim':
        desconto += (0.05)
    if aniversario == 'sim':
        desconto += (0.03)
    return desconto

def calcular_preço_final (preço, vip, aniversario):
    desconto_base = calcular_desconto(preço)
    desconto_adicional = calcular_desconto_adicional(vip, aniversario)
    desconto_total = desconto_base + desconto_adicional
    preço_final = preço - (preço * desconto_total)


    print(f'O preço final a ser pago pelo produto é igual a R${preço_final: .2f}')

        
main()