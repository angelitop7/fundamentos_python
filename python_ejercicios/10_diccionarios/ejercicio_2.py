# Ejercicio 2: Crea un diccionario de 4 productos con su precio y calcula el total.
productos = {"arroz": 4500, "leche": 3800, "huevos": 12000, "pan": 3000}
total = 0
for precio in productos.values():
    total += precio
print(total)
