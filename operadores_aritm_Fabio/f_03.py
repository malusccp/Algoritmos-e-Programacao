# 03 Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos.

#Entrada
Minutos = int(input('Minutos: '))

#Processamento 
Horas = Minutos // 60 
Minutos_restantes = Minutos % 60  
#Saida
print(f'>>> {Minutos} minutos equivalem a {Horas}h e {Minutos_restantes}min')