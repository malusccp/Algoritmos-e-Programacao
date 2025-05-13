import os

def obter_numero_inteiro(label: str):
    return int(input(label))

def obter_numero_real(label: str):
    return float(input(label))

def obter_resposta(label: str):
    return str(input(label))



def string(label: str):
 return str(input(label))



def get_integer_number(label):
  entrada = input(label)

  try:
    numero_a = int(entrada)
    return numero_a
  except ValueError:
    print('Valor Inteiro Inválido! ')
    return get_integer_number(label)


def get_integer_number_dif(label, forbidden_value):
  numero = get_integer_number(label)

  while numero == forbidden_value:
    print(f'Valor deve ser diferente de {forbidden_value}')
    numero = get_integer_number(label)
  
  return numero


def get_integer_number_min(label, min_value):
  numero = get_integer_number(label)

  while numero < min_value:
    print(f'Valor deve ser no mínimo {min_value}')
    numero = get_integer_number(label)
  
  return numero

def get_decimal_number_min(label, min_value):
  numero = get_decimal_number(label)

  while numero < min_value:
    print(f'Valor deve ser no mínimo {min_value}')
    numero = get_decimal_number(label)
  
  return numero


def get_integer_number_not_zero(label):
  numero = get_integer_number(label)

  while numero == 0:
    print(f'Valor deve ser diferente de 0')
    numero = get_integer_number(label)
  
  return numero


def get_integer_number_max(label, max_value):
  numero = get_integer_number(label)

  while numero > max_value:
    print(f'Valor deve ser no máximo {max_value}')
    numero = get_integer_number(label)
  
  return numero


def get_decimal_in_range(label: str, min_value: float, max_value: float):
  numero = get_decimal_number(label)

  while numero < min_value or numero > max_value:
    print(f'Valor fora da faixa ({min_value}-{max_value})')
    numero = get_decimal_number(label)
  
  return numero

def get_int_in_range(label: str, min_value: int, max_value: int):
  numero = get_integer_number(label)

  while numero < min_value or numero > max_value:
    print(f'Valor fora da faixa ({min_value}-{max_value})')
    numero = get_integer_number(label)
  
  return numero

def get_decimal_number(label: str):
  entrada = input(label)

  try:
    numero_a = float(entrada)
    return numero_a
  except ValueError:
    print('Valor decimal inválido!')
    numero_b = get_decimal_number(label)
    return numero_b


def limpar_tela():
  os.system('cls')

def linhas():
  return print("-" * 30)

def eh_par(num):
    if num % 2 == 0:
        return print(f'O número {num} é par')
    else:
        return print(f'O número {num} é ímpar')
    