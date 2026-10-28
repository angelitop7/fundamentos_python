# Ejercicio 3: Escribe una función que reciba una lista y devuelva el número mayor sin usar max.
def mayor(lista):
    m = lista[0]
    for n in lista:
        if n > m:
            m = n
    return m


print(mayor([4, 9, 2, 15, 7]))
