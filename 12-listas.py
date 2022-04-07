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