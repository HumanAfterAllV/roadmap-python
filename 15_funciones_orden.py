estudiantes = {
    1: {"nombre": "Ana López", "fecha_nacimiento": "2005-03-14", "calificaciones": [9.2, 8.5, 7.8, 10]},
    2: {"nombre": "Carlos Pérez", "fecha_nacimiento": "2006-07-22", "calificaciones": [6.8, 7.4, 8.2, 6.5]},
    3: {"nombre": "María Gómez", "fecha_nacimiento": "2004-12-10", "calificaciones": [9.8, 9.5, 9.3, 10]},
    4: {"nombre": "Luis Fernández", "fecha_nacimiento": "2007-05-18", "calificaciones": [5.6, 6.2, 7.1, 5.8]},
    5: {"nombre": "Elena Ramírez", "fecha_nacimiento": "2003-09-30", "calificaciones": [8.9, 9.2, 9.7, 8.5]},
    6: {"nombre": "Pedro Sánchez", "fecha_nacimiento": "2005-11-05", "calificaciones": [7.5, 8.2, 8.0, 7.9]},
    7: {"nombre": "Laura Torres", "fecha_nacimiento": "2006-01-25", "calificaciones": [10, 9.8, 9.5, 10]},
    8: {"nombre": "Jorge Herrera", "fecha_nacimiento": "2004-06-15", "calificaciones": [8.2, 7.5, 6.9, 8.0]},
    9: {"nombre": "Sofia Méndez", "fecha_nacimiento": "2007-08-03", "calificaciones": [9.3, 9.1, 9.0, 9.5]},
    10: {"nombre": "Diego Castro", "fecha_nacimiento": "2005-04-12", "calificaciones": [7.0, 6.8, 7.2, 7.5]}
}


class Estudiantes:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Estudiantes, cls).__new__(cls)
            cls._instance.estudiantes_lista = estudiantes
        return cls._instance
    
    def __init__(self):
        self.promedios = {}
    
    def promedio_calificaciones(self):
        for estudiante in self.estudiantes_lista.values():
            promedio = sum(estudiante["calificaciones"]) / len(estudiante["calificaciones"])
            self.promedios[estudiante["nombre"]] = promedio
        
        for item, value in self.promedios.items():
            print(f"{item} - {value}")

        return self.promedios
    
    def mejores_estudiantes(self):

        if not self.promedios:
            print("Primero selecciona la opción 1: Promedios ")
            return
        for nombre, promedio in self.promedios.items():
            if promedio >= 9:
                print(f"{nombre} - {promedio}")

    def ordenar_por_nacimiento(self):
        print(sorted(self.estudiantes_lista.values(), key=lambda est: est["fecha_nacimiento"]))
    
    def mayor_calificaciones(self):
        calificaciones_totales = [cal for est in self.estudiantes_lista.values() for cal in est["calificaciones"]]
        mayor = max(calificaciones_totales)
        print(f"La mayor calificación es: {mayor}")


def menu():
    estudiantes = Estudiantes()
    menu = {
        1: "Promedio estudiantes",
        2: "Mejores estudiantes",
        3: "Nacimiento",
        4: "Mayor calificación",
        5: "Salir"
    }
    while True:
        print("Opciones")
        for item, value in menu.items():
            print(f"{item} - {value}")
        try:
            respuesta = abs(int(input("Opción: ")))

            if respuesta == 1:
                estudiantes.promedio_calificaciones()
            elif respuesta == 2:
                estudiantes.mejores_estudiantes()
            elif respuesta == 3:
                estudiantes.ordenar_por_nacimiento()
            elif respuesta == 4:
                estudiantes.mayor_calificaciones()
            elif respuesta == 5:
                print("Saliendo del programa")
                break

        except ValueError:
            print("Error: Opción invalida")
    
menu()