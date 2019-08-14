# Nombre: Juan Diego Poccori Escalante
# Código: 144884

# 1. Escribir un algoritmo que calcule la siguiente expresión:
# (1^2) + (2^2) - (3^2) + (4^2) - (5^2) + ... + (100^2)

# Inicializar variables y calcular suma E
nro = 100
i = 1
sumaE = 0
signo = 1
expresion = ""
while nro >= i:
  sumaE+=(signo * i**2)
  expresion += f"{signo} * {i}^2"
  signo*=-1
  i+=1
# Mostar la sumaE
print(sumaE)
print(expresion)