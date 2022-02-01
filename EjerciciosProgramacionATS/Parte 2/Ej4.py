"""
Construir un programa que simule el funcionamiento de una calculadora que puede realizar las cuatro operaciones
 aritméticas básicas (suma, resta, multiplicación y división). 
 El usuario debe especificar la operación con el primer carácter  del nombre de la operación.
S, s – Suma
R, r – Resta
P, p, M, m – Multiplicación
D, d - División
"""

num1 = float(input("Digita el primer numero: "))
num2 = float(input("Digita el segundo numero: "))
operacion = input("Digita la operacion: ").upper()

if operacion == 'S':
    suma = num1 + num2
    print(f"La suma es {suma}")
elif operacion == 'R':
    resta = num1 - num2
    print(f"La resta es {resta}")
elif operacion == 'M':
    producto = num1 * num2
    print(f"El producto es {producto}")
elif operacion == 'D':
    cociente = num1 / num2
    print(f"El cociente entre los dos numeros es {cociente:.2f}")
else:
    print("Digite la operacion correctamente. S -> sumar, R -> restar, M -> multiplicar, D -> dividir")