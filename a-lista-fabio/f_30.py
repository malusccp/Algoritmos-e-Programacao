def converter_minutos (minutos):
    dias = minutos // 1440
    resto = minutos % 1440
    horas = resto // 60
    minutos = resto % 60
    return dias, horas, minutos

minutos = int(input('Digite um número inteiro em minutos: '))

dias, horas, minutos = converter_minutos (minutos) 
print(f'O valor de {minutos} equivale a {dias} dias, {horas}h e {minutos}min')