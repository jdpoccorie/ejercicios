# Nombre: Juan Diego Poccori Escalante
# Código: 144884

# 5. Se tiene una relacion de alumnos. Para cada alumno se tiene 3 notas. Escribir un algoritmo que calcule el promedio de cada alumno

# Definir funciones
def calcPromedio(nroAlumnos):
  i=0
  while nroAlumnos > i:
    j = 1
    sumaNotas = 0
    print(f":::::Alumno {i+1}:::::")
    while j <= 3:
      nota = int(input(f"Ingrese nota {j}: "))
      sumaNotas += nota
      j+=1
    promedio = sumaNotas / 3
    print(f"Promedio Alumno {i+1} es: {round(promedio, 2)}")
    i+=1


# Leer numero
nroAlumnos = int(input("Ingresar número de alumnos: "))

# Verificar si es un nroAlumnos es positivo
if nroAlumnos >= 0:
  calcPromedio(nroAlumnos)
else:
  print("Error: Numero de alumnos debe ser un numero positivo")
