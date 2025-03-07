import random
import math

class IDBuild:
    @staticmethod
    def id_build(dicc, num1, num2):
        while True:
            new_id = random.randint(num1, num2)
            if new_id not in dicc:
                return new_id

class ManejoErrores:
    @staticmethod
    def handle_error(error, tipo):
        if isinstance(error, ValueError):
            print(f"Error: Valor incorrecto, debe ser un tipo {tipo}")
        elif isinstance(error, KeyboardInterrupt):
            print("\nUsuario saliendo del programa(ctrl+c)")
            exit()

class Participantes:

    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Participantes, cls).__new__(cls)
            cls._instance.participantes = {}

        return cls._instance

    def __init__(self):
        pass

    def registrar(self, nombre, pais, edad):
        new_id = IDBuild.id_build(self.participantes, 1000, 9999)

        if new_id in self.participantes:
            print("ID ya agregado")
            return
        
        if not (18 <= edad <= 50):
            print("Edad fuera del rango permitido")
            return
        
        nombre_format = nombre.replace(" ", "-")
        pais_format = pais.replace(" ",  "-")

        self.participantes[new_id] = {
            "nombre": nombre_format,
            "pais": pais_format,
            "edad": edad
        }

        return new_id
    
class EventoDeportivo:
    
    def __init__(self, gestor_participantes):
        self.eventos = {}
        self.ganadores = []
        self.gestor_participantes = gestor_participantes

    def registrar_evento(self, nombre, num_participantes):

        if num_participantes < 3 or num_participantes > 15  :
            print("Error: Min 3 participantes - Max 15")
            return

        new_id = IDBuild.id_build(self.eventos, 1, 100)

        if new_id in self.eventos:
            print("ID del evento ocupado")
            return
        
        nombre_format = nombre.replace(" ", "-")
        
        self.eventos[new_id] = {
            "nombre" : nombre_format,
            "participantes" : []
        }

        contador = 0

        while contador < num_participantes:
            print("Participantes")
            nombre_p = str(input("Nombre del participante: ")).lower().strip()
            
            try:
                pais_p = str(input("País del participante: ")).lower().strip()
            except(ValueError) as error:
                ManejoErrores.handle_error(error, "string")

            try:
                edad_p = abs(int(input("Edad del participante: ")))

            except (ValueError) as error:
                ManejoErrores.handle_error(error, "entero")
                continue
            except KeyboardInterrupt:
                ManejoErrores.handle_error(KeyboardInterrupt)

            participante_id = self.gestor_participantes.registrar(nombre_p, pais_p, edad_p)

            if participante_id:
                self.eventos[new_id]["participantes"].append(
                    self.gestor_participantes.participantes[participante_id]
                )
                contador += 1
        print("Registro exitoso")

class GestorEventos:
    def __init__(self, gestor_participantes):
        self.gestor_participantes = gestor_participantes
        self.eventos = {}
        self.ganadores = {}

    def crear_evento(self, nombre, num_participantes):
        evento = EventoDeportivo(self.gestor_participantes)
        evento.registrar_evento(nombre, num_participantes)

        self.eventos[nombre] = evento

    def ver_eventos(self):
        if not self.eventos:
            print("Sin eventos")
            return
        
        print("Lista de eventos \n")
        for nombre_evento, evento in self.eventos.items():
            for evento_id, detalles in evento.eventos.items():
                print(f"📌 ID: {evento_id} - Nombre: {detalles['nombre']}")
                print("👥 Participantes:")
                for p in detalles["participantes"]:
                    print(f"   - {p['nombre']} | {p['pais']} | {p['edad']} años")
                print("-" * 40)

    def simulador(self,id_evento):
        print("Simulador")

        evento_encontrado = None
        for evento in self.eventos.values():
            if id_evento in evento.eventos:
                evento_encontrado = evento
                break

        if evento_encontrado is None:
            print("Sin eventos")
            return
        
        participantes = evento_encontrado.eventos[id_evento]["participantes"]

        if len(participantes) < 3:
            print("No hay suficientes participantes")
            return
        
        if id_evento in self.ganadores:
            print("Los participantes de este evento ya participaron")
            return
        
        seleccionados = random.sample(participantes, 3)
        self.ganadores[id_evento] = seleccionados

        for i,p in enumerate(seleccionados, 1):
            print(f"{i}° {p['nombre']} | {p['pais']} | {p['edad']} años")

    def pais_ganador(self):

        if not self.ganadores:
            print("Sin ganadores aun")
            return
        
        conteo_paises = {}

        for id_evento, lista_ganadores in self.ganadores.items():
            for ganador in lista_ganadores:
                pais = ganador["pais"]
                if pais not in conteo_paises:
                    conteo_paises[pais] = 0
                conteo_paises[pais] += 1

        resultado = max(conteo_paises, key=conteo_paises.get)
        print(f"🏆 El país con más ganadores es {resultado} con {conteo_paises[resultado]} ganadores.")
        
def menu():
    gestor_participantes = Participantes()
    gestor_eventos = GestorEventos(gestor_participantes)

    menu = {
        1: "Registrar evento",
        2: "Ver eventos y participantes",
        3: "Simulador",
        4: "Medallas",
        5: "Salir"
    }

    while True:
        for item, value in menu.items():
            print(f"{item} - {value}")

        try:
            opcion = abs(int(input("Selecciona una opción: ")))

        except (ValueError) as error:
            ManejoErrores.handle_error(error, "entero")

        if opcion == 1:
            nombre_evento = str(input("Nombre del evento: ")).strip().lower()
            try:
                num_participantes = abs(int(input("Numero de participantes: ")))
            except(ValueError) as error:
                ManejoErrores.handle_error(error, "entero")
                continue
            
            gestor_eventos.crear_evento(nombre_evento, num_participantes)

        elif opcion == 2:
            gestor_eventos.ver_eventos()

        elif opcion == 3:
            id_evento = abs(int(input("Introduce el ID del evento: ")))
            gestor_eventos.simulador(id_evento)
        elif opcion == 4:
            gestor_eventos.pais_ganador()
        elif opcion == 5:
            print("Saliendo del programa")
            break
        else:
            print("Opción invalida")
            
menu()