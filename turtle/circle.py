import turtle
import math
bob = turtle.Turtle()
print(bob)

def circle (t, raio):
  circunferencia = 2 * math.pi * raio
  n = 30
  length = circunferencia / 360
 polygon (bob, 30, length)

turtle.mainloop()