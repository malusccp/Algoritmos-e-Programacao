# 2. Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.

#Entrada
Horas = int(input('Horas: '))
Minutos = int(input('Minutos: '))

#Processamento
minutos_convert = Horas * 60 + Minutos

#Saida
print (f'>>{Horas}h e {Minutos}min convertidos para minutos correspondem a {minutos_convert} minutos')