class stack:
    def __init__(self):
        self.lista = []

    def agregar_documento(self):
        print("Agrega un documento")

        documento = str(input("Introduce el documento: ")).strip().lower()

        new_documento = documento.replace(" ", "-")
        
        print(f"Documento agregado con exito: {new_documento}")
        self.lista.append(new_documento)
    
    def imprimir_documento(self):
        if not self.lista:
            print("No hay ningún documento a imprimir")
            return

        documento = str(input("Documento a imprimir: ")).strip().lower()
        new_documento = documento.replace(" ", "-")

        if new_documento in self.lista:
            self.lista.remove(new_documento)
            print(f"Documento {new_documento} impreso")     
        else:
            print(f"El documento {new_documento} no se pudo imprimir")
    
    def lista_documentos(self):
        if not self.lista:
            print("Lista vacia")
            return
        
        for elemento in self.lista:
            print(f"{elemento}")


def menu():
    new_stack = stack()
    menu = {
        1: "Agregar un documento",
        2: "Imprimir",
        3: "Lista"
    }
    while True:
        for key, value in menu.items():
            print(f"{key} - {value}")
        try:
            respuesta = abs(int(input("¿Que deseas hacer?: ")))

            if respuesta == 1:
                new_stack.agregar_documento()
            elif respuesta == 2:
                new_stack.imprimir_documento()
            elif respuesta == 3:
                new_stack.lista_documentos()
            else:
                print("Error: Introduce un valor correcto")
        except ValueError:
            print("Error: Introduce un valor correcto")
        continuar = str(input("¿Deseas continuar s/n?")).strip().lower()
        if continuar == "n":
            print("Saliendo del programa")
            break
        else:
            continue

menu()