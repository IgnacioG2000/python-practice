# Hacer un programa que pida un caracter e indique si es una vocal o no

letra = input("Digite una letra: ").lower() # <- me lo pasa a minuscula

# Tambien se puede hacer asi
'''
letra = input("Digite una letra: ")
letra = letra.lower()
'''

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("La letra es vocal")
else:
    print("La letra no es vocal")
