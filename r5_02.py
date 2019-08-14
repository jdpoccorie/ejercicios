# Nombre: Juan Diego Poccori Escalante
# Código: 144884

# 2. Escribir un algoritmo que escriba los n primeros numeros impares

# Definir funciones
def escribirImpares(numero):
  i=1
  while numero > 0:
    print(i)
    numero -= 1
    i += 2
    

# Leer número
numero = int(input("Ingresar numero: "))

# Verificar si es positivo incluido el cero
if numero >= 0:
  # Mostrar numeros impares
  escribirImpares(numero)
else:
  print("Error: debe ser un número positivo")