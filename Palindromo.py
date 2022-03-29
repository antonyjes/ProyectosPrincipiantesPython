palabras = []

for x in range(1,6):
    palabra = input(f"Ingrese palabra número {x}: ")
    palabras.append(palabra)

for i in range(len(palabras)):
    if palabras[i][::-1] == palabras[i]:
        print(f"La palabra {palabras[i]} es palíndroma.")
    else:
        print(f"La palabras {palabras[i]} no es palíndroma.")