from abc import ABC, abstractmethod

class Impresora(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Escaner(ABC):
    @abstractmethod
    def escanear(self):
        pass

class Fax(ABC):
    @abstractmethod
    def enviar_fax(self):
        pass


class ImpresoraBN(Impresora):
    def imprimir(self):
        return "🖨️ Imprimiendo Blanco y negro"
    
class ImpresoraColor(Impresora):
    def imprimir(self):
        return "🌈 Imprimiendo a color"
    
class MultiFuncional(Impresora, Escaner, Fax):
    def imprimir(self):
        return "🖨️ Imprimiendo Blanco y negro"
    
    def escanear(self):
        return "📄 Escaneando documento"
    
    def enviar_fax(self):
        return "📠 Mandando Fax"


def probar_impresora(lista_impresoras):
    for impresora in lista_impresoras:
        print(impresora.imprimir())

        if isinstance(impresora, Escaner):
            print(impresora.escanear())
        if isinstance(impresora, Fax):
            print(impresora.enviar_fax())

lista_impresora = [ImpresoraBN(), ImpresoraColor(), MultiFuncional()]

probar_impresora(lista_impresora)