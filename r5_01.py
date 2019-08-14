# Nombre: Juan Diego Poccori Escalante
# Código: 144884

# 1. Escribir un algoritmo que escriba los n primeros enteros positivos

# Definir funciones
def escribirNumeros(numero):
  i = 0
  while numero >= i:
    print(i)
    i+=1

# Leer numero
numero = int(input("Ingrese número: "))

# Verificar si es positivo incluido el cero
if numero >= 0:
  # Escribir numeros
  escribirNumeros(numero)
else:
  print("Error, el número debe ser positivo")