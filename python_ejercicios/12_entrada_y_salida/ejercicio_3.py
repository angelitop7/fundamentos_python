# Ejercicio 3: Lee registro.txt línea por línea con un ciclo for e imprímelo.
# Ejecuta primero ejercicio_2.py para que exista registro.txt.
with open("registro.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())
