import turtle
import math
bob = turtle.Turtle()
print(bob)

def polygon (t, length, n):
  angle = 360/n
  for i in range(n):
   t.fd(length)
   t.lt(angle)

polygon(bob, 70, 5)

turtle.mainloop()