# Nombre: Juan Diego Poccori Escalante
# Código: 144884

# 6. Escribir un algoritmo que calcule la suma de los n numeros enteros positivos
# Definir funciones
def calcularSuma(numero):
  i = 1
  sumaNumeros = 0
  while numero >= i:
    sumaNumeros += i
    i+=1
  return sumaNumeros


# Leer numero
numero = int(input("Ingresar numero: "))

# Verificar si es un numero positivo
if numero >= 0:
  print(calcularSuma(numero))
else:
  print("Error: Debe ser un numero positivo")
