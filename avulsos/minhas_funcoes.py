def ano_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def obter_numero_inteiro(label: str):
    return int(input(label))

def obter_numero_real(label: str):
    return float(input(label))

def obter_resposta(label: str):
    return str(input(label))


def eh_par(num):
    if num % 2 == 0:
        return print(f'O número {num} é par')
    else:
        return print(f'O número {num} é ímpar')
    
def horas_to_minutos(horas, minutos):
    return horas * 60 + minutos


def minutos_to_horasemin(minutos):
  minutos // 60 
  minutos % 60 
  return 