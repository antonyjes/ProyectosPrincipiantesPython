num = int(input("Ingresa un número(1-100): "))

while num<1 or num>100:
    num = int(input("Ingresa un número(1-100): "))

if num%2==0:
    print("Este número es par.")
else:
    print("Este número es impar.")