def main():
   ang1 = int(input('Digite um valor para o ângulo: '))
   ang2 = int(input('Digite um valor para o ângulo: '))
   ang3 = int(input('Digite um valor para o ângulo: '))
   if eh_triangulo(ang1, ang2, ang3):
      classificaçao_triangulo(ang1, ang2, ang3)
   else:
      print('Os valores citados não formam um triângulo. Tente novamente.')
      main()
      
      
def eh_triangulo(ang1, ang2, ang3):
   return ang1 + ang2 + ang3 == 180

def classificaçao_triangulo(ang1, ang2, ang3):
   if ang1 == 90 or ang2 == 90 or ang3 == 90:
      return print('O triângulo é classificado como retângulo')
   elif ang1 < 90 and ang2 < 90 and ang3 < 90:
      return  print('O triângulo é classificado como acutângulo')
   elif ang1 > 90 or ang2 > 90 or ang3 > 90:
      return  print('O triângulo é classificado como obtusângulo')

main()