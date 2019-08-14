# Leer nrodeVentas
nroVentas = int(input("Ingresar nro de ventas: "))
i = 1
importeTotal = 0

while nroVentas >= i:
  print(f"Venta Número {i}")
  # Leer numero de alpacas vendidas
  nroAlpacasVendidas = int(input("Numero de alpacas vendidas: "))
  j = 1
  sumVenta = 0
  while nroAlpacasVendidas >= j:
    # Leer precio de cada alpaca vendida
    precio = float(input(f"Precio alpaca {j}: "))
    sumVenta += precio
    j+=1
  importeTotal += sumVenta
  i+=1

# Mostrar importe total
print(importeTotal)