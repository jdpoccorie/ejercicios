import math
x = float(input("Velocidad liebre: "))
y = float(input("Velocidad tortuga: "))
t = 10
while t <= 100:
  ex = x * t
  ey = y * t
  ez = math.sqrt(ex**2 + ey**2)
  print(f"espacio de sepación para t={t} es: {ez}")
  t+=10