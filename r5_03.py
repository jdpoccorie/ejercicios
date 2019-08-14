# Nombre: Juan Diego Poccori Escalante
# Código: 144884

# 3. Escribir un algoritmo que muestra la tabla de multiplicar del 8

# Definir funciones
# Funcion que muestra la tabla de multiplicar de un numero
def tablaMultiplicar(numero):
  i = 1
  while i <= 12:
    print("8 *", i, "=", numero * i)
    i+=1

# Leer número
numero = int(input("Ingrese número: "))

# mostrar tabla de multiplicar
tablaMultiplicar(numero)