
def main():
    temperatura = float(input('Insira a temperatura a ser convertida: '))
    unidade_temperatura = str(input('Insira a unidade da temperatura escolhida(C/F/K): '))
    unidade_conversao = str(input('Insira para qual unidade deseja converter a temperatura(C/F/K): '))
    if unidade_temperatura == (('C' or 'c') and temperatura >= -273.15) or (unidade_temperatura == ('K' or 'k') and temperatura >= 0) or unidade_temperatura == ('F' or 'f'):
      conversao_temp(temperatura, unidade_temperatura, unidade_conversao)
      print(f'A temperatura de {temperatura} {unidade_temperatura} quando convertida para {unidade_conversao} equivale a {conversao_temp(temperatura, unidade_temperatura, unidade_conversao)}')
    else:
       print('O valor da temperatura não é válido. Tente novamente')
       main()

def conversao_temp(temperatura, unidade_temperatura, unidade_conversao):
    if unidade_temperatura == celsius() and unidade_conversao == kelvin():
        return celsius_to_kelvin(temperatura)
    elif unidade_temperatura == celsius() and unidade_conversao == fahrenheit():
        return celsius_to_fahrenheit(temperatura)
    elif unidade_temperatura == kelvin() and unidade_conversao == celsius():
        return kelvin_to_celsius(temperatura)
    elif unidade_temperatura == kelvin() and unidade_conversao == fahrenheit():
        return kelvin_to_fahrenheit(temperatura)
    elif unidade_temperatura == fahrenheit() and unidade_conversao == celsius():
        return fahrenheit_to_celsius(temperatura)
    elif unidade_temperatura == fahrenheit() and unidade_conversao == kelvin():
        return fahrenheit_to_kelvin(temperatura)


def celsius():
    return ('C' or 'c')



def kelvin():
    return ('K' or 'k')


def fahrenheit():
    return ('F' or 'f')


def celsius_to_kelvin(temperatura: float):
    return temperatura + 273.15



def celsius_to_fahrenheit(temperatura):
    return (temperatura * 1.8) + 32


def kelvin_to_celsius(temperatura):
    return temperatura - 273 


def kelvin_to_fahrenheit(temperatura):
    return (temperatura - 273) * 1.8 + 32


def fahrenheit_to_celsius(temperatura):
    return (temperatura - 32)/1.8


def fahrenheit_to_kelvin(temperatura):
    return (temperatura -32) * 5/9 + 273




    

main()
