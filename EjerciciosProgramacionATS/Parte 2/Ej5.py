"""
Hacer un programa que simule un cajero automático con un saldo inicial de $1000
y tendrá el siguiente menú de opciones:
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir
"""

saldo = 1000

print("\t ***MENU***")
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")

opcion = int(input("Digita la opcion: "))

if opcion == 1:
    montoAIngresar = float(input("Digite el monto a ingresar: "))
    saldo += montoAIngresar
    print(f"El saldo disponible es {saldo}")
elif opcion == 2:
    montoARetirar = float(input("Digite el monto a retirar: "))
    if montoARetirar > saldo:
        print("No tiene saldo suficiente para retirar")
    else:
        saldo -= montoARetirar
        print(f"El saldo disponible es {saldo}")
elif opcion == 3:
    print(f"El saldo disponible es {saldo}")
elif opcion == 4:
    print("Gracias por usar nuestro cajero")
else:
    print("Se equivoco de opcion de menu")