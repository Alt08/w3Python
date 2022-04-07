# El try permite probar un bloque de código en busca de errores.
# El except le permite manejar el error.
# El else te permite ejecutar código cuando no hay ningún error.
# El finally le permite ejecutar código, independientemente del resultado de los bloques de prueba y excepción.

# Manejo de excepciones Cuando ocurre un error, o una excepción como lo llamamos, Python normalmente se detendrá y
# generará un mensaje de error. Estas excepciones se pueden manejar usando la trydeclaración: Ejemplo El trybloque
# generará una excepción, porque xno está definido:

try:
  print(x)
except:
  print("An exception occurred")

# Esta declaración generará un error, porque xno está definida:

# muchas excepciones Puede definir tantos bloques de excepción como desee, por ejemplo, si desea ejecutar un bloque
# de código especial para un tipo especial de error:
#
# Ejemplo
# Imprima un mensaje si el bloque try genera un NameErrory otro para otros errores:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


# Else
# Puede usar la palabra clave para definir un bloque de código que se ejecutará si no se generaron errores:
#
# Ejemplo
# En este ejemplo, el bloque try no genera ningún error:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


# El finally, si se especifica, se ejecutará independientemente de si el bloque try genera un error o no.
#
# Ejemplo
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# Como desarrollador de Python, puede optar por generar una excepción si se produce una condición.
# Para lanzar (o generar) una excepción, use la raisepalabra clave.

# Ejemplo
# Genera un error y detiene el programa si x es menor que 0:

x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")

