import re

texto = input("Ingresa la oración: ")

palabras = texto.split()

contador = 0
similares = 0

listaPalabras = []

for x in palabras:
    y = re.sub("\.|\,|\;|\!|\?|\¿|\¡","",x).lower()
    listaPalabras.append(y)
    
for y in listaPalabras:
    contador += 1
    if listaPalabras.count(y) > 1:
        similares += 1

print("La oración tiene " + str(contador-(similares//2)) + " palabras únicas.")
print("La oración tiene " + str(contador) + " palabras en total.")
print("La oración tiene " + str(similares//2) + " palabra(s) similar(es).")