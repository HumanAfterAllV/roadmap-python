from abc import ABC, abstractmethod
import math

class Operacion(ABC):
    @abstractmethod
    def calcular(self, num1, num2):
        pass
    

class Suma(Operacion):
    def calcular(self, num1, num2):
            return num1 + num2

class Resta(Operacion):
    def calcular(self, num1, num2):
        return num1 - num2

class Multiplicacion(Operacion):
    def calcular(self, num1, num2):
        return num1 * num2

class Division(Operacion):
    def calcular(self, num1, num2):
        if num2 == 0:
            return "Error: División entre 0"
        return num1 / num2
    
class Calculadora:
    def __init__(self):
        self.operaciones = {}

    def registrar(self, nombre, operación):
        self.operaciones[nombre] = operación
    
    def calcular(self, operacion, num1, num2):
        if operacion not in self.operaciones:
            return "Operación no encontrada"
        return self.operaciones[operacion].calcular(num1, num2)
    
class Potencia(Operacion):
    def calcular(self, num1, num2):
        return math.pow(num1, num2)

calcu = Calculadora()

calcu.registrar("Suma", Suma())
calcu.registrar("Resta", Resta())
calcu.registrar("Multiplicacion", Multiplicacion())
calcu.registrar("Division", Division())
calcu.registrar("Potencia", Potencia())

print(calcu.calcular("Suma", 5, 5))
print(calcu.calcular("Resta", 10, 5))
print(calcu.calcular("Multiplicacion", 10, 8))
print(calcu.calcular("Division", 70, 2))
print(calcu.calcular("Potencia", 4, 2))
