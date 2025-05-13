
# Entrada 
coef_a = int(input('Digite um valor para o coeficiente a:  '))
coef_b = int(input('Digite um valor para o coeficiente b: '))
coef_c = int(input('Digite um valor para o coeficiente c: '))
coef_d = int(input('Digite um valor para o coeficiente d: '))
coef_e = int(input('Digite um valor para o coeficiente e: '))
coef_f = int(input('Digite um valor para o coeficiente f: '))
# Processamento 
x = (coef_c * coef_e) - (coef_b * coef_f) / (coef_a * coef_e) - (coef_b * coef_d)
y = (coef_a * coef_f) - (coef_c * coef_d) / (coef_a * coef_e) - (coef_b * coef_d)

# Saída
print(f'Os valores de x e y são iguais a {x} e {y}, respectivamente')