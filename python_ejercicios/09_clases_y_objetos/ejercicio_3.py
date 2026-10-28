# Ejercicio 3: Agrega a Cuenta un método retirar que no permita saldo negativo.
class Cuenta:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def retirar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Fondos insuficientes")


c = Cuenta(1000)
c.depositar(500)
c.retirar(2000)
c.retirar(300)
print(c.saldo)
