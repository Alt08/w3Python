# Con el bucle while podemos ejecutar un conjunto de declaraciones siempre que una condición sea verdadera.

i = 1
while i < 6:
    print(i)
    i += 1

# La declaración de ruptura
# Con la instrucción break podemos detener el bucle incluso si la condición while es verdadera:
# Ejemplo
# Salga del bucle cuando tenga 3 años:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# La declaración de continuación
# Con la instrucción continuar podemos detener la iteración actual y continuar con la siguiente:
# Ejemplo
# Continúe con la siguiente iteración si i es 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# La declaración más
# Con la declaración else podemos ejecutar un bloque de código una vez cuando la condición ya no sea verdadera:
# Ejemplo
# Imprima un mensaje una vez que la condición sea falsa:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

