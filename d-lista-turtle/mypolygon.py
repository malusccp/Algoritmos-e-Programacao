import turtle
import math
bob = turtle.Turtle()
print(bob)


def square (t, length):
  for i in range(4):
   t.fd(length)
   t.lt(length)


def polygon (t, length, n):
  angle = 360/n
  for i in range(n):
   t.fd(length)
   t.lt(angle)

def circle (t, raio):
  circunferencia = 2 * math.pi * raio
  n = 30
  length = circunferencia / 360
  polygon (bob, 30, length)

def arc (t, raio, angle):
  arco = 2 * math.pi * raio * (angle/360)
  n = 30
  length = arco / 360
  polygon (bob, 30, length)



turtle.mainloop()