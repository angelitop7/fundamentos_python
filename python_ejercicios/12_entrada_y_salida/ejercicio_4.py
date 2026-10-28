# Ejercicio 4: Crea un programa que pida 3 notas, calcule el promedio y lo guarde en un archivo
# con el mensaje Aprobó o No aprobó.
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
promedio = (n1 + n2 + n3) / 3
mensaje = "Aprobó" if promedio >= 3.0 else "No aprobó"
with open("resultado.txt", "w", encoding="utf-8") as f:
    f.write(f"Promedio: {promedio:.2f} - {mensaje}\n")
print(mensaje)
