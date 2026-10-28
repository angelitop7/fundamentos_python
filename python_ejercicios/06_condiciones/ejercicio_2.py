# Ejercicio 2: Pide un año y di si es bisiesto (divisible por 4 y no por 100, o divisible por 400).
anio = int(input("Año: "))
if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print("Es bisiesto")
else:
    print("No es bisiesto")
