import random

mano = ["piedra", "papel", "tijera"]
random_mano = random.choice(mano)

user_mano = input("Ingrese su elección(piedra o papel o tijera): ")

print("La computadora eligió: " + random_mano)

if user_mano == "tijera" and random_mano == "piedra":
    print("Computadora gana")
elif user_mano == "piedra" and random_mano == "tijera":
    print("Tú ganas")
elif user_mano == "piedra" and random_mano == "papel":
    print("Computadora gana")
elif user_mano == "papel" and random_mano == "piedra":
    print("Tú ganas")
elif user_mano == "tijera" and random_mano == "papel":
    print("Tú ganas")
elif user_mano == "papel" and random_mano == "tijera":
    print("Computadora gana")
else:
    print("Empate")