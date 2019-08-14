nroVueltas = int(input("Nro de vueltas: "))
i = 1
sumaTTS = 0
while nroVueltas >= i:
  print(f"Tiempo vuelta {i}")
  hh = int(input(f"Hora {i}: "))
  mm = int(input(f"Minuto {i}: "))
  ss = int(input(f"Segundo {i}: "))
  TTS = hh*3600 + mm*60 + ss
  sumaTTS += TTS
  i += 1

promedio = sumaTTS / nroVueltas # Para que los re
hp = promedio//3600
mp = (promedio%3600)//60
sp = (promedio%3600)%60
print(f"Promedio de tiempos de las {nroVueltas} vueltas es: {int(hp)}:{int(mp)}:{int(sp)}")