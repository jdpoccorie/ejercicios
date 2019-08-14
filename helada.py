# Inicializar variables
nroDiasMayo = 31
i = 1
diasConHelada = 0
while i <= nroDiasMayo:
  # Leer temperatura diaria
  temperatura = int(input(f"Temperatura del día {i}: "))
  if temperatura < 0:
    diasConHelada+=1
  i+=1

# Mostrar numero de dias con helada y sin helada
print(f"Numero de dìas con helada {diasConHelada}")
