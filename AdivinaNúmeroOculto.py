from random import randint as rint

number_random = rint(1,50)
intentos = 0

number_enter = int(input("Ingrese el número oculto(1-50): "))

while number_enter != number_random:
    intentos += 1
    if number_enter < number_random:
        number_enter = int(input("Ingrese un número más alto: "))
    else:
        number_enter = int(input("Ingrese un número más bajo: "))

print("Felicidades encontraste el número oculto " + str(number_random))
print("Utilizaste " + str(intentos+1) + " intentos")