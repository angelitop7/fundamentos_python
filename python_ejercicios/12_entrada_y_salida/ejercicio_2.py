# Ejercicio 2: Pide el nombre y la ficha del aprendiz y guárdalos en un archivo registro.txt.
nombre = input("Nombre del aprendiz: ")
ficha = input("Ficha: ")
with open("registro.txt", "w", encoding="utf-8") as f:
    f.write(nombre + "\n")
    f.write(ficha + "\n")
