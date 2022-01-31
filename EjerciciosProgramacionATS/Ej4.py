import math
# Dado un radio, calcular area y longitud de un circulo

radio = float(input("Digita el radio del circulo: "))

area = math.pi * radio ** 2

longitud = 2 * math.pi * radio

print(f"El area del circulo es: {area:.2f}")
print(f"La longitud del circulo es: {longitud:.2f}")

# .nf -> cantidad n de decimales despues de la coma
