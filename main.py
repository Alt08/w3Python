# Identacion tiene que ser al menor 1 para no dar error


# Bien
if 5 > 2:
    print("Five is greater than two!")
# Mal
# if 5 > 2:
# print("Five is greater than two!")

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

# TIPOS DE DATOS
'''
Tipo de texto:	str
Tipos numéricos:	int, float, complex
Tipos de secuencia:	list, tuple, range
Tipo de mapeo:	dict
Establecer tipos:	set, frozenset
Tipo booleano:	bool
Tipos binarios:	bytes, bytearray, memoryview
'''

import random

print(random.randrange(1, 10))

# CANDENAS MULTILINEA
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# CORTAR CADENAS
b = "Hello, World!"
print(b[2:5])

# Cortar desde el principio
b = "Hello, World!"
print(b[:5])

# Cortar hasta el final - de izquierda a derecha
b = "Hello, World!"
print(b[2:])

# Indexación negativa - de derecha a izquierda
b = "Hello, World!"
print(b[-5:-2])

# MODIFICAR CADENAS - Mayúsculas
a = "Hello, World!"
print(a.upper())

# MODIFICAR CADENAS - Minúscula
a = "HELLO, WORLD!"
print(a.lower())

# MODIFICAR CADENAS - Eliminar espacios en blanco
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"

# MODIFICAR CADENAS - Reemplazar cadena
a = "Hello, World!"
print(a.replace("H", "J"))

# MODIFICAR CADENAS - Cadena dividida
a = "Hello, World!"
print(a.split(","))  # regresa ['Hello', ' World!']

# Formato de cadena
'''
    --ESTA MAL PORQUE NO SE PUEDE CONCATENAR STRING CON INT
    age = 36
    txt = "My name is John, I am " + age
    print(txt)
'''

# FORMA CORRECTA
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# número ilimitado de argumentos
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# pase de indice
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Caracteres de escape
# txt = "We are the so-called "Vikings" from the north." - esta mal

# funcionando bien
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# BOOLEANOS - REGRESA TRUE O FALSE
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Evaluar una cadena y un número
print(bool("Hello"))
print(bool(15))

# LISTAS - los datos pueden ser de cuarquiel tipo
fruits = ["apple", "banana", "cherry", "cherry"]
print(fruits)

# OBTENER LA LONGUITUD DE UNA LISTA / len()
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

'''
      La lista:       Es una colección ordenada y modificable. Permite miembros duplicados.
      Tuple:          Es una colección ordenada e inmutable. Permite miembros duplicados.
      Conjunto:       Es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
      El diccionario: Es una colección ordenada** y modificable. No hay miembros duplicados.
'''

thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)

# ACCESO POR POSICION
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# ACCESO POR POSICION NEGATIVA
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# ACCESO POR POSICION DENTRO DE UN RANGO
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# CAMBIAR ALGUN VALOR DE LA LISTA
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# CAMBIAR POR RANGO EL VALOR DE LA LISTA
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# INSERTAR ELEMENTOS A LA LISTA - insert() inserta el elemento en una posicion especifica
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "watermelon")
print(thislist)

# AGREGAR ELEMENTOS A LA LISTA - append() agrega el elemento al final de la lista
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# AGREGAR ELEMENTOS DE UNA LISTA A LA LISTA ACTUAL - extend()
'''
  CON extend() podemos mezclar tuplas, lista, diccionarios y conjuntos
'''
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

print('\n')

# minar elementos de la lista
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Eliminar por índice especificado
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Con la funcion pop podemos eliminar el ultimo elementos
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# del otro forma de eliminar un elemento
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Vaciar contenido de una lista
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Recorrer una lista por sus valores - ciclo for
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print('la fruta es: ' + x)

# Recorriendo con un for corto
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# Recorrer una lista por sus indices - ciclo for
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# Recorriendo lista por su indice - ciclo while
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Lista sin comprensión
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

# Lista con comprensión
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Ordenar litas - alfanumericos
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Ordenar litas - Numericos
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Ordenar descendiente alfanumericos y numericos
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

# Copiar una lista
thislist = ["1", "2", "3"]
mylist = thislist.copy()
print(mylist)

# Otra manera de copiar
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Unir listas - forma 1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Unir listas - forma 2
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
print(list1)

# Métodos de lista
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

