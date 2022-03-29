factura = float(input("Ingrese total de la factura: "))

def propina(porcentaje):
    propina = factura * porcentaje
    roundpropina = round(propina,2)  #redondear a dos decimales
    return roundpropina

print("\n*********Porcentaje a aplicar**********")
print("\n1. 18%")
print("2. 20%")
print("3. 25%")
opcion = int(input("\nIngrese la opción a aplicar(1,2 o 3): "))

while opcion != 1 and opcion != 2 and opcion != 3:
    opcion = int(input("\nIngrese la opción a aplicar(1,2 o 3): "))

if opcion == 1:
    print(f"\nLa propina aplicando el 18% es ${propina(0.18)} que contabiliza un total de ${factura + propina(0.18)}.")
elif opcion == 2:
    print(f"\nLa propina aplicando el 20% es ${propina(0.2)} que contabiliza un total de ${factura + propina(0.2)}.")
else:
    print(f"\nLa propina aplicando el 25% es ${propina(0.25)} que contabiliza un total de ${factura + propina(0.25)}.")
