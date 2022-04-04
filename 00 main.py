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
#  --------------- LISTAS ---------------
'''
    se puede cambiar y estan ordenados, lo que permite 
    agregar y eliminar elementos en una lista después de que se haya creado y permite duplicados
    se escriben con corchete
        listas -> []
    
    es una colección ordenada e inmutable, no se puede modificar y permite valores duplicados
    no se puede agregar o eliminar datos despues de ser creado
    se escribe con parentesis
        tuplas -> () 
    
    Los elementos establecidos no se pueden modificar y no estan ordenados, pero puede eliminar elementos y agregar elementos nuevos.
    se escriben con llaves
    set
    
    se escriben con llaves
    diccionarios -> {}
'''
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
'''
    Lista: es una colección ordenada y modificable. Permite miembros duplicados.
    Tuple: es una colección ordenada e inmutable. Permite miembros duplicados.
    Conjunto: es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
    Diccionario: es una colección ordenada** y modificable. No hay miembros duplicados.
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

# Elminar elementos de la lista
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

# ------------- TUPLAS ------------------
# tipos de datos en las tuplas
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# Las tuplas pueden contener diferentes tipos de datos
tuple4 = ("abc", 34, True, 40, "male")

# El tipos de datos que contniene la tupal
mytuple5 = ("apple", "banana", "cherry")
print(type(mytuple5))

# constructor tupla()
thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thistuple)

# -> ACCESO A LA TUPLAS <-
# Una tupla es una colección ordenada e inmutable

# Acceder a un elemento por indice
thistuples = ("apple", "banana", "cherry")
print(thistuples[1])

# Indexación negativa
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# Acceso a elementos entre un rango
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# La busqueda inicia en la posicion 2 y termina en la 5, pero esta ultima posicion no se incluye
print(thistuple[2:5])

# Comprobar si un elemento existe en la tupla
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# Actulizar tuplas (inmutables)
# Para poder actualizar datos en tupla primero se convierte en lista
# Una vez agregado el nuevo elemento se convierte nuevamente a tupla
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# agregar elementos a tupla - Se hace lo mismo que actualizar
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Agregar una tupla a otra tupla
thistuple = ("apple", "banana", "cherry")
# AL crea una tupla de 1 elemento se coloca una ,(coma) al final
# de lo contrario no sera reconocida como una tupla
y = ("orange",)
thistuple += y

print(thistuple)

# Eliminar elementos en una tupla - se hace lo mismo que al agregar un elemento
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# Encaquetacion de tuplas
fruits = ("apple", "banana", "cherry")

# Desempaquetando una tupla
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Iterar a través de los elementos e imprimir los valores:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# Iterar elementos de la tuplas por índice - usando range() y len()
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

# ------------- SETS (Conjuntos) ------------------
# Es una colección desordenada, inmutable* y no indexada

# Crear un sets
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Acceder a sus elementos mediante un for
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# Comprobar si un elemento se encuentra en la tupla
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Agregue un elemento a un conjunto, usando el método add()
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")

print(thisset)

# Agregar un sets a otro sets con updata()
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)

print(thisset)

# Al sets se le puede agregar tuplas, listas o diccionarios
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)

print(thisset)

# Eliminar un elemento del sets usando remove()
# Elimina "banana" usando el remove() método:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")

print(thisset)
# Nota: Si el elemento a eliminar no existe, remove()generará un error

# Eliminar un elemento del sets usando discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")

print(thisset)
# Nota: Si el elemento a eliminar no existe, NOdiscard() generará un error.

# Vaciar un sets con clear()
thisset = {"apple", "banana", "cherry"}
thisset.clear()

# print(thisset)

# Eliminar sets por completo con del
thisset = {"apple", "banana", "cherry"}
del thisset

# print(thisset)

# Nota: Ambos union()y update() excluirán cualquier elemento duplicadoO
# Unir sets = con union()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# Unir sets = con update()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)

print(set1)

# El intersection_update() método mantendrá solo los elementos que están presentes en ambos conjuntos.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)

print(x)

# El intersection() método devolverá un nuevo conjunto, que solo contiene los elementos que están presentes en ambos conjuntos
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)

print(z)

# El symmetric_difference_update() método mantendrá solo los elementos que NO están presentes en ambos conjuntos
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)

print(x)

# El symmetric_difference() método devolverá un nuevo conjunto, que contiene solo los elementos que NO están presentes en ambos conjuntos
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)

print(z)

# Method	Description
# symmetric_difference_update()	    inserts the symmetric differences from this set and another
# add()	                            Adds an element to the set
# update()	                        Update the set with the union of this set and others
# clear()	                        Removes all the elements from the set
# discard()	                        Remove the specified item
# remove()	                        Removes the specified element
# intersection_update()	            Removes the items in this set that are not present in other, specified set(s)
# pop()	                            Removes an element from the set
# difference_update()	            Removes the items in this set that are also included in another, specified set
# difference()	                    Returns a set containing the difference between two or more sets
# copy()	                        Returns a copy of the set
# intersection()	                Returns a set, that is the intersection of two other sets
# isdisjoint()	                    Returns whether two sets have a intersection or not
# issubset()	                    Returns whether another set contains this set or not
# issuperset()	                    Returns whether this set contains another set or not
# union()	                        Return a set containing the union of sets
# symmetric_difference()            Returns a set with the symmetric differences of two sets

# ------- -> Diccionarios <- -------
# se utilizan para almacenar valores de datos en pares
# clave:valor
# una colección ordenada *, modificable y que no admite duplicados.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# -- -> No permite valores duplicados <- --
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,  # -> valor duplicados no se imprime
    "year": 2020  # -> valor duplicados no se imprime
}
print(thisdict)

# Imprimir loguitud del diccionario
print(len(thisdict))

# Los diccionario pueden ser de cualquier tipo de datos
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

print(thisdict)

# Para acceder a un elemento hacemos referencia a su nombre clave
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# Forma 1
x = thisdict["year"]
print(x)

# Forma 2
x = thisdict.get("model")
print(x)

# Obtener claves keys()
x = thisdict.keys()
print(x)

# La lista de claves es una vista del diccionario,
# lo que significa que cualquier cambio realizado
# en el diccionario se reflejará en la lista de claves.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)  # before the change
car["color"] = "white"
print(x)  # after the change

# Obtener valores values()
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()
print(x)  # before the change
# Realice un cambio en el diccionario original y vea que la lista de valores también se actualice
car["year"] = 2020
print(x)  # after the change

# Obtener artículos
# El método items() devolverá cada elemento en un diccionario, como tuplas en una lista.
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()
print(x)  # before the change
car["year"] = 2020
print(x)  # after the change

# Comprobar si existe la clave
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Si existe dicho elemento")

# Cambiar valores haciendo referencia a su nombre clave
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018

# Actualizar diccionarios con los elementos del argumento dado -> update()
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

# El método update() actualizará el diccionario con los elementos de un argumento dado.
# Si el artículo no existe, se agregará.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)

# El método pop() elimina el elemento con el nombre de clave especificado
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

# El  método popitem() elimina el último elemento insertado
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)

# La delpalabra clave elimina el elemento con el nombre de clave especificado
# Tambien puede eliminar un diccionario completamento, pero dara error al intentar imprimir dicho dicicionario
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

# El método clear() vacía el diccionario
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

# Imprimir las claves de los diccionarios con FOR
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x)

# Imprimir los  valores
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(thisdict[x])

# Tambien podemos obtener las claves y los valores usando las siguientes funciones
# keys()   ->
# values() ->
for x in thisdict.keys():
    print(x)
for x in thisdict.values():
    print(x)

# Recorra las claves y los valores usando el método items():

for x, y in thisdict.items():
    print(x, y)

# copia de un diccionario con el método copy()
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print("diccionario copiado con el método copy()")
print(mydict)

# una copia de un diccionario con la función dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print("Diccionrio copia con la funcion dict()")
print(mydict)

# Diccionarios anidados forma 1
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Forma 2 de crear diccionarios anidados
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# Metodos que se pueden usar en los diccionarios

# copy()	    Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	        Returns the value of the specified key
# items()	    Returns a list containing a tuple for each key value pair
# values()	    Returns a list of all the values in the dictionary
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# keys()	    Returns a list containing the dictionary's keys
# clear()	    Removes all the elements from the dictionary
# pop()	        Removes the element with the specified key
# popitem()	    Removes the last inserted key-value pair
# update()	    Updates the dictionary with the specified key-value pairs
