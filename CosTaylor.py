# Nombre: Juan Diego Poccori Escalante
# Código: 144884

# 1. Escribir un algoritmo que calcule el coseno mediante series de Taylor
x = float(input("Angulo en sexagesimales: "))

# Calcular el coseno
x = x * 3.14159265/180
signo = 1
numerador = x * x
denominador = 2
termino = 1
coseno = 0
k = 1
while termino > 0.00000000000001:
  k = k + 2
  coseno = coseno + (termino * signo)
  termino = numerador / denominador
  numerador = numerador * (x * x)
  denominador = denominador * k * (k+1)
  signo = -signo

print(round(coseno, 6))

# 1/0!
# -x^2/2!
# x^4/4!
# -x^6/6!
# ...
