# Nombre: Juan Diego Poccori Escalante
# Código: 144884

# 10. Escribir un algoritmo para calcular el promedio aritmético de N números
# Leer numero
numero = int(input("Ingresar número: "))

# Verificar si numero es positivo
if numero >= 0:
  i = 1
  suma = 0
  promedio = 0
  while numero >= i:
    # Leer numeros
    ingresaNum = int(input(f"Ingresar numero {i}: "))
    suma+=ingresaNum
    i+=1
  # Calcuar promedio
  promedio = suma / numero
  # Mostrar promedio
  print(f"El promedio es: {promedio}")
else: 
  print("Error: Debe ser un número positivo")
  
