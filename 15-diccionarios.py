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