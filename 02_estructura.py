class agenda():
    def __init__(self):
        self.agenda = {}
    
    def busqueda(self):

        while True:
            try:
                print("Búsqueda de usuarios")
                if not self.agenda : 
                    print("No hay registros en tu agenda")
                    return
                
                respuesta = str(input("Introduce el nombre: ")).strip().lower()
                respuesta_formateada = respuesta.replace(" ","-")
                if respuesta in self.agenda:
                    info = self.agenda[respuesta_formateada]
                    print(f"Nombre encontrado: {respuesta_formateada.capitalize()}")
                    print(f"Numero de teléfono: {info.get("numero", "No disponible")}")
                else:
                    print("No se encontró el nombre")
            except ValueError:
                print("Error: Introduce un valor correcto")

            continuar = str(input("¿Deseas buscar a otra persona? s/n: ")).strip().lower()
            if continuar == "n":
                break
                
    def agregar_contacto(self):
        print("Agrega a un usuario")    

        nombre = str(input("Introduce el nombre: ")).strip().lower()
        nombre_formateado = nombre.replace(" ", "-")

        if nombre_formateado in self.agenda:
            print("No hay registro con ese nombre")
            return
        
        while True:
            try:
                numero = abs(int(input("Introduce el numero(max 11): ")))
                if len(str(numero)) == 10:
                    self.agenda[nombre_formateado] = {"nombre": nombre_formateado, "numero": numero}
                    print(f"Contacto {nombre} registrado con éxito")
                    break
                else:
                    print("Error: Introduce un numero valido")
            except ValueError:
                print("Error: Introduce un numero correcto")
            

    def actualizar_contacto(self):
        print("Actualizar contacto")

        nombre = str(input("Introduce el nombre: ")).strip().lower()
        nombre_formateado = nombre.replace(" ", "-")

        if nombre_formateado not in self.agenda:
            print("No hay registro de ese contacto")
            return
        
        while True:
            try:
                numero = abs(int(input("Introduce el numero actualizar(max 11): ")))
                if len(str(numero)) == 10:
                    self.agenda[nombre_formateado]["numero"] = numero
                    break
                else:
                    print("Error: Introduce un numero valido")
            except ValueError:
                print("Error: Introduce un numero correcto")
    
    def eliminar_contacto(self):
        print("Eliminar contacto")

        nombre = str(input("Introduce el nombre: ")).strip().lower()
        nombre_formateado = nombre.replace(" ", "-")
        if nombre_formateado not in self.agenda:
            print("No hay registro de ese contacto")
            return
        if nombre_formateado in self.agenda:
            del self.agenda[nombre_formateado]
            print(f"Contacto {nombre_formateado.capitalize()} eliminado")
        
def menu():
    new_agenda = agenda()

    menu = {
        1: "Agregar nuevo contacto",
        2: "Buscar contacto",
        3: "Actualizar agenda",
        4: "Elimina a un contacto",
    }

    while True:
        print("Menu")
        for key, value in menu.items():
            print(f"{key}-{value}")
        try:
            opcion = abs(int(input("Selecciona una opción: ")))
            if opcion == 1:
                new_agenda.agregar_contacto()
            elif opcion == 2:
                new_agenda.busqueda()
            elif opcion == 3:
                new_agenda.actualizar_contacto()
            elif opcion == 4:
                new_agenda.eliminar_contacto()
            else:
                print("Error: Selecciona una opción valida")
        except ValueError:
            print("Error: Selecciona una opción valida")
        continuar = str(input("¿Deseas hacer otra operación s/n?: "))
        if continuar == "n":
            print("Saliendo del programa")
            break
        else:
            continue
            
menu()