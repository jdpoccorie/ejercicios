# Nombre: Juan Diego Poccori Escalante
# Código: 144884

# 1. Escribir un algoritmo que calcule la suma de la siguiente expresió:
# (1/100) + (2/99) + (3/98) + (4/97) + ... + (99/2) + (100/1)

i = 1
j = 100
sumaE = 0
expresions = ""
while i <= 100:
  expresion = i / j
  expresions += (f"({i}/{j}) + ")
  sumaE += expresion
  i+=1
  j-=1
# print(expresions)
print(f"Suma de la expresión {sumaE}")