# Formato de cadena ()
# El format()método le permite formatear partes seleccionadas de una cadena.
#
# A veces, hay partes de un texto que no controla, ¿tal vez provienen de una base de datos o de la entrada del usuario?
#
# Para controlar dichos valores, agregue marcadores de posición (corchetes {}) en el texto y ejecute los valores a
# través del format()método:
#
# Ejemplo
# Agrega un marcador de posición donde quieras mostrar el precio:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# Valores múltiples

uantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Números de índice Puede usar números de índice (un número dentro de las llaves {0}) para asegurarse de que los
# valores se colocan en los marcadores de posición correctos:
#
# Ejemplo
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Si desea hacer referencia al mismo valor más de una vez, utilice el número de índice:
# Ejemplo
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# Índices con nombre También puede usar índices con nombre ingresando un nombre dentro de las llaves {carname},
# pero luego debe usar nombres cuando pasa los valores de los parámetros txt.format(carname = "Ford"):
#
# Ejemplo
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))
