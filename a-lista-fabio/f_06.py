# Entrada
velocidade_km = int(input('Digite o valor da velocidade em km/h: '))
# Processamento
velocidade_ms = velocidade_km / 3.6
# Saída
print(f'A velocidade de {velocidade_km}km/h quando transformada em m/s equivale a {velocidade_ms: .1f}m/s')