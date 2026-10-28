# Ejercicio 4: Cuenta cuántas veces aparece cada palabra en una frase corta.
frase = "el perro y el gato juegan con el perro"
conteo = {}
for palabra in frase.split():
    conteo[palabra] = conteo.get(palabra, 0) + 1
print(conteo)
