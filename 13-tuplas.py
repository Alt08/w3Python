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