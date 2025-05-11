def main():
   x = int(input('Digite um valor para o lado: '))
   y = int(input('Digite um valor para o lado: '))
   z = int(input('Digite um valor para o lado: '))
   if eh_triangulo(x, y, z):
       classificaçao_triangulos(x, y, z)
   else:
     print('Os lados informados não formam um triângulo. Tente novamente.')
     main()


def eh_triangulo(x, y, z):
    return x <= y + z and y <= x + z and z <= x + y


def classificaçao_triangulos(x, y, z):
    if x == y == z:
        return print('O triângulo é classificado como equilátero')
    elif x == y != z or x == z != y or y == z != x:
        return print('O triângulo é classificado como equilátero')
    else:
        return print('O triângulo é classificado como escaleno')
    
    
main()