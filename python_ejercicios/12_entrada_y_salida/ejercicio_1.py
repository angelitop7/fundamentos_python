# Ejercicio 1: Pide dos números y muestra su suma, resta, multiplicación y división.
a = float(input("Primer número: "))
b = float(input("Segundo número: "))
print(a + b, a - b, a * b)
if b != 0:
    print(a / b)
else:
    print("No se puede dividir entre cero")
