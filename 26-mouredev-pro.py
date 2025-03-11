import os
import csv
import re
import random
from enum import Enum

class Status(Enum):
    ACTIVE = "Activo"
    INACTIVE = "Inactivo"

class CSVManager:
    
    _instance = None
    def __new__(cls, document="mouredev.csv"):
        if cls._instance is None:
            cls._instance = super(CSVManager, cls).__new__(cls)
            cls._instance.document = document

            if not os.path.exists(cls._instance.document):
                with open(cls._instance.document, "w", newline='') as archivo:
                    writer = csv.writer(archivo)
                    writer.writerow(["ID", "Nombre", "Email", "Estatus"])

        return cls._instance
    
    def __init__(self):
        self.status = Status.INACTIVE
        self.regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    def id_builder(self):
        ids = []
        with open(self.document, "r") as archivo:
            reader = csv.DictReader(archivo)
            for row in reader:
                ids.append(int(row["ID"]))

        return max(ids) + 1 if ids else 1
    
    def email_exist(self, email):
        with open(self.document, "r") as archivo:
            reader = csv.DictReader(archivo)
            for row in reader:
                if row["Email"].strip().lower() == email.strip().lower():
                    return True
                
        return False
    
    def email_validation(self, email: str):
        return bool(re.match(self.regex_email, email.strip()))
    
    def add_student(self, name, email, active):
        if self.email_exist(email):
            print("Error: Email ya registrado")
            return
        
        if not self.email_validation(email):
            print("Error: Email no valido")
            return

        new_id = self.id_builder()
        name_format = name.replace(" ", "-").title()
        new_status = Status.ACTIVE.value if active else Status.INACTIVE.value

        with open(self.document, "a", newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow([new_id, name_format, email.strip().lower(), new_status])

        print(f"✅ Estudiante {name} agregado con ID: {new_id}")

class Raffle:
    def __init__(self, document):
        self.document = document

    def ganadores(self):
        participantes = []
        with open(self.document, "r") as archivo:
            reader = csv.DictReader(archivo)
            for row in reader:
                if row["Estatus"].strip().lower() == Status.ACTIVE.value.lower():
                    participantes.append((int(row["ID"]), row["Email"]))

        if len(participantes) < 3:
            print("❌ Error: No hay suficientes estudiantes activos para el sorteo.")
            return None  

        ganadores = random.sample(participantes, 3)
        premios = ["🎉 1° ganador de una suscripción", "🎁 2° ganador de un descuento", "📚 3° ganador de un libro"]

        resultados = {ganador[1]: premio for ganador, premio in zip(ganadores, premios)}

        return resultados
    
class Methods:
    @staticmethod
    def results(documento):
        with open(documento, "r") as archivo:
            reader = csv.reader(archivo)
            next(reader)
            
            filas = list(reader)
            if not filas:
                print("📂 Contenido vacío")
                return

            print("\n📜 **Lista de Estudiantes** 📜")
            print("-" * 50)
            for fila in filas:
                print(f"{fila[0]} | {fila[1]} | {fila[2]} | {fila[3]}")
            print("-" * 50)

    @staticmethod
    def handle_error(error):
        if isinstance(error, ValueError):
            print("❌ Error: Ingresa un valor correcto")
        elif isinstance(error, KeyboardInterrupt):
            print("🛑 Usuario detuvo el programa (ctrl + c)")
            exit()

def menu():
    menu = {
        1: "Agregar estudiante",
        2: "Sorteo",
        3: "Ver documento",
        4: "Salir"
    }

    csv_manager = CSVManager()
    raffle = Raffle(csv_manager.document)

    while True:
        print("\n🎓 **Gestor de Sorteos - Mouredev** 🎓")
        for item, value in menu.items():
            print(f"{item} - {value}")
        
        try:
            option = abs(int(input("📌 Selecciona una opción: ")))

        except ValueError as error:
            Methods.handle_error(error)
            continue

        except KeyboardInterrupt as error:
            Methods.handle_error(error)

        if option == 1: 
            name = str(input("👤 Nombre: ")).strip().title()
            email = str(input("✉ Email: ")).strip()
            active = input("🔵 Estatus (Activo/Inactivo): ").strip().lower() == "activo"

            csv_manager.add_student(name, email, active)

        elif option == 2:
            resultado_sorteo = raffle.ganadores()
            if resultado_sorteo:
                print("\n🏆 **Ganadores del Sorteo:** 🏆")
                for ganador_email, premio in resultado_sorteo.items():
                    print(f"📧 {ganador_email}: {premio}")

        elif option == 3: 
            Methods.results(csv_manager.document)

        elif option == 4:
            print("🚪 Saliendo del programa... ¡Hasta la próxima!")
            if os.path.exists("mouredev.csv"):
                os.remove("mouredev.csv")
            break

menu()
