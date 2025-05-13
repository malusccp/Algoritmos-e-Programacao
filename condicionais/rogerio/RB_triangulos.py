import math


    

def eh_triangulo(x, y, z):
    return x <= y + z and y <= x + z and z <= x + y

def perimetro_triangulo(x, y, z):
    return print(f'O perímetro do triângulo é igual a {x + y + z}')

def area_triangulo(x, y, z):
   p = (x + y + z)/2
   return print(f'A área do triângulo é igual a {math.sqrt(p * (p - x) * (p - y) * (p - z))} ')  

def classificacao(x, y, z):
    if x == y or x == z or y == z :
        return print('O triângulo é isóceles e retângulo')
    elif x == y == z:
        return print('O triângulo é equilátero e acutângulo')
    else:
        return print('O triângulo é escaleno e obtusângulo')
    
    
def eh_degenerado(x, y, z):
    return eh_triangulo(x,y,z) and (x == y + z or y == x + z or z == x + y)


def main():
    x = int(input('Digite o valor do lado do triângulo: '))
    y = int(input('Digite o valor do lado do triângulo: '))
    z = int(input('Digite o valor do lado do triângulo: '))
    if eh_triangulo(x, y, z):
      print('Os lados formam um triângulo')
      if eh_degenerado(x, y, z):
        print('Além disso, é um triângulo degenerado')
      perimetro_triangulo(x, y, z)
      area_triangulo(x, y, z)
      classificacao(x, y, z)
    else: 
        print('Os lados não formam um triângulo')
        main()
       
 
 
main()
