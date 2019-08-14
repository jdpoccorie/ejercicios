# Nombre: Juan Diego Poccori Escalante
# Código: 144884

import math
# 1. Escribir un algoritmo que calcule el coseno mediante series de Taylor
# definir factorial
def factorial(numero):
  if numero < 0:
    mensaje = "Error: Debe ser un numero mayor o igual a cero"
    return print(mensaje)
  i = 1
  factorial = 1
  while numero >= i:
    factorial*=i
    i+=1
  return factorial

# Leer angulo en sexagesimales
angulo = float(input("Ingrese ángulo en sexagesimales: "))
PIio = 3.1415
# Calcular coseno
# Convertir angulo a radianes
anguloRad = angulo * (math.pi/180)
termino = 1
coseno = 0
signo = 1
j=2
# Mientras termino sea mayor a 0.0000001
while termino > 0.00000001:
  coseno+=(signo*termino)
  termino = anguloRad**(j)/factorial(j)
  j+=2
  signo*=-1

# Mostrar coseno redondeado a 6
print(round(coseno,6))