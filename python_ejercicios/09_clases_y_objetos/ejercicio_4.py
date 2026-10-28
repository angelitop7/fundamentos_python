# Ejercicio 4: Crea Vehiculo y una subclase Moto que sobrescriba un método describir().
class Vehiculo:
    def describir(self):
        print("Soy un vehículo")


class Moto(Vehiculo):
    def describir(self):
        print("Soy una moto")


Vehiculo().describir()
Moto().describir()
