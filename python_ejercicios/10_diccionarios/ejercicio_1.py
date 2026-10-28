# Ejercicio 1: Crea un diccionario con los datos de un libro (título, autor, año) e imprímelos.
libro = {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "anio": 1967}
for clave, valor in libro.items():
    print(clave, valor)
