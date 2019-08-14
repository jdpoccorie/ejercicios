k = 0
denominador = 101
numerador = 0

# mio
suma = 0
Esuma = ""

while k < 100:
  k = k + 1
  denominador = denominador - 1
  numerador = numerador + 1
  termino = numerador / denominador
  suma = suma + termino
  Esuma = Esuma + f"{numerador} / {denominador} \n"

print("La expresion es:", Esuma)
print("La suma es: ", suma)