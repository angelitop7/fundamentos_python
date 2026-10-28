# Ejercicio 1: Crea la clase Aprendiz con nombre y ficha, y un método que los muestre.
class Aprendiz:
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha

    def mostrar(self):
        print(f"Aprendiz: {self.nombre} - Ficha: {self.ficha}")


a = Aprendiz("Ana", "2900001")
a.mostrar()
