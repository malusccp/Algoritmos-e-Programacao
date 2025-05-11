# Entrada 
numeroA = int(input('Insira o número A: '))
numeroB = int(input('Insira o número B: '))
numeroC = int(input('Insira o número C: '))
# Processamento 
R = (numeroA + numeroB)**2
S = (numeroB + numeroC)**2
D = (R + S) / 2

# Saída
print(f'>>>> O cálculo da expressão é igual a {D}')