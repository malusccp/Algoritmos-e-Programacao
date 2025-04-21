from minha_funcoes import obter_numero_inteiro
from minha_funcoes import horas_to_minutos

def main():
    hora_inicio = obter_numero_inteiro('Digite a hora que começou o jogo: ')
    min_inicio = obter_numero_inteiro('Digite os minutos em relação ao horário que começou o jogo: ')
    hora_final = obter_numero_inteiro('Digite a hora que acabou o jogo: ')
    min_final = obter_numero_inteiro('Digite os minutos em relação ao horário que acabou o jogo: ')
    inicio_total_min = horas_to_minutos(hora_inicio, min_inicio)
    final_total_min = horas_to_minutos(hora_final, min_final)
    duracao_min = validar_tempo(inicio_total_min, final_total_min)
    minutos_to_horasemin(duracao_min)



def validar_tempo(inicio_total_min, final_total_min):
   if final_total_min < inicio_total_min:
      return (24 * 60 - inicio_total_min) + final_total_min
   elif final_total_min == inicio_total_min:
      return 24 * 60
   else:
      return final_total_min - inicio_total_min


def minutos_to_horasemin(duracao_min):
  duracao_min // 60 
  duracao_min % 60 
  return print(f'A duração do jogo é igual a {duracao_min//60}h e {duracao_min % 60}min')

main()