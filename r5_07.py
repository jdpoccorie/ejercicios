# Nombre: Juan Diego Poccori Escalante
# Código: 144884

# 7. En el centro meteorológico de la UNSAAC se tiene registrado las temperaturas diarias mínimas del año 1998. Elaborar un algoritmo que permita determinar cuántos días fueron con helada y cuántos sin helada. Se considera un dia con helada cuando la temperatura mínima de ese día es menor o igual a cero.

# Inicializar variables
nroDias = 365
i = 1
diasConHelada = 0
diasSinHelada = 0
while i <= nroDias:
  # Leer temperatura diaria
  temperatura = int(input(f"Temperatura del día {i}: "))
  if temperatura <= 0:
    diasConHelada+=1
  else:
    diasSinHelada+=1
  i+=1

# Mostrar numero de dias con helada y sin helada
print(f"Numero de dìas con helada {diasConHelada}")
print(f"Numero de dìas sin helada {diasSinHelada}")
