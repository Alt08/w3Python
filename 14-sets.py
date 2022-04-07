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
