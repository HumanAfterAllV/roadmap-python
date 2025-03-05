import re

class SessionUsuario:
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            cls._instance = super(SessionUsuario, cls).__new__(cls)
            cls._instance.sesion = {}

        return cls._instance
    
    def iniciar_sesion(self, username, nombre, email):
        if not self.sesion:
            self.sesion["username"] = username
            self.sesion["nombre"] = nombre
            self.sesion["email"] = email
            print(f"Sesión iniciada: {username}")
        else:
            print("Error: Ya hay una sesión activa")

    def obtener_sesion(self):
        if self.sesion:
            return self.sesion
        else:
            print("No hay ninguna sesión")
            return None
        
    def cerrar_sesion(self):
        if self.sesion:
            self.sesion.clear()
            print("Sesion cerrada correctamente")
        else:
            print("No hay sesion")




regex_email = r'^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$'

def validar(cadena, regex):
        return bool(re.match(regex, cadena))

def manejar_error(error): 
    if isinstance(error, ValueError):
        print("Error: Debe ingresar un número válido.")
    elif isinstance(error, KeyboardInterrupt):
        print("\nUsuario saliendo del programa por Ctrl + C.")
        exit()  




    
sesion = SessionUsuario()

menu = {
    1: "Iniciar sesión",
    2: "Obtener sesión",
    3: "Cerrar sesión",
    4: "Salir"
}
while True:
    for item, value in menu.items():
        print(f"{item} - {value}")
    try:
        opcion = abs(int(input("Opción: ")))

        if opcion == 1:
            nombre = str(input("Ingresa tu nombre: ")).strip()
            username = str(input("Ingresa tu username: ")).strip()
            email = str(input("Ingresa tu email: ")).strip()

            if validar(email, regex_email):
                sesion.iniciar_sesion(username,nombre, email,)
            else:
                print("Error: El email ingresado no es valido")
        elif opcion == 2:
            datos_sesion = sesion.obtener_sesion()
            if datos_sesion:
                for item, value in datos_sesion.items():
                    print(f"{item} - {value}")
            
        elif opcion == 3:
            sesion.cerrar_sesion()
        elif opcion == 4:
            print("Saliendo del programa")
            break
    
    except (ValueError) as error:
        manejar_error(error)
    except KeyboardInterrupt:
        manejar_error(KeyboardInterrupt())
    
    
    

