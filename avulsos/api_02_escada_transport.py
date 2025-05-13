#O aumento ou perda de peso, de forma
#simplificada, é um o resultado da balança entre superávit ou déficit
#calórico. Se consumir mais do que precisa, aumenta o peso, caso
#contrário diminui ou mantém.
#De acordo com a OMS, um homem adulto em média precisa
#consumir apenas 2400 calorias/dia para manter o peso atual. Já
#as mulheres ficam em 2000 calorias. Ou seja, esse é o valor que
#gastamos em atividades do dia a dia, normais. Já para perder 1kg
#de peso é necessário o gasto calórico excedente de 7000 calorias.
#Na academia, temos uma série de exercícios do tipo aeróbico,
#dentre eles o Transport e Simulador de Escada. No Transport, um
#homem gasta em média 100 calorias a cada 5 min, já uma mulher
#a cada 6 min. E na escada, um homem gasta 100 calorias a cada
#7 minutos e a mulher a cada 8 minutos.
#Considerando as informações acima como verdade (informações
#hipotéticas), e que o ritmo alimentar permanecerá o mesmo.
#Faça um programa para auxiliar na perda de peso de homens e
#mulheres adultos. O objetivo é, de acordo com a situação atual
#(peso atual, se homem ou mulher, quantos quilos quer perder,
#quantos dias por semana irá fazer atividade física, e quanto tempo
#por dia irá treinar). Pergunte ainda qual proporção (%) de tempo
#alocada para o Transport, e calcule a contrapartida de Escada (os
#dois serão 100%).
#Seu objetivo, ao final, é informar em quantas semanas o usuário
#alcançará o objeto desejado, bem como indicar para cada dia de
#atividade física, quantos minutos de escada e quantos de
#Transport ele deverá seguir (todos os dias são iguais). Faça as
#validações adequadas.

def main():
    print('========== CALCULADORA DE TREINO BY MALU E THEUS S2 ==========')
    print('PS: MENÇÃO HONROSA PARA XAMÃ S2')
    peso_atual = float(input("Digite o seu peso atual (kg):"))
    sexo = int(input("Digite seu sexo (MASCULINO = 0 | FEMININO = 1): "))
    perda = float(input("Quantos quilos vocÊ deseja perder?: "))
    dias_por_semana = int(input("Quantos dias por semana irá treinar?: "))
    tempo_por_dia = int(input("Quantas horas por dia irá treinar?: ")) * 60

    proporcao_transport = int(input("Qual a proporção de tempo dedicada ao Transport?: "))/100
    proporcao_escada = 1 - proporcao_transport

    tempo_por_dia_transport = tempo_por_dia * proporcao_transport
    tempo_por_dia_escada = tempo_por_dia * proporcao_escada

    gastar = perda * 7000

    if sexo == 0:
        cal_transport = tempo_por_dia_transport * 100 // 5
        cal_escada = tempo_por_dia_escada * 100 // 7
    else: 
        cal_transport = tempo_por_dia_transport * 100 // 6
        cal_escada = tempo_por_dia_escada * 100 // 8


    gasto_total_dia = cal_transport + cal_escada
     
 
    dias = 0
    
    gasto_necessario_exceder = 0
    if sexo == 0:
        gasto_necessario_exceder = 2400
    else:
        gasto_necessario_exceder += 2000
    
    if gasto_total_dia < gasto_necessario_exceder:
        print("Olha... com esse tempo de treino é mais fácil bater laje e peneirar brita... treina mais pow")
    
    else:
        while gastar > 0:
            gastar += gasto_necessario_exceder
            gastar -= gasto_total_dia 
            dias += 1

        semanas = dias // dias_por_semana
        print(f''' ========== RESULTADO DO TREINO ==========
                    > SEMANAS ATÉ ALCANÇAR O RESULTADO: {semanas}
                    > MINUTOS DE TRANSPORTE POR DIA: {tempo_por_dia_transport: .0f}
                    > MINUTOS DE ESCADA POR DIA: {tempo_por_dia_escada: .0f}
            
        ''')

    

main()
    



    





    

