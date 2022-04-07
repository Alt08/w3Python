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