# Nombre: Juan Diego Poccori Escalante
# Código: 144884

# 1. Escribir un algoritmo que escriba el numero, el cuadrado y el cubo de los n primeros numeros enteros positivos

# Definir funciones
# Mostrar numero, Cuadrado, Cubo
def listarNumeros(numero):
  i=1
  while numero >= i:
    print(i, i**2, i**3)
    i+=1
    

# Leer numero
numero = int(input("Ingresar número: "))

# mostrar numero, cuadrado, cubo
listarNumeros(numero)