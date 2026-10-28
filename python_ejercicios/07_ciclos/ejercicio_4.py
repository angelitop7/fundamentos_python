# Ejercicio 4: Usa while para pedir una clave hasta que el usuario escriba la correcta.
clave_correcta = "python123"
intento = input("Clave: ")
while intento != clave_correcta:
    print("Clave incorrecta")
    intento = input("Clave: ")
print("Acceso concedido")
