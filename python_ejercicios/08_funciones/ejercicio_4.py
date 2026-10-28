# Ejercicio 4: Crea factorial(n) con un ciclo y pruébala con 5 (resultado 120).
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


print(factorial(5))
