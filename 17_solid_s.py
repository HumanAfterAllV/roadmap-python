from enum import Enum
import random
import re   

class EstadoLibro(Enum):
    DISPONIBLE = "Disponible"
    PRESTADO = "Prestado"

class IDBuild:
    @staticmethod
    def id_build(dicc):
        while True:
            new_id = random.randint(1000, 9999)
            if new_id not in dicc:
                return new_id

class BookManager:

    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BookManager, cls).__new__(cls)
            cls._instance.libros = {}
        return cls._instance
    
    def __init__(self):
        self.estado = EstadoLibro.DISPONIBLE

    def registro(self, titulo, autor):

        libro_id = IDBuild.id_build(self.libros)

        if libro_id in self.libros:
            print("Libro con ID ya registrado, intenta otro ID")
            return
        
        self.libros[libro_id] = {
            "titulo": titulo,
            "autor": autor,
            "estado": self.estado
        }

        print(f"Libro: {titulo} registrado exitosamente")

    def libro_vista(self):

        for id_libro, datos in self.libros.items():
            print(f"ID: {id_libro} \n Titulo: {datos['titulo']} \n Autor: {datos['autor']} \n Estado: {datos['estado'].value}")

class UserManager:

    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserManager, cls).__new__(cls)
            cls._instance.usuarios = {}
        return cls._instance

    def __init__(self):
        self.regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        self.regex_telefono = r'^\+?\d{1,3}?[-.\s]?\(?\d{2,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{3,4}$'

    def validar(self, cadena, regex):
        return bool(re.match(regex, cadena))

    def registro_usuario(self, nombre, email, telefono):

        usuario_id = IDBuild.id_build(self.usuarios)

        if usuario_id in self.usuarios:
            print("Usuario ya registrado con ese id")
            return
        
        if not self.validar(email, self.regex_email):
            print("Error: email no valido")
            return
        
        if not self.validar(str(telefono), self.regex_telefono):
            print("Error: telefono no valido")
            return
        else:
            nombre_format = nombre.replace(" ", "-")
            self.usuarios[usuario_id] = {
                "nombre": nombre_format,
                "email" : email,
                "telefono": telefono,
            }
            print(f"Usuario {nombre_format} exitosamente registrado")
    def vista_usuarios(self):
        if not self.usuarios:
            print("Sin usuario registrados")
            return
        
        for id_usuarios,datos in self.usuarios.items():
            print(f"ID: {id_usuarios} \n Nombre: {datos['nombre']} \n Email: {datos['email']} \n Teléfono: {datos['telefono']}")
        
class ManagerLibrary:
    def __init__(self, book_manager, user_manager):
        self.book_manager = book_manager
        self.user_manager = user_manager

    def prestar_libros(self, usuario_id, libro_id):
        if usuario_id not in self.user_manager.usuarios:
            print("Usuario no registrado")
            return
        if libro_id not in self.book_manager.libros:
            print("Libro no registrado")
            return
        
        if self.book_manager.libros[libro_id]["estado"] == EstadoLibro.PRESTADO:
            print("Libro no disponible")
            return

        self.book_manager.libros[libro_id]["estado"] = EstadoLibro.PRESTADO

        if "libros_prestados" not in self.user_manager.usuarios[usuario_id]:
            self.user_manager.usuarios[usuario_id]["libros_prestados"] = []

        self.user_manager.usuarios[usuario_id]["libros_prestados"].append(libro_id)
        print(f"Libro ID {libro_id} prestado a Usuario ID {usuario_id}")

    def devolver_libros(self, usuario_id, libro_id):
        if usuario_id not in self.user_manager.usuarios:
            print("Usuario no registrado")
            return
        if libro_id not in self.book_manager.libros:
            print("Libro no registrado")
            return
        
        if "libros_prestados" not in self.user_manager.usuarios[usuario_id] or libro_id not in self.user_manager.usuarios[usuario_id]["libros_prestados"]:
            print("Error: Este usuario no tiene este libro prestado.")
            return

        
        self.book_manager.libros[libro_id]["estado"] = EstadoLibro.DISPONIBLE

        print("Libro devuelto con éxito")

def error_manager(error):
    if isinstance(error, ValueError):
        print("Error: Ingresa un opción valida")
    elif isinstance(error, KeyboardInterrupt):
        print("Usuario saliendo por comando (ctrl + c)")
        exit()

def menu():
    menu = {
        1: "Registrar libro",
        2: "Registrar usuario",
        3: "Lista de libros",
        4: "Lista de usuarios",
        5: "Prestar libro",
        6: "Devolver libros",
        7: "Salir",
    } 
    

    user_manager = UserManager()
    book_manager = BookManager()
    libro_manager = ManagerLibrary(book_manager , user_manager)

    while True:
        print("Biblioteca")
        for item, value in menu.items():
            print(f"{item} - {value}")

        try:
            opcion = abs(int(input("Ingresa una opción: ")))

            if opcion == 1:

                titulo = str(input("Ingresa titulo: ")).strip().upper()
                autor = str(input("Ingresa el autor: ")).strip().lower()

                book_manager.registro(titulo, autor)
            elif opcion == 2:

                nombre = str(input("Ingresa el nombre: ")).lower()
                email = str(input("Ingresa el email: "))
                telefono = abs(int(input("Ingresa el telefono: ")))

                user_manager.registro_usuario(nombre, email, telefono)

            elif opcion == 3:
                book_manager.libro_vista()
            
            elif opcion == 4:
                user_manager.vista_usuarios()

            elif opcion == 5:
                print("Lista de libros")
                book_manager.libro_vista()
                
                print("-----------------------")

                print("Lista de usuarios")
                user_manager.vista_usuarios()

                libro_id = abs(int(input("ID: ")))
                user_id = abs(int(input("User ID: ")))
                libro_manager.prestar_libros(user_id, libro_id)
            elif opcion == 6:
                print("Lista de libros")
                book_manager.libro_vista()
                
                print("-----------------------")

                print("Lista de usuarios")
                user_manager.vista_usuarios()
                
                libro_id = abs(int(input("ID: ")))
                user_id = abs(int(input("User ID: ")))
                libro_manager.devolver_libros(user_id, libro_id)

            elif opcion == 7:
                print("Saliendo del programa")
                break

            else:
                print("Opción incorrecta")

        except (ValueError) as error:
            error_manager(error)
        
        except KeyboardInterrupt:
            error_manager(KeyboardInterrupt())

menu()