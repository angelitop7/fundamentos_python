# Ejercicio 3: Imprime la tabla de multiplicar de un número ingresado por el usuario.
n = int(input("Número: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
