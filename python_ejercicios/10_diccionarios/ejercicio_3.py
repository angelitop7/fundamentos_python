# Ejercicio 3: Pide una palabra al usuario y verifica si existe como clave en un diccionario
# de traducciones español-inglés.
traducciones = {"hola": "hello", "gato": "cat", "casa": "house", "perro": "dog"}
palabra = input("Palabra: ")
if palabra in traducciones:
    print(traducciones[palabra])
else:
    print("No existe en el diccionario")
