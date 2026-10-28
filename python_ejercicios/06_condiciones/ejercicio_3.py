# Ejercicio 3: Según la hora (0 a 23), imprime Buenos días, Buenas tardes o Buenas noches.
hora = int(input("Hora (0-23): "))
if 0 <= hora < 12:
    print("Buenos días")
elif 12 <= hora < 19:
    print("Buenas tardes")
else:
    print("Buenas noches")
