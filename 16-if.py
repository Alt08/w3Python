# Es igual a : a == b
# No es igual a: a != b
# Menos que: a < b
# Menor o igual que: a <= b
# Mayor que: a > b
# Mayor o igual que: a >= b

# IF
a = 33
b = 200
if b > a:
  print("b is greater than a")

# ELIF
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# IF ELIF ELSE
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# IF forma corta
if a > b: print("a is greater than b")

# IF ELSE forma corta - una condicion
a = 2
b = 330
print("A") if a > b else print("B")
# Forma corta IF ELSE con 3 condiciones
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# IF con operadores logicos -> AND
# Prueba si aes mayor que b, Y si c es mayor que a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# IF con operadores logicos -> OR
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


# IF anidados
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# ifLas declaraciones no pueden estar vacías, pero si por alguna razón tiene
# una ifdeclaración sin contenido, passintrodúzcala para evitar errores.
a = 33
b = 200

if b > a:
  pass