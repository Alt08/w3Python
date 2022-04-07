# ---- VARIABLES ----
# no es necesario declarar el tipo de variable
x = 5  # entero
y = "John"  # String
print(x)
print(y)

# Las variables con el mismo nombre se pueden reasignar el valor
x = 4  # x is of type int
x = "Sally"  # x is now of type str
print(x)

# podemos especificar el tipo de variable de la siguiente manera
# Esto es opcional a menos que sea necesario
x = str(3)
y = int(3)
z = float(3)

# Obtener el tipo de variable
x = 5
y = "John"
print(type(x))
print(type(y))

# Para los string se pueden usar las comillas simples o dobles
x = "John"
x = 'John'
print(x)
print(x)

# Distingue mayúsculas y minúsculas
a = 4
A = "Sally"
print(a)
print(A)

# valores para múltiples variables
x, y, z = "Melon", "Banana", "Papa"
print(x)
print(y)
print(z)

# Un valor para múltiples variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# colección de valores en una lista
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Variables de salida
x = "awesome"
print("Python is " + x)

# Variables globales
x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()

# Variables globales con el mismo nombre
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)


# palabra clave mundial = variable local pero declarado de manera local dentro de una funcion
# Si usa la globalpalabra clave, la variable pertenece al ámbito global
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

# Para cambiar el valor de una variable global dentro de una función
x = "awesome"

def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)