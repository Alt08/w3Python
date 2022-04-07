# Ejemplo
# Imprime cada fruta en una lista de frutas:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Bucle a través de una cadena
# Incluso las cadenas son objetos iterables, contienen una secuencia de caracteres:

# Ejemplo
# Repasa las letras de la palabra "banana":

for x in "banana":
  print(x)

# La declaración de ruptura
# Con la instrucción break podemos detener el bucle antes de que haya recorrido todos los elementos:

# Ejemplo
# Salga del bucle cuando xsea "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# Ejemplo
# Salga del ciclo cuando xsea "banana", pero esta vez el descanso viene antes de la impresión:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# La declaración de continuación
# Con la instrucción continuar podemos detener la iteración actual del ciclo y continuar con la siguiente:

# Ejemplo
# No imprimir plátano:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# La función rango() Para recorrer un conjunto de código un número específico de veces, podemos usar la función
# range() , La función range() devuelve una secuencia de números, comenzando desde 0 de forma predeterminada,
# se incrementa en 1 (de forma predeterminada) y termina en un número específico.

# Ejemplo
# Usando la función range():

for x in range(6):
  print(x)


# La función range() por defecto es 0 como valor inicial, sin embargo, es posible especificar el valor inicial
# agregando un parámetro: range(2, 6) , lo que significa valores del 2 al 6 (pero sin incluir el 6):

# Ejemplo
# Usando el parámetro de inicio:

for x in range(2, 6):
  print(x)

# La función range() por defecto incrementa la secuencia en 1, sin embargo, es posible especificar el valor del
# incremento agregando un tercer parámetro: range(2, 30, 3 ) :

# Ejemplo
# Incremente la secuencia con 3 (el valor predeterminado es 1):

for x in range(2, 30, 3):
  print(x)

# Ejemplo
# Imprime todos los números del 0 al 5 e imprime un mensaje cuando el ciclo haya terminado:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Nota: El else bloque NO se ejecutará si el bucle se detiene mediante un break instrucción.

# Bucles anidados
# Un bucle anidado es un bucle dentro de un bucle.
#
# El "bucle interno" se ejecutará una vez por cada iteración del "bucle externo":
#
# Ejemplo
# Escriba cada adjetivo para cada fruta:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

