'''
a = int(input("Digita un numero: "))
b = int(input("Digita otro numero: "))

print(f"Los numeros son, en orden, a = {a} y b =  {b}")

aux = a
a = b

print(f"Los numeros, invertidos, son a = {a} y b = {aux} ")
'''

##### Mejor forma ####
a = int(input("Digita un numero: "))
b = int(input("Digita otro numero: "))

print(f"Los numeros son, en orden, a = {a} y b =  {b}")

# Forma de intercambiar valores facilmente

a, b = b, a

print(f"Los valores nuevos son a = {a} y b = {b} ")
