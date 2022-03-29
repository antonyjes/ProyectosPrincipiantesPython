import re

def limpiartexto(text):
    text = re.sub("\.|\;|\!|\?|\¿|\¡|\*","",text)
    return text

nombre = input("Ingresa tu nombre: ")
nombre = limpiartexto(nombre)

while nombre == "":
    print("Error nombre inválido.")
    nombre = input("Ingresa tu nombre: ")
    nombre = limpiartexto(nombre)

fechanacimiento = input("Ingresa tu fecha de nacimiento: ")
fechanacimiento = limpiartexto(fechanacimiento)

while fechanacimiento == "":
    print("Error fecha inválida")
    fechanacimiento = input("Ingresa tu fecha de nacimiento: ")
    fechanacimiento = limpiartexto(fechanacimiento)

direccion = input("Ingresa tu dirección: ")
direccion = limpiartexto(direccion)

while direccion == "":
    print("Error dirección inválida")
    direccion = input("Ingresa tu dirección: ")
    direccion = limpiartexto(direccion)

metas = input("Ingresa tus metas personales: ")
metas = limpiartexto(metas)

while metas == "":
    print("Error fecha inválida")
    metas = input("Ingresa tus metas personales: ")
    metas = limpiartexto(metas)

print("Nombre: " + nombre)
print("Fecha de nacimiento: " + fechanacimiento)
print("Dirección: " + direccion)
print("Metas personales: " + metas)