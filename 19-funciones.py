# Una función es un bloque de código que solo se ejecuta cuando se le llama.
# Puede pasar datos, conocidos como parámetros, a una función.
# Una función puede devolver datos como resultado.
# Crear una función
# En Python, una función se define usando la palabra clave def :

# Ejemplo
def my_function():
  print("Hello from a function")

# Llamar a una función
# Para llamar a una función, use el nombre de la función seguido de paréntesis:
#
# Ejemplo
def my_function():
  print("Hello from a function")

my_function()

# Argumentos
# La información se puede pasar a funciones como argumentos.
#
# Los argumentos se especifican después del nombre de la función, entre paréntesis. Puede agregar tantos argumentos
# como desee, simplemente sepárelos con una coma.
#
# El siguiente ejemplo tiene una función con un argumento (fname). Cuando se llama a la función, pasamos un nombre,
# que se usa dentro de la función para imprimir el nombre completo:
#
# Ejemplo
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Los argumentos a menudo se reducen a args en la documentación de Python.

# ¿Parámetros o argumentos?
# Los términos parámetro y argumento se pueden usar para lo mismo: información que se pasa a una función.
# Desde la perspectiva de una función:
# Un parámetro es la variable que aparece entre paréntesis en la definición de la función.

# Un argumento es el valor que se envía a la función cuando se llama. Número de argumentos Por defecto, una función
# debe llamarse con el número correcto de argumentos. Lo que significa que si su función espera 2 argumentos,
# debe llamar a la función con 2 argumentos, ni más ni menos.

# Ejemplo
# Esta función espera 2 argumentos y obtiene 2 argumentos:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# Argumentos arbitrarios, *args Si no sabe cuántos argumentos se pasarán a su función, agregue un *antes del nombre
# del parámetro en la definición de la función. De esta manera, la función recibirá una tupla de argumentos y podrá
# acceder a los elementos en consecuencia:

# Ejemplo
# Si se desconoce el número de argumentos, agregue un *antes del nombre del parámetro:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Argumentos de palabras clave
# También puede enviar argumentos con la sintaxis clave = valor .
#
# De esta manera el orden de los argumentos no importa.
#
# Ejemplo
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# Argumentos de palabras clave arbitrarias, **kwargs Si no sabe cuántos argumentos de palabras clave se pasarán a su
# función, agregue dos asteriscos: **antes del nombre del parámetro en la definición de la función. De esta forma,
# la función recibirá un diccionario de argumentos y podrá acceder a los elementos en consecuencia:

# Ejemplo
# Si se desconoce el número de argumentos de palabras clave, agregue un doble **antes del nombre del parámetro:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Los argumentos Kword arbitrarios a menudo se reducen a **kwargs en la documentación de Python.

# Valor de parámetro predeterminado
# El siguiente ejemplo muestra cómo utilizar un valor de parámetro predeterminado.

# Si llamamos a la función sin argumento, usa el valor predeterminado:

# Ejemplo
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Pasar una lista como argumento Puede enviar cualquier tipo de datos de argumento a una función (cadena, número,
# lista, diccionario, etc.), y se tratará como el mismo tipo de datos dentro de la función.

# Por ejemplo, si envía una Lista como argumento, seguirá siendo una Lista cuando llegue a la función:

# Ejemplo
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Valores devueltos
# Para permitir que una función devuelva un valor, use la return declaración:

# Ejemplo
eef my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))






































