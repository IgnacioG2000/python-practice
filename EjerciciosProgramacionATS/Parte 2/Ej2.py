a = float(input("Digita un numero: "))
b = float(input("Digita otro numero: "))
c = float(input("Digita otro numero: "))

if (a > b) and (a > c):
    print(f"El mayor es {a}")
elif (b > a) and (b > c):
    print(f"El mayor es {b}")
else:
    print(f"El mayor es {c}")

# Otra opcion son 3 elif para acaparar la ultima condicion
'''
if (a > b) and (a > c):
    print(f"El mayor es {a}")
elif (b > a) and (b > c):
    print(f"El mayor es {b}")
elif (c > a) and (c > b):
    print(f"El mayor es {c}")
'''