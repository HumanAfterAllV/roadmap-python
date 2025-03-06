from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self):
        self.velocidad = 0

    @abstractmethod
    def acelerar(self, velocidad):
        pass
    
    @abstractmethod
    def frenar(self, velocidad):
        pass

class Bicicleta(Vehiculo):
    def acelerar(self, velocidad):
        self.velocidad += velocidad
        print(f"Bicicleta acelerando a {self.velocidad} km/h")

    def frenar(self, velocidad):
        self.velocidad -= velocidad
        if self.velocidad < 0:
            self.velocidad = 0
        print(f"Bicicleta frenando a {self.velocidad} km/h")


class Coche(Vehiculo):
    def acelerar(self, velocidad):
        self.velocidad += velocidad
        print(f"Coche acelerando a {self.velocidad} km/h")
        
    def frenar(self, velocidad):
        self.velocidad -= velocidad
        if self.velocidad < 0:
            self.velocidad = 0
        print(f"Coche frenando a {self.velocidad} km/h")


class Patineta(Vehiculo):
    def acelerar(self, velocidad):
        self.velocidad += velocidad
        print(f"Patineta acelerando a {self.velocidad} km/h")
        
    def frenar(self, velocidad):
        self.velocidad -= velocidad
        if self.velocidad < 0:
            self.velocidad = 0
        print(f"Patineta frenando a {self.velocidad} km/h")

def probar_vehiculos(lista_vehiculos):
    for vehiculo in lista_vehiculos:
        vehiculo.acelerar(15)
        vehiculo.frenar(15)

vehiculos = [ Bicicleta(),Coche(),Patineta() ]

probar_vehiculos(vehiculos)